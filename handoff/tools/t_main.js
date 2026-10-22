const { chromium } = require('playwright-core');
const URL = (process.env.APP_URL||'file://'+require('path').resolve(__dirname,'../../nc_medicaid_bh_dashboard.html'));
const log = (k, v) => console.log(k.padEnd(46), JSON.stringify(v));
(async () => {
  const b = await chromium.launch({ executablePath: (process.env.CHROMIUM||'/opt/pw-browsers/chromium') });
  const errs = [];
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  p.on('pageerror', e => errs.push('pageerror: ' + e.message));
  p.on('console', m => { if (m.type() === 'error' && !/fonts|ERR_/.test(m.text())) errs.push('console: ' + m.text()); });
  p.on('dialog', d => d.accept());
  await p.route(/fonts\./, r => r.abort());
  await p.goto(URL);

  // --- step cards
  log('open steps on first phone visit', await p.$$eval('[id^=step-body-]:not(.hidden)', e => e.map(x => x.id)));
  await p.tap('#step-toggle-2');
  log('step 2 opened', await p.$eval('#step-toggle-2', e => e.getAttribute('aria-expanded')));
  log('expand-all label', await p.textContent('#expand-all-btn'));
  await p.tap('#expand-all-btn');
  log('after expand all: open', await p.$$eval('[id^=step-body-]:not(.hidden)', e => e.length));
  log('label now', await p.textContent('#expand-all-btn'));
  await p.tap('#expand-all-btn');
  log('after collapse all: open', await p.$$eval('[id^=step-body-]:not(.hidden)', e => e.length));

  // --- tap a checklist row (label) toggles; state survives re-render
  await p.tap('#step-toggle-1');
  const row = p.locator('[data-check-key="step_1_sub_0"]');
  await p.tap('#step-body-1 li:first-child label');
  log('row tap checked', await row.isChecked());
  log('progress text', await p.textContent('#metric-subtasks-count'));
  log('step 1 stays open after re-render', await p.$eval('#step-toggle-1', e => e.getAttribute('aria-expanded')));
  log('focus restored to checkbox', await p.evaluate(() => document.activeElement.dataset.checkKey));
  log('status badge', (await p.textContent('#step-toggle-1')).replace(/\s+/g, ' ').trim());

  // --- guide button + sheet
  await p.tap('#step-body-1 li:first-child button');
  log('sheet open', await p.isVisible('#subtask-detail-modal'));
  log('body scroll locked', await p.evaluate(() => document.body.classList.contains('modal-open')));
  const box = await p.$eval('#subtask-detail-modal > div', e => { const r = e.getBoundingClientRect(); return [Math.round(r.bottom), innerHeight, Math.round(r.width)]; });
  log('sheet bottom/viewport/width', box);
  log('toggle label (checked row)', await p.textContent('#modal-subtask-toggle-btn'));
  await p.tap('#modal-subtask-toggle-btn');
  log('row unchecked via sheet', !(await row.isChecked()));
  log('sheet closed', !(await p.isVisible('#subtask-detail-modal')));

  // --- next up
  await p.locator('[data-check-key="step_1_sub_0"]').check();
  for (let i = 1; i < 5; i++) await p.locator(`[data-check-key="step_1_sub_${i}"]`).check();
  log('next up after step 1 done', (await p.textContent('#next-up')).replace(/\s+/g, ' ').trim());
  await p.tap('#next-up button');
  await p.waitForTimeout(700);
  log('next-up opened step 2', await p.$eval('#step-toggle-2', e => e.getAttribute('aria-expanded')));

  // --- phase tabs / pager
  await p.tap('#phase-pager button:last-child');
  log('pager -> phase', await p.evaluate(() => appState.activePhase));
  log('tab strip scrolled so active visible', await p.evaluate(() => { const a = document.querySelector('#phase-tabs-container [aria-current=page]').getBoundingClientRect(); return a.left >= 0 && a.right <= innerWidth; }));
  log('heading', await p.textContent('#phase-heading'));

  // --- setup panel & filters
  await p.tap('#setup-panel > summary');
  log('setup open', await p.$eval('#setup-panel', e => e.open));
  await p.tap('#county-dropdown-trigger');
  await p.fill('#county-search-input', 'wake');
  await p.tap('.county-item-label:not(.hidden) input');
  log('setup summary (draft)', await p.textContent('#setup-summary'));
  await p.tap('#apply-filter-btn');
  log('setup auto-closed on phone', !(await p.$eval('#setup-panel', e => e.open)));
  log('regional panel auto-opened', await p.$eval('#regional-panel', e => e.open));
  log('badge', await p.textContent('#regions-active-count-badge'));
  log('tel links', await p.$$eval('#regional-contacts-grid a[href^="tel:"]', e => e.slice(0, 3).map(a => a.getAttribute('href') + ' | ' + a.textContent)));
  log('mailto links', await p.$$eval('#regional-contacts-grid a[href^="mailto:"]', e => e.length));
  await p.screenshot({ path: 'm_regional.png' });

  // --- timeline tap
  await p.tap('#schedule-panel > summary');
  await p.screenshot({ path: 'm_schedule.png', fullPage: false });
  await p.locator('#timeline-container button').nth(3).tap();
  await p.waitForTimeout(700);
  log('timeline row -> phase/open', await p.evaluate(() => [appState.activePhase, document.querySelector('[id^=step-toggle-4]')?.getAttribute('aria-expanded')]));

  // --- notes sheet
  await p.tap('#step-body-4 button:has-text("Add note")');
  log('notes textarea focused', await p.evaluate(() => document.activeElement.id));
  await p.fill('#modal-notes-textarea', 'Call city <b>planning</b>\nTicket #123');
  await p.tap('text=Save Notes');
  log('note chip in header', (await p.textContent('#step-toggle-4')).includes('Note'));

  // --- font sizes / inputs (iOS zoom)
  log('input font-size px', await p.$eval('#county-search-input', e => getComputedStyle(e).fontSize));
  log('smallest rendered text px', await p.evaluate(() => { let min = 99; document.querySelectorAll('body *').forEach(el => { if (el.children.length === 0 && el.textContent.trim() && el.offsetParent !== null && !el.closest('#print-report')) { min = Math.min(min, parseFloat(getComputedStyle(el).fontSize)); } }); return min; }));
  log('touch targets < 44px (visible buttons/links)', await p.evaluate(() => [...document.querySelectorAll('button, summary, label:has(input)')].filter(el => el.offsetParent !== null && !el.closest('#print-report') && !el.closest('.hidden')).map(el => { const r = el.getBoundingClientRect(); return [el.tagName, (el.innerText || el.getAttribute('aria-label') || '').trim().slice(0, 24), Math.round(r.width), Math.round(r.height)]; }).filter(([, , w, h]) => h < 44 || w < 44).slice(0, 12)));
  log('overflow-x', await p.evaluate(() => document.documentElement.scrollWidth > innerWidth));
  log('ERRORS', errs);
  await b.close();
})();
