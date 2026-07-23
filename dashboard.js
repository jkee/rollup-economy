'use strict';

const INDEX_URL = '6digit/fleet_index_v5_1.json';
const recordUrl = naics => '6digit/records/' + naics + '.json';
const PAGE_SIZE = 150;
const PAGE_STEP = 300;
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
const TIER_SHORT = {HIGHEST_PRIORITY: 'Highest', PRIORITY: 'Priority', CONDITIONAL: 'Conditional', LOW_PRIORITY: 'Low', STRUCTURAL_OUT: 'Out', UNKNOWN: 'No base'};
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
const state = {
  records: [], summary: null, query: '', tiers: new Set(), readiness: new Set(),
  sectors: new Set(), reviews: new Set(), crossing: false, heterogeneous: false,
  minScore: 0, sort: 'score-desc', visible: PAGE_SIZE, lastFocus: null, openRecord: null
};
const detailCache = new Map();

const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const esc = value => String(value ?? '').replace(/[&<>'"]/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[char]));
const label = value => String(value ?? 'UNKNOWN').toLowerCase().replaceAll('_', ' ').replace(/\b\w/g, char => char.toUpperCase());
const tierLabel = value => value === 'UNKNOWN' ? 'No Base Tier' : label(value);
const score = value => value == null ? '—' : Number(value).toFixed(2);
const number = value => value == null ? '—' : Number(value).toLocaleString(undefined, {maximumFractionDigits: 4});
const tierOf = record => record.tier || 'UNKNOWN';
const runBase = record => 'pipeline/v5_1/runs/' + record.naics + '/' + record.run_id;
const debounce = (fn, wait) => { let t; return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), wait); }; };
const groupSet = group => ({tier: state.tiers, readiness: state.readiness, sector: state.sectors, review: state.reviews}[group]);

async function init() {
  try {
    const response = await fetch(INDEX_URL);
    if (!response.ok) throw new Error(INDEX_URL + ' returned ' + response.status);
    const data = await response.json();
    state.records = data.records;
    state.summary = data.summary;
    renderMetrics();
    renderFilters();
    renderMethod();
    bindEvents();
    applyHash();
    $('#loading').hidden = true;
    const deepLink = parseHash().params.get('r');
    if (deepLink) openDrawerByNaics(deepLink, null);
  } catch (error) {
    $('#loading').hidden = true;
    $('#error').hidden = false;
    $('#error').innerHTML = '<strong>Dashboard data could not be loaded.</strong><br>' + esc(error.message) + '<br><small>Serve the repository root over HTTP.</small>';
  }
}

// ---------- URL state ----------

function parseHash() {
  const [view, qs] = location.hash.slice(1).split('?');
  return {view: view || 'fleet', params: new URLSearchParams(qs || '')};
}

function applyHash() {
  const {view, params} = parseHash();
  const csv = key => new Set((params.get(key) || '').split(',').filter(Boolean));
  state.query = params.get('q') || '';
  state.tiers = csv('tier');
  state.readiness = csv('rd');
  state.sectors = csv('sec');
  state.reviews = csv('rev');
  state.crossing = params.get('x') === '1';
  state.heterogeneous = params.get('het') === '1';
  state.minScore = Number(params.get('min')) || 0;
  state.sort = ['score-desc', 'score-asc', 'l-desc', 'order', 'naics'].includes(params.get('sort')) ? params.get('sort') : 'score-desc';
  state.visible = PAGE_SIZE;
  syncControls();
  setView(view);
  renderFleet();
}

function buildHash() {
  const params = new URLSearchParams();
  if (state.query) params.set('q', state.query);
  if (state.tiers.size) params.set('tier', [...state.tiers].join(','));
  if (state.readiness.size) params.set('rd', [...state.readiness].join(','));
  if (state.sectors.size) params.set('sec', [...state.sectors].join(','));
  if (state.reviews.size) params.set('rev', [...state.reviews].join(','));
  if (state.crossing) params.set('x', '1');
  if (state.heterogeneous) params.set('het', '1');
  if (state.minScore > 0) params.set('min', String(state.minScore));
  if (state.sort !== 'score-desc') params.set('sort', state.sort);
  if (state.openRecord) params.set('r', state.openRecord);
  const qs = params.toString();
  return '#' + ($('#methodology-view').hidden ? 'fleet' : 'methodology') + (qs ? '?' + qs : '');
}

function syncUrl(push = false) {
  const url = buildHash();
  if (location.hash === url) return;
  push ? history.pushState(null, '', url) : history.replaceState(null, '', url);
}

function syncControls() {
  $('#fleet-search').value = state.query;
  $('#fleet-sort').value = state.sort;
  $('#filter-borderline').checked = state.crossing;
  $('#filter-heterogeneous').checked = state.heterogeneous;
  $('#filter-min-score').value = state.minScore;
  $('#min-score-value').textContent = state.minScore > 0 ? 'A ≥ ' + Number(state.minScore).toFixed(1) : 'Off';
  $$('[data-filter-group]').forEach(input => { input.checked = groupSet(input.dataset.filterGroup).has(input.value); });
}

// ---------- filtering ----------

function passes(record, skip) {
  if (state.query && !((record.naics + ' ' + record.title + ' ' + record.search_text).toLowerCase().includes(state.query.toLowerCase()))) return false;
  if (skip !== 'tier' && state.tiers.size && !state.tiers.has(tierOf(record))) return false;
  if (skip !== 'readiness' && state.readiness.size && !state.readiness.has(record.readiness)) return false;
  if (skip !== 'sector' && state.sectors.size && !state.sectors.has(sectorOf(record))) return false;
  if (skip !== 'review' && state.reviews.size && !state.reviews.has(record.independent_review)) return false;
  if (skip !== 'crossing' && state.crossing && record.robust_tier) return false;
  if (skip !== 'heterogeneous' && state.heterogeneous && !record.heterogeneous) return false;
  if (skip !== 'min' && state.minScore > 0 && !(record.A != null && record.A >= state.minScore)) return false;
  return true;
}

function filteredRecords() {
  return state.records.filter(record => passes(record, null)).sort((left, right) => {
    if (state.sort === 'score-asc') return ((left.A ?? Infinity) - (right.A ?? Infinity)) || left.naics.localeCompare(right.naics);
    if (state.sort === 'l-desc') return ((right.L ?? -Infinity) - (left.L ?? -Infinity)) || left.naics.localeCompare(right.naics);
    if (state.sort === 'naics') return left.naics.localeCompare(right.naics);
    if (state.sort === 'order') return (left.order ?? Infinity) - (right.order ?? Infinity);
    return ((right.A ?? -Infinity) - (left.A ?? -Infinity)) || left.naics.localeCompare(right.naics);
  });
}

function facetCounts() {
  const facets = {tier: {}, readiness: {}, sector: {}, review: {}, crossing: 0, heterogeneous: 0};
  const bump = (group, key) => { facets[group][key] = (facets[group][key] || 0) + 1; };
  for (const record of state.records) {
    if (passes(record, 'tier')) bump('tier', tierOf(record));
    if (passes(record, 'readiness')) bump('readiness', record.readiness);
    if (passes(record, 'sector')) bump('sector', sectorOf(record));
    if (passes(record, 'review')) bump('review', record.independent_review);
    if (passes(record, 'crossing') && !record.robust_tier) facets.crossing++;
    if (passes(record, 'heterogeneous') && record.heterogeneous) facets.heterogeneous++;
  }
  return facets;
}

function activeFilterCount() {
  return state.tiers.size + state.readiness.size + state.sectors.size + state.reviews.size +
    (state.crossing ? 1 : 0) + (state.heterogeneous ? 1 : 0) + (state.minScore > 0 ? 1 : 0) + (state.query ? 1 : 0);
}

// ---------- rendering ----------

function renderMetrics() {
  const summary = state.summary;
  $('#campaign-total').textContent = summary.published.toLocaleString('en-US') + ' / ' + (summary.published + summary.excluded).toLocaleString('en-US');
  const metrics = [
    [summary.published.toLocaleString('en-US'), 'Published', summary.excluded + ' exclusions'],
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
  $('#verdict-filters').innerHTML = tierValues.map(value => check('tier', value, tierLabel(value))).join('');
  const readinessValues = [...new Set(state.records.map(record => record.readiness))].sort();
  $('#confidence-filters').innerHTML = readinessValues.map(value => check('readiness', value, label(value))).join('');
  $('#review-filters').innerHTML = [['accepted', 'Independently reviewed'], ['not_reviewed', 'Not reviewed']]
    .map(item => check('review', item[0], item[1])).join('');
  const sectorValues = [...new Set(state.records.map(sectorOf))].sort();
  $('#sector-filters').innerHTML = sectorValues.map(value => {
    const name = Object.values(SECTORS).find(sector => sector[0] === value);
    return check('sector', value, value + ' · ' + (name ? name[1] : 'Unknown'));
  }).join('');
}

function check(group, value, text) {
  return '<label class="check-row"><input type="checkbox" data-filter-group="' + group + '" value="' + esc(value) + '">' +
    '<span>' + esc(text) + '</span><small data-count-for="' + group + ':' + esc(value) + '">0</small></label>';
}

function updateRailCounts(facets) {
  $$('[data-count-for]').forEach(element => {
    const [group, value] = element.dataset.countFor.split(/:(.*)/);
    element.textContent = facets[group][value] || 0;
  });
  $('#borderline-count').textContent = facets.crossing;
  $('#heterogeneous-count').textContent = facets.heterogeneous;
}

function renderTierBar(counts) {
  const total = TIER_ORDER.reduce((sum, tier) => sum + (counts[tier] || 0), 0);
  $('#tier-bar').innerHTML = total === 0 ? '' : TIER_ORDER.map(tier => {
    const count = counts[tier] || 0;
    if (!count && !state.tiers.has(tier)) return '';
    const active = state.tiers.has(tier);
    return '<button type="button" class="tier-seg tier-' + tier.toLowerCase() + (active ? ' on' : '') + '"' +
      ' style="flex-grow:' + Math.max(count, total * 0.04) + '" data-tier="' + tier + '" aria-pressed="' + active + '"' +
      ' title="' + esc(tierLabel(tier)) + ' · ' + count + ' industries — click to filter">' +
      '<span>' + esc(TIER_SHORT[tier]) + '</span><b>' + count + '</b></button>';
  }).join('');
}

function renderChips() {
  const chips = [];
  if (state.query) chips.push(['query', '', '“' + state.query + '”']);
  state.tiers.forEach(value => chips.push(['tier', value, tierLabel(value)]));
  state.readiness.forEach(value => chips.push(['readiness', value, label(value)]));
  state.reviews.forEach(value => chips.push(['review', value, value === 'accepted' ? 'Reviewed' : 'Not reviewed']));
  state.sectors.forEach(value => chips.push(['sector', value, 'Sector ' + value]));
  if (state.crossing) chips.push(['crossing', '', 'Crossing interval']);
  if (state.heterogeneous) chips.push(['heterogeneous', '', 'Heterogeneous']);
  if (state.minScore > 0) chips.push(['min', '', 'A ≥ ' + Number(state.minScore).toFixed(1)]);
  $('#active-chips').hidden = chips.length === 0;
  $('#active-chips').innerHTML = chips.map(chip =>
    '<button type="button" class="chip" data-chip-group="' + chip[0] + '" data-chip-value="' + esc(chip[1]) + '"' +
    ' aria-label="Remove filter ' + esc(chip[2]) + '"><span>' + esc(chip[2]) + '</span><b>×</b></button>'
  ).join('') + (chips.length > 1 ? '<button type="button" class="chip chip-clear" data-chip-group="all">Clear all</button>' : '');
}

function removeFilter(group, value) {
  if (group === 'all') return resetFilters();
  if (group === 'query') { state.query = ''; }
  else if (group === 'crossing') { state.crossing = false; }
  else if (group === 'heterogeneous') { state.heterogeneous = false; }
  else if (group === 'min') { state.minScore = 0; }
  else groupSet(group).delete(value);
  syncControls();
  refresh();
}

function refresh() {
  state.visible = PAGE_SIZE;
  renderFleet();
  syncUrl();
}

function renderFleet() {
  const records = filteredRecords();
  const facets = facetCounts();
  $('#fleet-result-count').textContent = records.length.toLocaleString('en-US') + (records.length === 1 ? ' industry' : ' industries');
  $('#fleet-context').textContent = records.length === state.records.length
    ? 'v5.1 Stage 1 · provisional sampled validation · 178 / 1,012 independently reviewed'
    : 'Filtered from ' + state.records.length.toLocaleString('en-US') + ' records';
  renderTierBar(facets.tier);
  renderChips();
  updateRailCounts(facets);
  const shown = records.slice(0, state.visible);
  $('#fleet-list').innerHTML = shown.map(fleetRow).join('');
  $('#fleet-empty').hidden = records.length > 0;
  const remaining = records.length - shown.length;
  const more = $('#show-more');
  more.hidden = remaining <= 0;
  if (remaining > 0) more.textContent = 'Show ' + Math.min(PAGE_STEP, remaining) + ' more · ' + remaining + ' below';
  const active = activeFilterCount();
  $('#filter-toggle').textContent = active ? 'Filters · ' + active : 'Filters';
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
    record.heterogeneous ? '<span class="badge">Heterogeneous</span>' : ''
  ].join('');
  const sparks = Object.keys(FACTORS).map(factor => {
    const value = record.factor_bases[factor];
    return '<span class="spark-row"><b>' + factor + '</b><i class="spark-track"><i class="spark-fill" style="width:' + (value == null ? 0 : value * 10) + '%"></i></i><em>' + (value == null ? '—' : Number(value).toFixed(1)) + '</em></span>';
  }).join('');
  return '<button class="fleet-row" data-naics="' + record.naics + '" aria-label="Open ' + esc(record.title) + ' v5.1 evidence">' +
    '<span class="rank">' + String(index + 1).padStart(2, '0') + '</span>' +
    '<span class="industry"><span class="naics">' + record.naics + '<span class="sector-label"> · v5.1 ' + (reviewed ? 'reviewed' : 'not reviewed') + '</span></span><strong>' + esc(record.title) + '</strong><span class="badges">' + badges + '</span></span>' +
    '<span class="factor-spark">' + sparks + '</span>' +
    '<span class="result-score"><strong>' + score(record.A) + '</strong><span class="verdict-' + tier.toLowerCase() + '">' + esc(tierLabel(tier)) + '</span><small>L ' + score(record.L) + ' · ' + esc(TIER_SHORT[record.tier_interval[0]]) + ' → ' + esc(TIER_SHORT[record.tier_interval[1]]) + '</small></span>' +
    '<span class="row-arrow">→</span></button>';
}

function renderMethod() {
  const cuts = [['Highest priority', 'A ≥ 7.5 · L ≥ 6'], ['Priority', 'A ≥ 6 · L ≥ 4'], ['Conditional', 'A ≥ 4.5 · L ≥ 2'], ['Low priority', 'A ≥ 3 · L ≥ 1'], ['Structural out', 'otherwise']];
  $('#method-cuts').innerHTML = cuts.map(item => '<div class="cut-row"><span>' + item[0] + '</span><strong>' + item[1] + '</strong></div>').join('');
  $('#factor-glossary').innerHTML = Object.entries(FACTORS).map(item =>
    '<article class="glossary-item"><b>' + item[0] + '</b><strong>' + esc(item[1][0]) + '</strong><p>' + esc(item[1][1]) + '</p></article>'
  ).join('');
}

// ---------- events ----------

function bindEvents() {
  $$('.nav-button').forEach(button => button.addEventListener('click', () => {
    setView(button.dataset.view);
    syncUrl(true);
    scrollTo({top: 0, behavior: 'smooth'});
  }));
  $('#fleet-search').addEventListener('input', debounce(event => { state.query = event.target.value.trim(); refresh(); }, 120));
  $('#fleet-sort').addEventListener('change', event => { state.sort = event.target.value; refresh(); });
  $('#filter-borderline').addEventListener('change', event => { state.crossing = event.target.checked; refresh(); });
  $('#filter-heterogeneous').addEventListener('change', event => { state.heterogeneous = event.target.checked; refresh(); });
  $('#filter-min-score').addEventListener('input', event => {
    state.minScore = Number(event.target.value);
    $('#min-score-value').textContent = state.minScore > 0 ? 'A ≥ ' + state.minScore.toFixed(1) : 'Off';
    refresh();
  });
  $('.filter-rail').addEventListener('change', event => {
    const input = event.target.closest('[data-filter-group]');
    if (!input) return;
    input.checked ? groupSet(input.dataset.filterGroup).add(input.value) : groupSet(input.dataset.filterGroup).delete(input.value);
    refresh();
  });
  $('#tier-bar').addEventListener('click', event => {
    const segment = event.target.closest('[data-tier]');
    if (!segment) return;
    state.tiers.has(segment.dataset.tier) ? state.tiers.delete(segment.dataset.tier) : state.tiers.add(segment.dataset.tier);
    syncControls();
    refresh();
  });
  $('#active-chips').addEventListener('click', event => {
    const chip = event.target.closest('[data-chip-group]');
    if (chip) removeFilter(chip.dataset.chipGroup, chip.dataset.chipValue);
  });
  $('#show-more').addEventListener('click', () => { state.visible += PAGE_STEP; renderFleet(); });
  $('#filter-toggle').addEventListener('click', () => document.body.classList.toggle('filters-open'));
  $('#reset-filters').addEventListener('click', resetFilters);
  $('#fleet-list').addEventListener('click', event => {
    const row = event.target.closest('.fleet-row');
    if (row) openDrawerByNaics(row.dataset.naics, row);
  });
  $('#record-drawer').addEventListener('click', event => {
    if (event.target.closest('.drawer-close')) return closeDrawer();
    const link = event.target.closest('[data-source-id]');
    if (link) {
      const target = $('#source-' + link.dataset.sourceId, $('#record-drawer'));
      if (target) target.scrollIntoView({behavior: 'smooth', block: 'start'});
    }
  });
  $('#drawer-backdrop').addEventListener('click', () => closeDrawer());
  addEventListener('keydown', event => { if (event.key === 'Escape' && !$('#record-drawer').hidden) closeDrawer(); });
  addEventListener('popstate', () => {
    applyHash();
    const record = parseHash().params.get('r');
    if (record && state.openRecord !== record) openDrawerByNaics(record, null);
    else if (!record && state.openRecord) closeDrawer(true);
  });
}

function resetFilters() {
  state.query = '';
  state.tiers.clear();
  state.readiness.clear();
  state.sectors.clear();
  state.reviews.clear();
  state.crossing = false;
  state.heterogeneous = false;
  state.minScore = 0;
  syncControls();
  refresh();
}

function setView(view) {
  if (!['fleet', 'methodology'].includes(view)) view = 'fleet';
  $$('.view').forEach(section => { section.hidden = section.id !== view + '-view'; });
  $$('.nav-button').forEach(button => {
    const active = button.dataset.view === view;
    button.classList.toggle('active', active);
    active ? button.setAttribute('aria-current', 'page') : button.removeAttribute('aria-current');
  });
}

// ---------- record drawer (lazy detail) ----------

function fetchRecord(naics) {
  if (!detailCache.has(naics)) {
    detailCache.set(naics, fetch(recordUrl(naics)).then(response => {
      if (!response.ok) throw new Error(recordUrl(naics) + ' returned ' + response.status);
      return response.json();
    }).catch(error => { detailCache.delete(naics); throw error; }));
  }
  return detailCache.get(naics);
}

async function openDrawerByNaics(naics, trigger) {
  if (!state.records.some(record => record.naics === naics)) return;
  state.lastFocus = trigger;
  state.openRecord = naics;
  $('#drawer-content').innerHTML = '<header class="drawer-hero"><button class="drawer-close" aria-label="Close record">×</button>' +
    '<div class="drawer-kicker">NAICS ' + esc(naics) + '</div><div class="drawer-loading">Loading the evidence record…</div></header>';
  $('#record-drawer').hidden = false;
  $('#record-drawer').scrollTop = 0;
  $('#drawer-backdrop').hidden = false;
  document.body.classList.add('drawer-open');
  $('.drawer-close').focus();
  syncUrl();
  try {
    const record = await fetchRecord(naics);
    if (state.openRecord !== naics) return;
    $('#drawer-content').innerHTML = drawerContent(record);
    $('.drawer-close').focus();
  } catch (error) {
    if (state.openRecord !== naics) return;
    $('#drawer-content').innerHTML = '<header class="drawer-hero"><button class="drawer-close" aria-label="Close record">×</button>' +
      '<div class="drawer-kicker">NAICS ' + esc(naics) + '</div><h2>Record could not be loaded</h2>' +
      '<p class="drawer-loading">' + esc(error.message) + '</p></header>';
  }
}

function closeDrawer(skipUrl = false) {
  state.openRecord = null;
  $('#record-drawer').hidden = true;
  $('#drawer-backdrop').hidden = true;
  document.body.classList.remove('drawer-open');
  if (!skipUrl) syncUrl();
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
