'use strict';

const DATA_URLS = {
  fleet: 'six_data_v3.json',
  campaign: '../pipeline/build/campaign_report_v3_1_2.json',
  golden: '../pipeline/build/golden_analysis_v3_1_2.json',
  thresholds: '../pipeline/build/thresholds.json'
};

const FACTORS = {
  V: { name: 'Value creation', short: 'AI-addressable labor value', inputs: ['labor_share', 'ai_replaceable_share'] },
  C: { name: 'Capture', short: 'Share of value the operator retains', inputs: ['pi_dist', 'pi_moat'] },
  A: { name: 'Adoption timing', short: 'Time to 50% effective adoption', inputs: ['t50_years', 'current_adoption_pct', 'historical_analogs'] },
  B: { name: 'Buyability', short: 'Target depth, ownership, crowding', inputs: ['n_band', 'owners_60plus_pct', 'active_consolidators'] },
  M: { name: 'Multiple potential', short: 'Entry-to-exit expansion', inputs: ['buy_mult', 'exit_mult', 'pricing_structure'] }
};

const MEMO_LABELS = {
  executive_view: 'Executive view',
  ai_changes_work: 'How AI changes the work', how_ai_changes_work: 'How AI changes the work',
  value_capture: 'Value capture',
  adoption_timing: 'Adoption timing',
  consolidation_economics: 'Consolidation & economics',
  terminal_demand: 'Terminal demand',
  risks_and_uncertainty: 'Risks & uncertainty'
};

const INPUT_LABELS = {
  labor_share: 'Labor share', ai_replaceable_share: 'AI-replaceable share', pi_dist: 'Distribution retention',
  pi_moat: 'Moat retention', t50_years: 'Years to 50%', current_adoption_pct: 'Current adoption',
  historical_analogs: 'Historical analog', n_band: '$1–10M EBITDA targets', owners_60plus_pct: 'Owners age 60+',
  active_consolidators: 'Active consolidators', buy_mult: 'Entry multiple', exit_mult: 'Exit multiple',
  pricing_structure: 'Pricing structure'
};

const state = {
  fleet: [], campaign: null, golden: null, thresholds: null,
  view: 'fleet', query: '', verdicts: new Set(), confidences: new Set(),
  borderline: false, heterogeneous: false, sort: 'score-desc', lastFocus: null,
  currentRecord: null, currentReview: null, currentKind: 'fleet', currentTab: 'thesis', exclusionTitles: {}
};

const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const esc = value => String(value ?? '').replace(/[&<>'"]/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[char]));
const pct = value => `${(Number(value) * 100).toFixed(Number(value) < .1 ? 1 : 0)}%`;
const score = value => Number(value).toFixed(2);
const verdictLabel = value => String(value).replace('_', ' ').replace(/\b\w/g, c => c.toUpperCase());
const count = (items, predicate) => items.filter(predicate).length;
const sourceIsUrl = source => /^https?:\/\//i.test(source || '');
const ordinal = value => {
  const rounded = Math.round(Number(value));
  const mod100 = rounded % 100;
  const suffix = mod100 >= 11 && mod100 <= 13 ? 'th' : ({1:'st',2:'nd',3:'rd'}[rounded % 10] || 'th');
  return `${rounded}${suffix}`;
};

function showToast(message) {
  const toast = $('#toast');
  toast.textContent = message;
  toast.classList.add('show');
  clearTimeout(showToast.timer);
  showToast.timer = setTimeout(() => toast.classList.remove('show'), 1800);
}

async function getJson(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`${url} returned ${response.status}`);
  return response.json();
}

async function init() {
  try {
    const [fleet, campaign, golden, thresholds] = await Promise.all(Object.values(DATA_URLS).map(getJson));
    state.fleet = fleet.records;
    state.campaign = campaign;
    state.golden = golden;
    state.thresholds = thresholds;
    if (!campaign.campaign_closed || !campaign.phase4_complete) throw new Error('The Phase-4 campaign is not closed.');
    const excludedRecords = await Promise.all(campaign.exclusions.map(item => getJson(`../pipeline/runs/${item.naics}/${item.run_id}.json`)));
    excludedRecords.forEach(record => { state.exclusionTitles[record.naics] = record.title; });
    renderAll();
    $('#loading').hidden = true;
    switchView(location.hash.slice(1) || 'fleet', false);
    bindGlobalEvents();
  } catch (error) {
    $('#loading').hidden = true;
    const box = $('#error');
    box.hidden = false;
    box.innerHTML = `<strong>Dashboard data could not be loaded.</strong><br>${esc(error.message)}<br><small>Serve the repository root over HTTP so the generated Phase-4 files are available.</small>`;
  }
}

function renderAll() {
  renderCampaignMetrics();
  renderFilters();
  renderFleet();
  renderGolden();
  renderExclusions();
  renderMethodology();
  $('#nav-excluded-count').textContent = state.campaign.excluded;
}

function renderCampaignMetrics() {
  const c = state.campaign;
  $('#campaign-total').textContent = `${c.planned.total} / ${c.planned.total}`;
  const metrics = [
    [c.published, 'Published', `${c.planned.fleet - c.excluded} fleet + ${c.planned.golden} golden`],
    [c.excluded, 'Excluded', 'kept outside rankings'],
    [c.attempt_counts.total, 'Total attempts', `${c.attempt_counts.remediation} bounded remediations`],
    [c.source_support.supported, 'Supported sources', `${c.source_support.partially_supported} partially supported`],
    [state.golden.separation_pass ? 'PASS' : 'FAIL', 'Golden separation', 'diagnostic only']
  ];
  $('#campaign-metrics').innerHTML = metrics.map(([value, label, detail]) =>
    `<div class="metric"><strong>${esc(value)}</strong><span>${esc(label)}</span><small>${esc(detail)}</small></div>`
  ).join('');
}

function renderFilters() {
  const verdictOrder = ['conditional', 'pass', 'kill', 'strong', 'hell_yes'];
  const verdicts = [...new Set(state.fleet.map(record => record.verdict))].sort((a,b) => verdictOrder.indexOf(a) - verdictOrder.indexOf(b));
  $('#verdict-filters').innerHTML = verdicts.map(value => checkTemplate('verdict', value, verdictLabel(value), count(state.fleet, r => r.verdict === value))).join('');
  const confidences = [...new Set(state.fleet.map(record => record.confidence))].sort();
  $('#confidence-filters').innerHTML = confidences.map(value => checkTemplate('confidence', value, value, count(state.fleet, r => r.confidence === value))).join('');
  $('#borderline-count').textContent = count(state.fleet, r => r.borderline);
  $('#heterogeneous-count').textContent = count(state.fleet, r => r.heterogeneous);
}

function checkTemplate(group, value, label, total) {
  return `<label class="check-row"><input type="checkbox" data-filter-group="${group}" value="${esc(value)}"><span>${esc(label)}</span><small>${total}</small></label>`;
}

function filteredFleet() {
  const query = state.query.toLowerCase();
  const result = state.fleet.filter(record => {
    if (query && !`${record.naics} ${record.title} ${record.sector.name}`.toLowerCase().includes(query)) return false;
    if (state.verdicts.size && !state.verdicts.has(record.verdict)) return false;
    if (state.confidences.size && !state.confidences.has(record.confidence)) return false;
    if (state.borderline && !record.borderline) return false;
    if (state.heterogeneous && !record.heterogeneous) return false;
    return true;
  });
  return result.sort((a,b) => {
    if (state.sort === 'score-asc') return a.S - b.S;
    if (state.sort === 'percentile-desc') return b.percentile - a.percentile;
    if (state.sort === 'naics') return a.naics.localeCompare(b.naics);
    return b.S - a.S;
  });
}

function renderFleet() {
  const records = filteredFleet();
  $('#fleet-result-count').textContent = `${records.length} ${records.length === 1 ? 'industry' : 'industries'}`;
  $('#fleet-context').textContent = records.length === state.fleet.length ? 'Published fleet · latest reviewed attempts' : `Filtered from ${state.fleet.length} published fleet records`;
  $('#fleet-empty').hidden = records.length > 0;
  $('#fleet-list').innerHTML = records.map((record, index) => fleetRow(record, index)).join('');
  $$('.fleet-row').forEach(button => button.addEventListener('click', () => openFleet(button.dataset.naics, button)));
}

function fleetRow(record, index) {
  const badges = [
    `<span class="badge conf-${record.confidence.toLowerCase()}">${esc(record.confidence)} confidence</span>`,
    `<span class="badge caveat">Reviewed · caveats</span>`,
    record.borderline ? '<span class="badge borderline">Borderline</span>' : '',
    record.heterogeneous ? '<span class="badge">Heterogeneous</span>' : ''
  ].join('');
  const sparks = Object.entries(record.scores).map(([factor, value]) =>
    `<span class="spark-row"><b>${factor}</b><i class="spark-track"><i class="spark-fill" style="width:${Math.max(0,Math.min(100,value*10))}%"></i></i><em>${Number(value).toFixed(1)}</em></span>`
  ).join('');
  return `<button class="fleet-row" data-naics="${record.naics}" aria-label="Open ${esc(record.title)} evidence">
    <span class="rank">${String(index + 1).padStart(2,'0')}</span>
    <span class="industry"><span class="naics">${record.naics}<span class="sector-label"> · ${esc(record.sector.name)}</span></span><strong>${esc(record.title)}</strong><span class="badges">${badges}</span></span>
    <span class="factor-spark" aria-label="Factor scores">${sparks}</span>
    <span class="result-score"><strong>${score(record.S)}</strong><span class="verdict-${record.verdict}">${verdictLabel(record.verdict)}</span><small>${ordinal(record.percentile)} percentile</small></span>
    <span class="row-arrow" aria-hidden="true">→</span>
  </button>`;
}

function renderGolden() {
  const g = state.golden;
  $('#golden-summary').innerHTML = `<div class="diag-lead"><strong>${g.separation_pass ? 'Separation passed' : 'Separation failed'}</strong><span>Mechanics ${g.mechanics_errors.length ? 'require review' : 'clean'} · no rerun trigger</span></div>
    <div class="diag-stat"><strong>${g.records.length}</strong><small>Independent runs</small></div>
    <div class="diag-stat"><strong>${g.mechanics_errors.length}</strong><small>Mechanics errors</small></div>
    <div class="diag-stat"><strong>${g.uncaught_melters.length}</strong><small>Uncaught melters</small></div>
    <div class="diag-stat"><strong>${g.review_outcome_counts.publishable_with_caveats}</strong><small>With caveats</small></div>`;
  const classes = [['winner','Known winners'], ['melter','Known melters'], ['control','Controls']];
  $('#golden-groups').innerHTML = classes.map(([klass,label]) => {
    const rows = g.records.filter(r => r.class === klass);
    return `<section class="golden-group"><h2>${label} · ${rows.length}</h2><div class="golden-grid">${rows.map(record => goldenCard(record,klass)).join('')}</div></section>`;
  }).join('');
  $$('.golden-card').forEach(button => button.addEventListener('click', () => openGolden(button.dataset.naics, button)));
}

function goldenCard(record, klass) {
  return `<button class="golden-card" data-naics="${record.naics}" aria-label="Open golden diagnostic for ${esc(record.title)}">
    <span class="golden-card-head"><span>${record.naics}</span><i class="${klass}"></i></span>
    <h3>${esc(record.title)}</h3>
    <span class="golden-card-foot"><strong>${score(record.S)}</strong><span>${verdictLabel(record.verdict)}<br>${record.confidence} confidence</span></span>
  </button>`;
}

function renderExclusions() {
  const c = state.campaign;
  $('#exclusions-summary').innerHTML = `<strong>${c.excluded}</strong><span>record remains excluded after the single permitted remediation. Its mechanics pass; material evidence defects keep it outside publication.</span>`;
  $('#exclusions-list').innerHTML = c.exclusions.map(exclusion => {
    const material = exclusion.findings.filter(f => f.severity === 'material');
    return `<article class="exclusion-card"><div class="exclusion-head"><div><span class="naics">${exclusion.naics} · FLEET · ATTEMPT ${exclusion.attempt}</span><h2>${esc(titleForNaics(exclusion.naics))}</h2><p>${esc(exclusion.run_id)}</p></div><span class="reject-pill">${esc(exclusion.outcome)}</span></div>
      <div class="exclusion-body"><p>${esc(exclusion.summary)}</p><div class="material-findings">${material.map(f => `<div class="finding"><strong>${esc(f.category.replaceAll('_',' '))}</strong><p>${esc(f.materiality)}</p></div>`).join('')}</div>
      <button class="open-exclusion" data-naics="${exclusion.naics}">Inspect excluded record →</button></div></article>`;
  }).join('');
  $$('.open-exclusion').forEach(button => button.addEventListener('click', () => openExcluded(button.dataset.naics, button)));
}

function renderMethodology() {
  const cuts = state.thresholds.verdict_cuts;
  $('#method-cuts').innerHTML = Object.entries(cuts).map(([name,value]) => `<div class="cut-row"><span>${verdictLabel(name)}</span><strong>S ≥ ${Number(value).toFixed(1)}</strong></div>`).join('');
  $('#factor-glossary').innerHTML = Object.entries(FACTORS).map(([key,value]) => `<article class="glossary-item"><b>${key}</b><strong>${value.name}</strong><p>${value.short}</p></article>`).join('');
}

function bindGlobalEvents() {
  $$('.nav-button').forEach(button => button.addEventListener('click', () => switchView(button.dataset.view)));
  $('#fleet-search').addEventListener('input', event => { state.query = event.target.value.trim(); renderFleet(); });
  $('#fleet-sort').addEventListener('change', event => { state.sort = event.target.value; renderFleet(); });
  $('#filter-borderline').addEventListener('change', event => { state.borderline = event.target.checked; renderFleet(); });
  $('#filter-heterogeneous').addEventListener('change', event => { state.heterogeneous = event.target.checked; renderFleet(); });
  $$('[data-filter-group]').forEach(input => input.addEventListener('change', event => {
    const target = event.target.dataset.filterGroup === 'verdict' ? state.verdicts : state.confidences;
    event.target.checked ? target.add(event.target.value) : target.delete(event.target.value);
    renderFleet();
  }));
  $('#reset-filters').addEventListener('click', resetFilters);
  $('#drawer-backdrop').addEventListener('click', closeDrawer);
  addEventListener('keydown', event => { if (event.key === 'Escape' && !$('#record-drawer').hidden) closeDrawer(); });
  addEventListener('popstate', () => switchView(location.hash.slice(1) || 'fleet', false));
}

function resetFilters() {
  state.query = ''; state.verdicts.clear(); state.confidences.clear(); state.borderline = false; state.heterogeneous = false;
  $('#fleet-search').value = ''; $('#filter-borderline').checked = false; $('#filter-heterogeneous').checked = false;
  $$('[data-filter-group]').forEach(input => { input.checked = false; });
  renderFleet();
}

function switchView(view, push = true) {
  const accepted = ['fleet','golden','exclusions','methodology'];
  if (!accepted.includes(view)) view = 'fleet';
  state.view = view;
  $$('.view').forEach(section => { section.hidden = section.id !== `${view}-view`; });
  $$('.nav-button').forEach(button => {
    const active = button.dataset.view === view;
    button.classList.toggle('active', active);
    active ? button.setAttribute('aria-current','page') : button.removeAttribute('aria-current');
  });
  if (push && location.hash !== `#${view}`) history.pushState(null,'',`#${view}`);
  scrollTo({top:0,behavior:'smooth'});
}

function titleForNaics(naics) {
  return state.fleet.find(r => r.naics === naics)?.title || state.golden.records.find(r => r.naics === naics)?.title || state.exclusionTitles[naics] || `NAICS ${naics}`;
}

function campaignRecord(kind, naics) {
  return state.campaign.records.find(record => record.kind === kind && record.naics === naics);
}

function openFleet(naics, trigger) {
  const record = state.fleet.find(item => item.naics === naics);
  openDrawer(record, record.acceptance.review, 'fleet', trigger);
}

async function openGolden(naics, trigger) {
  const campaign = campaignRecord('golden', naics);
  if (!campaign) return showToast('Golden artifact identity not found.');
  await loadRawRecord('golden', naics, campaign.run_id, trigger);
}

async function openExcluded(naics, trigger) {
  const exclusion = state.campaign.exclusions.find(item => item.naics === naics);
  if (!exclusion) return;
  await loadRawRecord(exclusion.kind, naics, exclusion.run_id, trigger);
}

async function loadRawRecord(kind, naics, runId, trigger) {
  trigger.disabled = true;
  const recordBase = kind === 'golden' ? 'golden_v3_1_2' : 'runs';
  try {
    const [raw, review] = await Promise.all([
      getJson(`../pipeline/${recordBase}/${naics}/${runId}.json`),
      getJson(`../pipeline/review/${naics}/${runId}.json`)
    ]);
    openDrawer(normalizeRaw(raw, review), review, kind, trigger);
  } catch (error) {
    showToast(`Could not open artifact: ${error.message}`);
  } finally {
    trigger.disabled = false;
  }
}

function normalizeRaw(raw, review) {
  return {
    naics: raw.naics, title: raw.title,
    sector: {code: raw.naics.slice(0,2), name: raw.naics.startsWith('54') ? 'Professional Services' : 'Golden diagnostic'},
    scores: Object.fromEntries(Object.entries(raw.scores).map(([key,value]) => [key,value.score])),
    scoreArithmetic: Object.fromEntries(Object.entries(raw.scores).map(([key,value]) => [key,value.arithmetic])),
    S: raw.S, verdict: raw.decision.verdict, borderline: raw.decision.borderline, gate_blocked: raw.decision.gate_blocked,
    capped_by: raw.decision.capped_by, confidence: raw.confidence_overall,
    terminal_value: raw.cross_checks.terminal_value.class, heterogeneous: raw.heterogeneous, percentile: null,
    run_meta: raw.run_meta, acceptance: {status: review.outcome === 'reject' || review.outcome === 'invalid' ? 'rejected' : 'accepted', review},
    flags: [], evidence: {dataset_inputs: raw.dataset_inputs, inputs: raw.inputs, subfactors: {}, cross_checks: raw.cross_checks, top_uncertain_inputs: raw.top_uncertain_inputs, reviewer_note: raw.reviewer_note},
    research_memo: raw.narrative, sources: raw.sources, publication_caveats: review.publication_caveats || []
  };
}

function openDrawer(record, review, kind, trigger) {
  state.lastFocus = trigger;
  state.currentRecord = record; state.currentReview = review; state.currentKind = kind; state.currentTab = 'thesis';
  $('#drawer-content').innerHTML = drawerShell(record, review, kind);
  const drawer = $('#record-drawer');
  const backdrop = $('#drawer-backdrop');
  drawer.hidden = false; backdrop.hidden = false; document.body.classList.add('drawer-open');
  bindDrawerEvents();
  $('.drawer-close').focus();
}

function closeDrawer() {
  $('#record-drawer').hidden = true; $('#drawer-backdrop').hidden = true; document.body.classList.remove('drawer-open');
  state.lastFocus?.focus(); state.currentRecord = null;
}

function drawerShell(record, review, kind) {
  const factors = Object.keys(FACTORS).map(key => score(record.scores[key])).join(' × ');
  const badges = [
    `<span class="badge">${esc(kind)} record</span>`, `<span class="badge">${esc(record.confidence)} confidence</span>`,
    `<span class="badge review">${esc(review.outcome || review.review_meta?.outcome || 'reviewed').replaceAll('_',' ')}</span>`,
    record.borderline ? '<span class="badge">Borderline</span>' : '', record.heterogeneous ? '<span class="badge">Heterogeneous</span>' : ''
  ].join('');
  return `<header class="drawer-hero"><button class="drawer-close" aria-label="Close record">×</button>
    <div class="drawer-kicker">NAICS ${record.naics} · ${esc(record.sector.name)}</div><h2 id="drawer-title">${esc(record.title)}</h2><div class="drawer-badges">${badges}</div>
    <div class="score-ledger"><div class="big-score"><span>Absolute score</span><strong>${score(record.S)}</strong><small>${verdictLabel(record.verdict)}${record.percentile != null ? ` · ${ordinal(record.percentile)} percentile` : ''}</small></div>
    <div class="aggregate-equation">Geometric mean of five frozen factors<strong>(${factors})<sup>⅕</sup> = ${score(record.S)}</strong></div></div></header>
    <nav class="drawer-tabs" aria-label="Record details"><button class="drawer-tab active" data-tab="thesis">Thesis</button><button class="drawer-tab" data-tab="evidence">Score & evidence</button><button class="drawer-tab" data-tab="caveats">Caveats <span>${record.publication_caveats.length}</span></button><button class="drawer-tab" data-tab="artifacts">Artifacts</button></nav>
    <div id="drawer-panel" class="drawer-panel">${drawerPanel('thesis')}</div>`;
}

function bindDrawerEvents() {
  $('.drawer-close').addEventListener('click', closeDrawer);
  $$('.drawer-tab').forEach(button => button.addEventListener('click', () => {
    state.currentTab = button.dataset.tab;
    $$('.drawer-tab').forEach(tab => tab.classList.toggle('active', tab === button));
    $('#drawer-panel').innerHTML = drawerPanel(state.currentTab);
    bindPanelEvents();
  }));
  bindPanelEvents();
}

function bindPanelEvents() {
  $$('.factor-button').forEach(button => button.addEventListener('click', () => {
    const card = button.closest('.factor-card'); const open = card.classList.toggle('open'); button.setAttribute('aria-expanded',open);
  }));
  $$('.input-button').forEach(button => button.addEventListener('click', () => {
    const card = button.closest('.input-card'); const open = card.classList.toggle('open'); button.setAttribute('aria-expanded',open);
  }));
  $$('[data-source-jump]').forEach(button => button.addEventListener('click', event => {
    event.stopPropagation();
    const sourceId = button.dataset.sourceJump;
    let target = $(`#source-${CSS.escape(sourceId)}`);
    if (!target) {
      state.currentTab = 'evidence';
      $$('.drawer-tab').forEach(tab => tab.classList.toggle('active', tab.dataset.tab === 'evidence'));
      $('#drawer-panel').innerHTML = drawerPanel('evidence');
      bindPanelEvents();
      target = $(`#source-${CSS.escape(sourceId)}`);
    }
    target?.scrollIntoView({behavior:'smooth',block:'center'}); target?.classList.add('flash'); setTimeout(() => target?.classList.remove('flash'),1300);
  }));
}

function drawerPanel(tab) {
  if (tab === 'evidence') return evidencePanel(state.currentRecord);
  if (tab === 'caveats') return caveatPanel(state.currentRecord, state.currentReview);
  if (tab === 'artifacts') return artifactsPanel(state.currentRecord, state.currentKind);
  return thesisPanel(state.currentRecord);
}

function thesisPanel(record) {
  const memo = record.research_memo || {};
  const lead = memo.executive_view || 'Open the evidence view for the complete deterministic score chain.';
  const rest = Object.entries(memo).filter(([key]) => key !== 'executive_view');
  const uncertainty = record.evidence.top_uncertain_inputs || [];
  return `<h3>Research memo</h3><div class="thesis-lead">${withSourceRefs(lead)}</div>
    ${rest.map(([key,value]) => `<section class="memo-section"><span>${esc(MEMO_LABELS[key] || key.replaceAll('_',' '))}</span><p>${withSourceRefs(value)}</p></section>`).join('')}
    <h4>Highest-impact uncertainties</h4><div class="uncertainty-grid">${uncertainty.map(item => `<article class="uncertainty-card"><strong>${esc(INPUT_LABELS[item.input] || item.input)}</strong><span>${esc(item.plausible_range)}</span><p>${esc(item.score_impact)}</p></article>`).join('')}</div>`;
}

function withSourceRefs(text) {
  return esc(text).replace(/\[([A-Z]\d+)\]/g, (_, id) => `<button class="source-id-link" data-source-jump="${id}" title="Open Score & evidence to inspect ${id}">${id}</button>`);
}

function evidencePanel(record) {
  return `<h3>Verdict → factors → inputs → evidence</h3><div class="factor-chain">${Object.entries(FACTORS).map(([key,meta]) => factorCard(record,key,meta)).join('')}</div>
    <h4>Source registry</h4><div class="source-registry">${record.sources.map(sourceCard).join('')}</div>
    <h4>Cross-checks</h4><div class="input-details" style="display:block">${crossChecks(record.evidence.cross_checks)}</div>`;
}

function factorCard(record, key, meta) {
  const formula = formulaFor(record,key);
  const inputs = meta.inputs.map(name => inputCard(record,name)).join('');
  return `<article class="factor-card"><button class="factor-button" aria-expanded="false"><span class="factor-letter">${key}</span><span class="factor-name"><strong>${meta.name}</strong><small>${meta.short}</small></span><span class="factor-score">${score(record.scores[key])}</span><span class="factor-chevron">›</span></button><div class="factor-details"><div class="factor-formula">${esc(formula)}</div><div class="input-list">${inputs}</div></div></article>`;
}

function formulaFor(record,key) {
  if (record.scoreArithmetic?.[key]) return record.scoreArithmetic[key];
  const i = record.evidence.inputs, d = record.evidence.dataset_inputs, s = record.evidence.subfactors;
  if (key === 'V') return `V_raw = ${d.labor_share.value} × ${i.ai_replaceable_share.value} = ${s.V_raw}; V = 10 × min(1, V_raw ÷ 0.25) = ${record.scores.V}`;
  if (key === 'C') return `C = 10 × ${i.pi_dist.value} × ${i.pi_moat.value} = ${record.scores.C}`;
  if (key === 'A') return `A = 10 when t50 = 0, else min(10, 10 ÷ t50); t50 = ${i.t50_years.value}; A = ${record.scores.A}`;
  if (key === 'B') return `TD = ${s.TD}; OW = ${s.OW}; CFD = ${s.CFD}; B = 10 × √(TD × OW) ÷ (1 + 0.3 × CFD) = ${record.scores.B}`;
  return `M = clamp(4 × (exit − buy) ÷ buy, 0, 10) = ${record.scores.M}`;
}

function inputCard(record,name) {
  const dataset = ['labor_share','n_band'].includes(name);
  const input = dataset ? record.evidence.dataset_inputs[name] : record.evidence.inputs[name];
  if (!input) return '';
  const method = dataset ? 'DATASET' : (input.method || input.provenance_type || 'ESTIMATE');
  const value = displayInputValue(name,input.value);
  const quality = input.evidence_quality || input.quality || '—';
  const refs = dataset ? datasetSources(input) : (input.source_ids || []).map(id => `<button class="source-id-link" data-source-jump="${esc(id)}">${esc(id)}</button>`).join('') || 'No source ID · declared estimate';
  const details = (dataset ? datasetDetails(input) : input.rationale) || 'No additional rationale.';
  const caveats = (input.caveats || []).join(' ');
  return `<article class="input-card"><button class="input-button" aria-expanded="false"><span class="input-name"><strong>${esc(INPUT_LABELS[name] || name)}</strong><small>${esc(quality)} evidence${input.confidence ? ` · ${esc(input.confidence)} confidence` : ''}</small></span><span class="input-value">${esc(value)}</span><span class="method-pill method-${method.toLowerCase()}">${esc(method)}</span><span>›</span></button>
    <div class="input-details"><dl><dt>Rationale</dt><dd>${esc(details)}</dd><dt>Range</dt><dd>${esc(input.plausible_range || 'Not stated')}</dd><dt>Evidence</dt><dd>${refs}</dd>${caveats ? `<dt>Caveat</dt><dd>${esc(caveats)}</dd>` : ''}${name === 'owners_60plus_pct' ? successionDetail(input) : ''}</dl>${roleBreakdown(input)}</div></article>`;
}

function displayInputValue(name,value) {
  if (['labor_share','ai_replaceable_share','pi_dist','pi_moat','current_adoption_pct','owners_60plus_pct'].includes(name)) return pct(value);
  if (name === 't50_years') return `${Number(value).toFixed(1)} yrs`;
  if (['buy_mult','exit_mult'].includes(name)) return `${Number(value).toFixed(1)}×`;
  if (name === 'n_band' || name === 'active_consolidators') return Number(value).toLocaleString();
  return String(value).length > 54 ? `${String(value).slice(0,51)}…` : value;
}

function datasetSources(input) {
  const values = input.sources || (input.source ? [input.source] : []);
  return values.length ? values.map(source => sourceIsUrl(source) ? `<a href="${esc(source)}" target="_blank" rel="noopener">${esc(source)}</a>` : `<span>${esc(source)}</span>`).join('<br>') : 'Generated deterministic dataset input';
}

function datasetDetails(input) {
  return input.method || input.derivation || input.source || '';
}

function successionDetail(input) {
  const s = input.succession_shortage_documented;
  if (!s) return '';
  return `<dt>Succession flag</dt><dd>${s.value ? 'Documented' : 'Not documented'} · ${esc(s.method)} · ${esc(s.rationale)}</dd>`;
}

function roleBreakdown(input) {
  const roles = input.breakdown_by_role || [];
  if (!roles.length) return '';
  return `<div class="role-breakdown"><div class="role-breakdown-head"><strong>Role-weight calculation</strong><span class="method-pill method-estimate">ESTIMATE</span></div><div class="role-table-wrap"><table><thead><tr><th>Role</th><th>Labor</th><th>Auto.</th><th>Contribution</th></tr></thead><tbody>${roles.map(role => `<tr><td><strong>${esc(role.role)}</strong><small>${esc(role.soc)} · ${esc(role.rationale)}</small></td><td>${pct(role.labor_share_of_total)}</td><td>${pct(role.within_role_automatable_fraction)}</td><td>${pct(role.contribution)}</td></tr>`).join('')}</tbody></table></div></div>`;
}

function sourceCard(source) {
  const title = esc(source.title || source.id);
  const link = sourceIsUrl(source.url) ? `<a href="${esc(source.url)}" target="_blank" rel="noopener">${title} ↗</a>` : `<strong>${title}</strong>`;
  return `<article id="source-${esc(source.id)}" class="source-card"><div class="source-top"><span>${esc(source.id)}</span><time>${esc(source.access_date || '')}</time></div>${link}<p>${esc(source.what_it_supports || source.supports || '')}</p></article>`;
}

function crossChecks(checks = {}) {
  return `<dl>${Object.entries(checks).map(([key,value]) => `<dt>${esc(key.replaceAll('_',' '))}</dt><dd>${esc(formatCrossCheck(value))}</dd>`).join('')}</dl>`;
}

function formatCrossCheck(value) {
  if (value && typeof value === 'object' && value.class && value.justification) return `${value.class} — ${value.justification}`;
  if (typeof value === 'number') return Number(value).toFixed(2);
  return typeof value === 'object' ? JSON.stringify(value) : value;
}

function caveatPanel(record, review) {
  const caveats = record.publication_caveats || [];
  const findings = review.findings || [];
  const summary = review.summary || record.acceptance.review.summary || '';
  return `<h3>Publication caveats</h3><div class="caveat-summary"><strong>${caveats.length} visible caveats.</strong><br>${esc(summary)}</div>
    <ul class="caveat-list">${caveats.map(item => `<li>${esc(item)}</li>`).join('') || '<li>No publication caveats recorded.</li>'}</ul>
    ${findings.length ? `<h4>Validator findings</h4><div class="review-findings">${findings.map(f => `<article class="review-finding"><strong>${esc(f.severity)} · ${esc(f.category.replaceAll('_',' '))}</strong><p>${esc(f.explanation)}</p><p><b>Materiality:</b> ${esc(f.materiality)}</p></article>`).join('')}</div>` : ''}`;
}

function artifactsPanel(record, kind) {
  const id = record.run_meta.run_id, naics = record.naics;
  const runRoot = kind === 'golden' ? 'golden_v3_1_2' : 'runs';
  const artifacts = [
    ['PKT','Research packet',`../pipeline/packets/${naics}/${id}.json`,'Model-authored narrative, scorecard, and source registry'],
    ['REC',kind === 'golden' ? 'Golden score record' : 'Fleet score record',`../pipeline/${runRoot}/${naics}/${id}.json`,'Python-finalized inputs, factors, aggregate, and verdict'],
    ['MEM','Research memo',`../pipeline/memos/${naics}/${id}.md`,'Deterministically rendered human-facing memo'],
    ['REV','Publication review',`../pipeline/review/${naics}/${id}.json`,'Exact-artifact review, findings, support, and caveats']
  ];
  return `<h3>Underlying artifacts</h3><div class="artifact-list">${artifacts.map(([icon,label,url,description]) => `<a class="artifact-link" href="${url}"><span class="artifact-icon">${icon}</span><span><strong>${label}</strong><small>${esc(description)}<br>${esc(url)}</small></span><span>↗</span></a>`).join('')}</div>
    <table class="metadata-table"><tr><th>run id</th><td>${esc(id)}</td></tr>${Object.entries(record.run_meta).filter(([key]) => key !== 'run_id').map(([key,value]) => `<tr><th>${esc(key.replaceAll('_',' '))}</th><td>${esc(value)}</td></tr>`).join('')}</table>`;
}

init();
