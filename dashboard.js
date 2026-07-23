'use strict';

const DATA_URL = '6digit/six_data_v5_1.json';
const FACTORS = {
  H: ['Implementable labor opportunity', 'Current compensation exposed to implementable AI task substitution'],
  F: ['Transferable-firm opportunity', 'Expected lens-eligible LMM control transfers over five years'],
  C: ['Commercial retention', 'Share of implemented gross benefit retained commercially'],
  D: ['Operator-required demand', 'Year-five constant-price service quantity still needing an operator']
};
const FORMULAS = {
  H: '10 × min(1, l × a × rho / 0.25)',
  F: '10 × clamp(log10(1 + n × e × s5) / log10(501), 0, 1)',
  C: '10 × min(1, q / 0.50)',
  D: '10 × clamp(d5 × o, 0, 1)'
};
const PRIMITIVES = {
  a: 'Task exposure', rho: 'Five-year implementation', e: 'Eligible firm share',
  s5: 'Five-year transfer rate', q: 'Commercial retention', d5: 'Service demand',
  o: 'Operator-required share', l: 'Labor compensation share', n: 'Eligible firm count'
};
const TIER_ORDER = ['HIGHEST_PRIORITY', 'PRIORITY', 'CONDITIONAL', 'LOW_PRIORITY', 'STRUCTURAL_OUT', 'UNKNOWN'];
const SECTORS = {
  '11': ['11', 'Agriculture, Forestry, Fishing'], '21': ['21', 'Mining, Oil and Gas'],
  '22': ['22', 'Utilities'], '23': ['23', 'Construction'],
  '31': ['31-33', 'Manufacturing'], '32': ['31-33', 'Manufacturing'], '33': ['31-33', 'Manufacturing'],
  '42': ['42', 'Wholesale Trade'], '44': ['44-45', 'Retail Trade'], '45': ['44-45', 'Retail Trade'],
  '48': ['48-49', 'Transportation and Warehousing'], '49': ['48-49', 'Transportation and Warehousing'],
  '51': ['51', 'Information'], '52': ['52', 'Finance and Insurance'],
  '53': ['53', 'Real Estate and Rental'], '54': ['54', 'Professional and Technical Services'],
  '55': ['55', 'Management of Companies'], '56': ['56', 'Administrative and Waste Services'],
  '61': ['61', 'Educational Services'], '62': ['62', 'Health Care and Social Assistance'],
  '71': ['71', 'Arts, Entertainment, Recreation'], '72': ['72', 'Accommodation and Food'],
  '81': ['81', 'Other Services'], '92': ['92', 'Public Administration']
};
const sectorOf = record => (SECTORS[record.naics.slice(0, 2)] || ['??', 'Unknown'])[0];
const state = {records: [], summary: null, query: '', tiers: new Set(), readiness: new Set(), sectors: new Set(), crossing: false, heterogeneous: false, sort: 'score-desc', lastFocus: null};

const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const esc = value => String(value ?? '').replace(/[&<>'"]/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[char]));
const label = value => String(value ?? 'UNKNOWN').toLowerCase().replaceAll('_', ' ').replace(/\b\w/g, char => char.toUpperCase());
const tierLabel = value => value === 'UNKNOWN' ? 'No Base Tier' : label(value);
const score = value => value == null ? '—' : Number(value).toFixed(2);
const number = value => value == null ? '—' : Number(value).toLocaleString(undefined, {maximumFractionDigits: 4});
const tierOf = record => record.tier || 'UNKNOWN';
const runBase = record => 'pipeline/v5_1/runs/' + record.naics + '/' + record.run_id;

async function init() {
  try {
    const response = await fetch(DATA_URL);
    if (!response.ok) throw new Error(DATA_URL + ' returned ' + response.status);
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
    $('#error').innerHTML = '<strong>Dashboard data could not be loaded.</strong><br>' + esc(error.message) + '<br><small>Serve the repository root over HTTP.</small>';
  }
}

function renderAll() {
  renderMetrics();
  renderFilters();
  renderFleet();
  renderMethod();
}

function renderMetrics() {
  const summary = state.summary;
  $('#campaign-total').textContent = summary.published + ' / ' + (summary.published + summary.excluded);
  const metrics = [
    [summary.published, 'Published', summary.excluded + ' exclusions'],
    [summary.independent_review.accepted, 'Independently reviewed', summary.independent_review.not_reviewed + ' labeled not reviewed'],
    [summary.tiers.HIGHEST_PRIORITY || 0, 'Highest priority', 'research priority, not buy signal'],
    [summary.tiers.PRIORITY || 0, 'Priority', (summary.tiers.CONDITIONAL || 0) + ' conditional'],
    [summary.readiness.MODEL_CONDITIONED || 0, 'Model-conditioned', (summary.readiness.STRESS_TEST_ONLY || 0) + ' evidence-first']
  ];
  $('#campaign-metrics').innerHTML = metrics.map(item =>
    '<div class="metric"><strong>' + esc(item[0]) + '</strong><span>' + esc(item[1]) + '</span><small>' + esc(item[2]) + '</small></div>'
  ).join('');
}

function renderFilters() {
  const tierValues = TIER_ORDER.filter(tier => state.records.some(record => tierOf(record) === tier));
  $('#verdict-filters').innerHTML = tierValues.map(value =>
    check('tier', value, tierLabel(value), state.records.filter(record => tierOf(record) === value).length)
  ).join('');
  const readinessValues = [...new Set(state.records.map(record => record.readiness))].sort();
  $('#confidence-filters').innerHTML = readinessValues.map(value =>
    check('readiness', value, label(value), state.records.filter(record => record.readiness === value).length)
  ).join('');
  const sectorValues = [...new Set(state.records.map(sectorOf))].sort();
  $('#sector-filters').innerHTML = sectorValues.map(value => {
    const name = Object.values(SECTORS).find(sector => sector[0] === value);
    return check('sector', value, value + ' · ' + (name ? name[1] : 'Unknown'), state.records.filter(record => sectorOf(record) === value).length);
  }).join('');
  $('#borderline-count').textContent = state.records.filter(record => !record.robust_tier).length;
  $('#heterogeneous-count').textContent = state.records.filter(record => record.lens && record.lens.heterogeneous).length;
}

function check(group, value, text, count) {
  return '<label class="check-row"><input type="checkbox" data-filter-group="' + group + '" value="' + esc(value) + '"><span>' + esc(text) + '</span><small>' + count + '</small></label>';
}

function filteredRecords() {
  const query = state.query.toLowerCase();
  return state.records.filter(record => {
    const lensText = ((record.lens && record.lens.included_activities) || '') + ' ' + ((record.lens && record.lens.customer_and_revenue_model) || '');
    if (query && !(record.naics + ' ' + record.title + ' ' + lensText).toLowerCase().includes(query)) return false;
    if (state.tiers.size && !state.tiers.has(tierOf(record))) return false;
    if (state.readiness.size && !state.readiness.has(record.readiness)) return false;
    if (state.sectors.size && !state.sectors.has(sectorOf(record))) return false;
    if (state.crossing && record.robust_tier) return false;
    if (state.heterogeneous && !(record.lens && record.lens.heterogeneous)) return false;
    return true;
  }).sort((left, right) => {
    if (state.sort === 'score-asc') return ((left.A ?? Infinity) - (right.A ?? Infinity)) || left.naics.localeCompare(right.naics);
    if (state.sort === 'naics') return left.naics.localeCompare(right.naics);
    if (state.sort === 'order') return (left.order ?? Infinity) - (right.order ?? Infinity);
    return ((right.A ?? -Infinity) - (left.A ?? -Infinity)) || left.naics.localeCompare(right.naics);
  });
}

function renderFleet() {
  const records = filteredRecords();
  $('#fleet-result-count').textContent = records.length + (records.length === 1 ? ' industry' : ' industries');
  $('#fleet-context').textContent = records.length === state.records.length ? 'v5.1 Stage 1 · provisional sampled validation · 178 / 1,012 independently reviewed' : 'Filtered from ' + state.records.length + ' records';
  $('#fleet-empty').hidden = records.length > 0;
  $('#fleet-list').innerHTML = records.map((record, index) => fleetRow(record, index)).join('');
  $$('.fleet-row').forEach(button => button.addEventListener('click', () => {
    openDrawer(state.records.find(record => record.naics === button.dataset.naics), button);
  }));
}

function fleetRow(record, index) {
  const tier = tierOf(record);
  const crossing = !record.robust_tier;
  const reviewed = record.independent_review === 'accepted';
  const badges = [
    '<span class="badge conf-low">' + esc(label(record.readiness)) + '</span>',
    '<span class="badge caveat">' + esc(label(record.action)) + '</span>',
    '<span class="badge review">' + (reviewed ? 'Independently reviewed' : 'Not independently reviewed') + '</span>',
    crossing ? '<span class="badge borderline">Crossing interval</span>' : '<span class="badge">Stable tier</span>',
    record.lens && record.lens.heterogeneous ? '<span class="badge">Heterogeneous</span>' : ''
  ].join('');
  const sparks = Object.keys(FACTORS).map(factor => {
    const value = record.factors[factor].base;
    return '<span class="spark-row"><b>' + factor + '</b><i class="spark-track"><i class="spark-fill" style="width:' + (value == null ? 0 : value * 10) + '%"></i></i><em>' + (value == null ? '—' : Number(value).toFixed(1)) + '</em></span>';
  }).join('');
  return '<button class="fleet-row" data-naics="' + record.naics + '" aria-label="Open ' + esc(record.title) + ' v5.1 evidence">' +
    '<span class="rank">' + String(index + 1).padStart(2, '0') + '</span>' +
    '<span class="industry"><span class="naics">' + record.naics + '<span class="sector-label"> · v5.1 ' + (reviewed ? 'reviewed' : 'not reviewed') + '</span></span><strong>' + esc(record.title) + '</strong><span class="badges">' + badges + '</span></span>' +
    '<span class="factor-spark">' + sparks + '</span>' +
    '<span class="result-score"><strong>' + score(record.A) + '</strong><span class="verdict-' + tier.toLowerCase() + '">' + esc(tierLabel(tier)) + '</span><small>Interval ' + esc(label(record.tier_interval[0])) + ' → ' + esc(label(record.tier_interval[1])) + '</small></span>' +
    '<span class="row-arrow">→</span></button>';
}

function renderMethod() {
  const cuts = [['Highest priority', 'A ≥ 7.5 · L ≥ 6'], ['Priority', 'A ≥ 6 · L ≥ 4'], ['Conditional', 'A ≥ 4.5 · L ≥ 2'], ['Low priority', 'A ≥ 3 · L ≥ 1'], ['Structural out', 'otherwise']];
  $('#method-cuts').innerHTML = cuts.map(item => '<div class="cut-row"><span>' + item[0] + '</span><strong>' + item[1] + '</strong></div>').join('');
  $('#factor-glossary').innerHTML = Object.entries(FACTORS).map(item =>
    '<article class="glossary-item"><b>' + item[0] + '</b><strong>' + esc(item[1][0]) + '</strong><p>' + esc(item[1][1]) + '</p></article>'
  ).join('');
}

function bindEvents() {
  $$('.nav-button').forEach(button => button.addEventListener('click', () => switchView(button.dataset.view)));
  $('#fleet-search').addEventListener('input', event => { state.query = event.target.value.trim(); renderFleet(); });
  $('#fleet-sort').addEventListener('change', event => { state.sort = event.target.value; renderFleet(); });
  $('#filter-borderline').addEventListener('change', event => { state.crossing = event.target.checked; renderFleet(); });
  $('#filter-heterogeneous').addEventListener('change', event => { state.heterogeneous = event.target.checked; renderFleet(); });
  $$('[data-filter-group]').forEach(input => input.addEventListener('change', event => {
    const target = {tier: state.tiers, readiness: state.readiness, sector: state.sectors}[event.target.dataset.filterGroup];
    event.target.checked ? target.add(event.target.value) : target.delete(event.target.value);
    renderFleet();
  }));
  $('#reset-filters').addEventListener('click', resetFilters);
  $('#drawer-backdrop').addEventListener('click', closeDrawer);
  addEventListener('keydown', event => { if (event.key === 'Escape' && !$('#record-drawer').hidden) closeDrawer(); });
  addEventListener('popstate', () => switchView(location.hash.slice(1) || 'fleet', false));
}

function resetFilters() {
  state.query = '';
  state.tiers.clear();
  state.readiness.clear();
  state.sectors.clear();
  state.crossing = false;
  state.heterogeneous = false;
  $('#fleet-search').value = '';
  $('#filter-borderline').checked = false;
  $('#filter-heterogeneous').checked = false;
  $$('[data-filter-group]').forEach(input => { input.checked = false; });
  renderFleet();
}

function switchView(view, push = true) {
  if (!['fleet', 'methodology'].includes(view)) view = 'fleet';
  $$('.view').forEach(section => { section.hidden = section.id !== view + '-view'; });
  $$('.nav-button').forEach(button => {
    const active = button.dataset.view === view;
    button.classList.toggle('active', active);
    active ? button.setAttribute('aria-current', 'page') : button.removeAttribute('aria-current');
  });
  if (push && location.hash !== '#' + view) history.pushState(null, '', '#' + view);
  scrollTo({top: 0, behavior: 'smooth'});
}

function openDrawer(record, trigger) {
  state.lastFocus = trigger;
  $('#drawer-content').innerHTML = drawerContent(record);
  $('#record-drawer').hidden = false;
  $('#drawer-backdrop').hidden = false;
  document.body.classList.add('drawer-open');
  $('.drawer-close').addEventListener('click', closeDrawer);
  $$('[data-source-id]', $('#record-drawer')).forEach(button => button.addEventListener('click', () => {
    const target = $('#source-' + button.dataset.sourceId, $('#record-drawer'));
    if (target) target.scrollIntoView({behavior: 'smooth', block: 'start'});
  }));
  $('.drawer-close').focus();
}

function closeDrawer() {
  $('#record-drawer').hidden = true;
  $('#drawer-backdrop').hidden = true;
  document.body.classList.remove('drawer-open');
  if (state.lastFocus) state.lastFocus.focus();
}

function drawerContent(record) {
  const tier = tierOf(record);
  const reviewed = record.independent_review === 'accepted' && record.review;
  const factors = Object.entries(FACTORS).map(item => factorCard(record, item[0], item[1][0], item[1][1])).join('');
  const primitives = Object.keys(PRIMITIVES).filter(key => record.primitives[key]).map(key => primitiveCard(key, record.primitives[key])).join('');
  const reviewCaveats = reviewed ? list(record.review.caveats, 'No validator caveats recorded.') : '<p class="empty-inline">Not selected for independent review under the frozen sampling contract.</p>';
  const findings = reviewed ? list(record.review.material_findings, 'No material findings.') : '<p class="empty-inline">No independent-review finding exists for this unsampled record.</p>';
  const reviewLabel = reviewed ? label(record.review.outcome) : 'Not Independently Reviewed';
  const run = runBase(record);
  return '<header class="drawer-hero"><button class="drawer-close" aria-label="Close record">×</button>' +
    '<div class="drawer-kicker">NAICS ' + record.naics + ' · v5.1 provisional sampled-validation research</div><h2 id="drawer-title">' + esc(record.title) + '</h2>' +
    '<div class="drawer-badges"><span class="badge">' + esc(label(record.readiness)) + '</span><span class="badge review">' + esc(label(record.action)) + '</span><span class="badge">' + esc(reviewLabel) + '</span>' + (record.robust_tier ? '<span class="badge">Stable tier</span>' : '<span class="badge borderline">Crossing interval</span>') + '</div>' +
    '<div class="score-ledger"><div class="big-score"><span>Breadth score A</span><strong>' + score(record.A) + '</strong><small>' + esc(tierLabel(tier)) + '</small></div>' +
    '<div class="aggregate-equation">A = mean(H,F,C,D) · L = weakest factor<strong>L ' + score(record.L) + ' · ' + esc(label(record.tier_interval[0])) + ' → ' + esc(label(record.tier_interval[1])) + '</strong></div></div></header>' +
    '<div class="drawer-panel">' +
      '<a class="memo-primary" href="' + esc(record.memo) + '"><span>Read the research memo</span><strong>Primary explanation ↗</strong></a>' +
      '<h3>Decision summary</h3><div class="decision-grid"><article><span>Principal driver</span><p>' + esc(record.principal_driver) + '</p></article><article><span>Principal weakness</span><p>' + esc(record.principal_weakness) + '</p></article></div>' +
      lensCard(record.lens) +
      '<h3>Factor chain</h3><div class="factor-chain">' + factors + '</div>' +
      '<h3>Primitive evidence</h3><div class="primitive-grid">' + primitives + '</div>' +
      '<h3>Validator review</h3><div class="review-summary"><strong>' + esc(reviewLabel) + '</strong><span>' + (reviewed ? record.review.material_findings.length + ' material findings · ' + record.review.caveats.length + ' caveats' : 'Published as not_reviewed by the frozen sampling contract') + '</span></div>' +
      '<h4>Material findings</h4>' + findings + '<h4>Review caveats</h4>' + reviewCaveats +
      '<h3>Cited sources</h3><div class="source-registry">' + record.sources.map(source => sourceCard(source, reviewed ? record.review.sources_audited : [], reviewed)).join('') + '</div>' +
      '<h3>Artifacts</h3><div class="artifact-list">' +
        artifact(run + '/packet.json', 'PACKET', 'Research packet', record.run_id) +
        artifact(run + '/score.json', 'SCORE', 'Deterministic score', 'Reproducible v5.1 mechanics') +
        (reviewed ? artifact(run + '/review.json', 'REVIEW', 'Isolated validator review', record.review.artifacts_sha256) : '') +
        artifact('pipeline/v5_1/methodology.md', 'METHOD', 'Frozen v5.1 methodology', record.run_meta.methodology_commit) +
      '</div><table class="metadata-table"><tr><th>Run</th><td>' + esc(record.run_id) + '</td></tr><tr><th>Research model</th><td>' + esc(record.run_meta.model_id) + '</td></tr><tr><th>Attempt</th><td>' + esc(record.run_meta.attempt) + '</td></tr><tr><th>Methodology</th><td>' + esc(record.run_meta.methodology_version) + '</td></tr></table></div>';
}

function lensCard(lens) {
  return '<article class="lens-card"><strong>Decision lens</strong><dl>' +
    '<dt>Included</dt><dd>' + esc(lens.included_activities) + '</dd>' +
    '<dt>Excluded</dt><dd>' + esc(lens.excluded_activities) + '</dd>' +
    '<dt>Customer / revenue</dt><dd>' + esc(lens.customer_and_revenue_model) + '</dd>' +
    '<dt>Heterogeneous</dt><dd>' + (lens.heterogeneous ? 'Yes' : 'No') + '</dd></dl></article>';
}

function factorCard(record, key, name, short) {
  const factor = record.factors[key];
  const anchors = key === 'H' ? ['l', 'a', 'rho'] : key === 'F' ? ['n', 'e', 's5'] : factor.primitives;
  return '<article class="factor-card"><div class="factor-button"><span class="factor-letter">' + key + '</span><span class="factor-name"><strong>' + esc(name) + '</strong><small>' + esc(short) + '</small></span><span class="factor-score">' + score(factor.base) + '</span></div>' +
    '<div class="factor-details" style="display:block"><div class="factor-formula">' + esc(FORMULAS[key]) + '<br>Range ' + score(factor.low) + '–' + score(factor.high) + ' · ' + esc(label(factor.evidence_state)) + ' · primitives ' + anchors.map(esc).join(', ') + '</div></div></article>';
}

function primitiveCard(key, primitive) {
  const value = primitive.base ?? primitive.value;
  const range = primitive.low == null && primitive.high == null ? '' : '<span>Range ' + number(primitive.low) + '–' + number(primitive.high) + '</span>';
  const sources = (primitive.source_ids || []).map(id => '<button class="source-id-link" type="button" data-source-id="' + esc(id) + '">' + esc(id) + '</button>').join('');
  const caveats = list(primitive.caveats || [], 'No packet caveats recorded.');
  return '<article class="primitive-card"><div class="primitive-head"><span><b>' + esc(key) + '</b><strong>' + esc(PRIMITIVES[key]) + '</strong></span><em>' + number(value) + '</em></div>' +
    '<div class="primitive-meta"><span>' + esc(label(primitive.evidence_state)) + (primitive.quality ? ' · ' + esc(label(primitive.quality)) : '') + '</span>' + range + '</div>' +
    (primitive.rationale ? '<h4>Rationale</h4><p>' + esc(primitive.rationale) + '</p>' : '') +
    (primitive.bridge ? '<h4>Bridge</h4><p>' + esc(primitive.bridge) + '</p>' : '') +
    (primitive.detail ? '<h4>Dataset provenance</h4><p>' + esc(primitive.detail) + '</p>' : '') +
    (sources ? '<div class="primitive-sources"><strong>Sources</strong>' + sources + '</div>' : '') +
    '<h4>Caveats</h4>' + caveats +
    (primitive.change_evidence ? '<div class="change-evidence"><strong>Evidence that would change this</strong><p>' + esc(primitive.change_evidence) + '</p></div>' : '') + '</article>';
}

function list(items, empty) {
  if (!items.length) return '<p class="empty-inline">' + esc(empty) + '</p>';
  return '<ul class="caveat-list">' + items.map(item => {
    const text = typeof item === 'string' ? item : (item.summary || item.finding || JSON.stringify(item));
    return '<li>' + esc(text) + '</li>';
  }).join('') + '</ul>';
}

function sourceCard(source, audits, reviewed) {
  const audit = audits.find(item => item.source_id === source.id);
  const auditLabel = audit ? label(audit.support) : (reviewed ? 'Audit Missing' : 'Not Independently Reviewed');
  return '<article class="source-card" id="source-' + esc(source.id) + '"><div class="source-top"><span>' + esc(source.id) + '</span><time>' + esc(source.access_date) + '</time></div><a href="' + esc(source.url) + '" target="_blank" rel="noopener">' + esc(source.title) + ' ↗</a>' +
    '<div class="author-support"><strong>Packet claim</strong><p>' + esc(source.supports) + '</p></div>' +
    '<div class="source-audit audit-' + esc(audit ? audit.support : 'missing') + '"><strong>Validator audit · ' + esc(auditLabel) + (audit ? (audit.reachable ? ' · reachable' : ' · unreachable') : '') + '</strong><p>' + esc(audit ? audit.note : (reviewed ? 'No source audit was published.' : 'This unsampled record has no independent source audit.')) + '</p></div></article>';
}

function artifact(href, icon, title, detail) {
  return '<a class="artifact-link" href="' + esc(href) + '"><span class="artifact-icon">' + esc(icon) + '</span><span><strong>' + esc(title) + '</strong><small>' + esc(detail) + '</small></span><span>↗</span></a>';
}

init();
