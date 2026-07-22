'use strict';

const DATA_URL = 'six_data_v4.json';
const FACTORS = {
  H: ['Implementable labor opportunity', 'Current compensation exposed to implementable AI task substitution'],
  F: ['Transferable-firm opportunity', 'Expected lens-eligible LMM control transfers over five years'],
  C: ['Commercial retention', 'Share of implemented gross benefit retained commercially'],
  D: ['Operator-required demand', 'Year-five constant-price service quantity still needing an operator']
};
const TIER_ORDER = ['HIGHEST_PRIORITY', 'PRIORITY', 'CONDITIONAL', 'LOW_PRIORITY', 'STRUCTURAL_OUT', 'UNKNOWN'];
const state = {records: [], summary: null, query: '', tiers: new Set(), readiness: new Set(), crossing: false, heterogeneous: false, sort: 'score-desc', lastFocus: null};

const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const esc = value => String(value ?? '').replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
const label = value => String(value ?? 'UNKNOWN').toLowerCase().replaceAll('_', ' ').replace(/\b\w/g, c => c.toUpperCase());
const score = value => value == null ? '—' : Number(value).toFixed(2);
const compactNumber = value => Number(value).toFixed(4).replace(/\.?0+$/, '');
const evidenceLabel = value => label(value === 'mixed' ? 'MIXED' : value === 'elicited' ? 'ELICITED' : value);

async function init() {
  try {
    const response = await fetch(DATA_URL);
    if (!response.ok) throw new Error(`${DATA_URL} returned ${response.status}`);
    const data = await response.json();
    state.records = data.records;
    state.summary = data.summary;
    renderAll();
    $('#loading').hidden = true;
    switchView(location.hash.slice(1) || 'fleet', false);
    bindEvents();
  } catch (error) {
    $('#loading').hidden = true;
    $('#error').hidden = false;
    $('#error').innerHTML = `<strong>Dashboard data could not be loaded.</strong><br>${esc(error.message)}<br><small>Serve the repository root over HTTP.</small>`;
  }
}

function renderAll() {
  renderMetrics();
  renderFilters();
  renderFleet();
  renderMethod();
}

function renderMetrics() {
  const s = state.summary;
  $('#campaign-total').textContent = `${s.membership} / ${s.membership}`;
  const metrics = [
    [s.complete_base, 'Complete bases', `${s.missing_base} evidence-first`],
    [s.tier_counts.HIGHEST_PRIORITY || 0, 'Highest priority', 'research priority, not buy signal'],
    [s.tier_counts.PRIORITY || 0, 'Priority', `${s.tier_counts.CONDITIONAL || 0} conditional`],
    [s.robust_tier_count, 'Stable tier', `${s.membership - s.robust_tier_count} crossing intervals`],
    [s.readiness_counts.MODEL_CONDITIONED || 0, 'Model-conditioned', 'assumptions remain visible']
  ];
  $('#campaign-metrics').innerHTML = metrics.map(([value, title, detail]) => `<div class="metric"><strong>${esc(value)}</strong><span>${esc(title)}</span><small>${esc(detail)}</small></div>`).join('');
}

function renderFilters() {
  const tierValues = TIER_ORDER.filter(tier => state.records.some(record => (record.tier || 'UNKNOWN') === tier));
  $('#verdict-filters').innerHTML = tierValues.map(value => check('tier', value, label(value), state.records.filter(r => (r.tier || 'UNKNOWN') === value).length)).join('');
  const readinessValues = [...new Set(state.records.map(record => record.readiness))].sort();
  $('#confidence-filters').innerHTML = readinessValues.map(value => check('readiness', value, label(value), state.records.filter(r => r.readiness === value).length)).join('');
  $('#borderline-count').textContent = state.records.filter(record => !record.robust_tier).length;
  $('#heterogeneous-count').textContent = state.records.filter(record => record.heterogeneous).length;
}

function check(group, value, text, count) {
  return `<label class="check-row"><input type="checkbox" data-filter-group="${group}" value="${esc(value)}"><span>${esc(text)}</span><small>${count}</small></label>`;
}

function filteredRecords() {
  const query = state.query.toLowerCase();
  return state.records.filter(record => {
    if (query && !`${record.naics} ${record.title} ${record.sector?.name || ''}`.toLowerCase().includes(query)) return false;
    if (state.tiers.size && !state.tiers.has(record.tier || 'UNKNOWN')) return false;
    if (state.readiness.size && !state.readiness.has(record.readiness)) return false;
    if (state.crossing && record.robust_tier) return false;
    if (state.heterogeneous && !record.heterogeneous) return false;
    return true;
  }).sort((a, b) => {
    if (state.sort === 'score-asc') return (a.A ?? Infinity) - (b.A ?? Infinity);
    if (state.sort === 'naics') return a.naics.localeCompare(b.naics);
    if (state.sort === 'v3-desc') return b.v3.S - a.v3.S;
    return (a.rank ?? Infinity) - (b.rank ?? Infinity);
  });
}

function renderFleet() {
  const records = filteredRecords();
  $('#fleet-result-count').textContent = `${records.length} ${records.length === 1 ? 'industry' : 'industries'}`;
  $('#fleet-context').textContent = records.length === state.records.length ? 'v4.3 Stage 1 · existing Phase 4 universe' : `Filtered from ${state.records.length} records`;
  $('#fleet-empty').hidden = records.length > 0;
  $('#fleet-list').innerHTML = records.map(fleetRow).join('');
  $$('.fleet-row').forEach(button => button.addEventListener('click', () => openDrawer(state.records.find(r => r.naics === button.dataset.naics), button)));
}

function fleetRow(record) {
  const tier = record.tier || 'UNKNOWN';
  const crossing = !record.robust_tier;
  const badges = [
    `<span class="badge conf-low">${esc(label(record.readiness))}</span>`,
    `<span class="badge caveat">${esc(label(record.action))}</span>`,
    crossing ? '<span class="badge borderline">Crossing interval</span>' : '<span class="badge">Stable tier</span>',
    record.heterogeneous ? '<span class="badge">Heterogeneous</span>' : ''
  ].join('');
  const sparks = Object.entries(FACTORS).map(([factor]) => {
    const value = record.factors[factor].base;
    return `<span class="spark-row"><b>${factor}</b><i class="spark-track"><i class="spark-fill" style="width:${value == null ? 0 : value * 10}%"></i></i><em>${value == null ? '—' : Number(value).toFixed(1)}</em></span>`;
  }).join('');
  return `<button class="fleet-row" data-naics="${record.naics}" aria-label="Open ${esc(record.title)} v4 evidence">
    <span class="rank">${record.rank == null ? '—' : String(record.rank).padStart(2, '0')}</span>
    <span class="industry"><span class="naics">${record.naics}<span class="sector-label"> · ${esc(record.sector?.name || 'Phase 4')}</span></span><strong>${esc(record.title)}</strong><span class="badges">${badges}</span></span>
    <span class="factor-spark">${sparks}</span>
    <span class="result-score"><strong>${score(record.A)}</strong><span class="verdict-${tier.toLowerCase()}">${esc(label(tier))}</span><small>v3 ${score(record.v3.S)} · ${esc(label(record.v3.verdict))}</small></span>
    <span class="row-arrow">→</span>
  </button>`;
}

function renderMethod() {
  const cuts = [['Highest priority', 'A ≥ 7.5 · L ≥ 6'], ['Priority', 'A ≥ 6 · L ≥ 4'], ['Conditional', 'A ≥ 4.5 · L ≥ 2'], ['Low priority', 'A ≥ 3 · L ≥ 1'], ['Structural out', 'otherwise']];
  $('#method-cuts').innerHTML = cuts.map(([name, value]) => `<div class="cut-row"><span>${name}</span><strong>${value}</strong></div>`).join('');
  $('#factor-glossary').innerHTML = Object.entries(FACTORS).map(([key, [name, short]]) => `<article class="glossary-item"><b>${key}</b><strong>${name}</strong><p>${short}</p></article>`).join('');
}

function bindEvents() {
  $$('.nav-button').forEach(button => button.addEventListener('click', () => switchView(button.dataset.view)));
  $('#fleet-search').addEventListener('input', event => { state.query = event.target.value.trim(); renderFleet(); });
  $('#fleet-sort').addEventListener('change', event => { state.sort = event.target.value; renderFleet(); });
  $('#filter-borderline').addEventListener('change', event => { state.crossing = event.target.checked; renderFleet(); });
  $('#filter-heterogeneous').addEventListener('change', event => { state.heterogeneous = event.target.checked; renderFleet(); });
  $$('[data-filter-group]').forEach(input => input.addEventListener('change', event => {
    const target = event.target.dataset.filterGroup === 'tier' ? state.tiers : state.readiness;
    event.target.checked ? target.add(event.target.value) : target.delete(event.target.value);
    renderFleet();
  }));
  $('#reset-filters').addEventListener('click', resetFilters);
  $('#drawer-backdrop').addEventListener('click', closeDrawer);
  addEventListener('keydown', event => { if (event.key === 'Escape' && !$('#record-drawer').hidden) closeDrawer(); });
  addEventListener('popstate', () => switchView(location.hash.slice(1) || 'fleet', false));
}

function resetFilters() {
  state.query = ''; state.tiers.clear(); state.readiness.clear(); state.crossing = false; state.heterogeneous = false;
  $('#fleet-search').value = ''; $('#filter-borderline').checked = false; $('#filter-heterogeneous').checked = false;
  $$('[data-filter-group]').forEach(input => { input.checked = false; });
  renderFleet();
}

function switchView(view, push = true) {
  if (!['fleet', 'methodology'].includes(view)) view = 'fleet';
  $$('.view').forEach(section => { section.hidden = section.id !== `${view}-view`; });
  $$('.nav-button').forEach(button => button.classList.toggle('active', button.dataset.view === view));
  if (push && location.hash !== `#${view}`) history.pushState(null, '', `#${view}`);
  scrollTo({top: 0, behavior: 'smooth'});
}

function openDrawer(record, trigger) {
  state.lastFocus = trigger;
  $('#drawer-content').innerHTML = drawerContent(record);
  $('#record-drawer').hidden = false;
  $('#drawer-backdrop').hidden = false;
  document.body.classList.add('drawer-open');
  $('.drawer-close').addEventListener('click', closeDrawer);
  $('.drawer-close').focus();
}

function closeDrawer() {
  $('#record-drawer').hidden = true;
  $('#drawer-backdrop').hidden = true;
  document.body.classList.remove('drawer-open');
  state.lastFocus?.focus();
}

function drawerContent(record) {
  const tier = record.tier || 'UNKNOWN';
  const factorCards = Object.entries(FACTORS).map(([key, [name, short]]) => factorCard(record, key, name, short)).join('');
  const v3Scores = Object.entries(record.v3.scores).map(([key, value]) => `${key} ${Number(value).toFixed(1)}`).join(' · ');
  const sourceReview = record.source_review?.outcome ? `<p><strong>Source-run review:</strong> ${esc(label(record.source_review.outcome))}. ${esc(record.source_review.summary || '')}</p>` : '';
  return `<header class="drawer-hero"><button class="drawer-close" aria-label="Close record">×</button>
    <div class="drawer-kicker">NAICS ${record.naics} · v4.3 Stage 1</div><h2 id="drawer-title">${esc(record.title)}</h2>
    <div class="drawer-badges"><span class="badge">${esc(label(record.readiness))}</span><span class="badge review">${esc(label(record.action))}</span>${record.robust_tier ? '<span class="badge">Stable tier</span>' : '<span class="badge borderline">Crossing interval</span>'}</div>
    <div class="score-ledger"><div class="big-score"><span>Breadth score A</span><strong>${score(record.A)}</strong><small>${esc(label(tier))}</small></div>
    <div class="aggregate-equation">A = mean(H,F,C,D) · L = weakest factor<strong>L ${score(record.L)} · ${esc(label(record.tier_interval[0]))} → ${esc(label(record.tier_interval[1]))}</strong></div></div></header>
    <div class="drawer-panel"><h3>v4 factors and evidence</h3><div class="factor-chain">${factorCards}</div>
    <h3>Why it lands here</h3><div class="caveat-summary"><strong>Driver: ${esc(record.principal_driver || 'unknown')} · Weakness: ${esc(record.principal_weakness || 'unknown')}</strong><br>All complete records remain model-conditioned, so the tier prioritizes further research and the action is ${esc(label(record.action))}.</div>
    <h3>v3 comparison</h3><div class="caveat-summary"><strong>v3 ${score(record.v3.S)} · ${esc(label(record.v3.verdict))} · ${esc(record.v3.confidence)} confidence</strong><br>${esc(v3Scores)}</div>${sourceReview}
    <h3>Reused source registry</h3><div class="source-registry">${record.sources.map(sourceCard).join('')}</div>
    <h3>Artifacts</h3><div class="artifact-list"><a class="artifact-link" href="../pipeline/v4_3/runs/${record.naics}/v4_3_minimal.json"><span class="artifact-icon">V4</span><span><strong>v4 score record</strong><small>Separate deterministic Stage 1 output</small></span><span>↗</span></a><a class="artifact-link" href="../pipeline/runs/${record.naics}/${record.source_run.run_id}.json"><span class="artifact-icon">V3</span><span><strong>Reused v3 evidence record</strong><small>${esc(record.source_run.run_id)}</small></span><span>↗</span></a></div></div>`;
}

function factorCard(record, key, name, short) {
  const factor = record.factors[key];
  const leaves = Object.entries(record.evidence[key].leaves || {}).map(([leaf, value]) => leafRow(leaf, value)).join('');
  return `<article class="factor-card"><div class="factor-button"><span class="factor-letter">${key}</span><span class="factor-name"><strong>${esc(name)}</strong><small>${esc(short)}</small></span><span class="factor-score">${score(factor.base)}</span></div><div class="factor-details" style="display:block"><div class="factor-formula">Range ${score(factor.low)}–${score(factor.high)} · ${esc(evidenceLabel(factor.evidence_state))} evidence</div><div class="input-list">${leaves}</div></div></article>`;
}

function leafRow(name, value) {
  if (typeof value !== 'object' || value == null) return '';
  const selectedRaw = value.value ?? value.base ?? value.terminal_class ?? '—';
  const selected = typeof selectedRaw === 'number' ? compactNumber(selectedRaw) : selectedRaw;
  const range = value.low != null || value.high != null ? `${score(value.low)}–${score(value.high)}` : 'Not numeric';
  return `<article class="input-card"><div class="input-button"><span class="input-name"><strong>${esc(name)}</strong><small>${esc(label(value.state || 'context'))}</small></span><span class="input-value">${esc(selected)}</span><span class="method-pill method-estimate">${esc(range)}</span></div>${value.rationale ? `<div class="input-details" style="display:block">${esc(value.rationale)}</div>` : ''}</article>`;
}

function sourceCard(source) {
  const title = esc(source.title || source.id);
  const heading = /^https?:\/\//i.test(source.url || '') ? `<a href="${esc(source.url)}" target="_blank" rel="noopener">${title} ↗</a>` : `<strong>${title}</strong>`;
  return `<article class="source-card"><div class="source-top"><span>${esc(source.id)}</span><time>${esc(source.access_date || '')}</time></div>${heading}<p>${esc(source.what_it_supports || source.supports || '')}</p></article>`;
}

init();
