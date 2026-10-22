const { chromium } = require('playwright-core');
const log = (k, v) => console.log(k.padEnd(48), JSON.stringify(v));
(async () => {
  const b = await chromium.launch({ executablePath: (process.env.CHROMIUM||'/opt/pw-browsers/chromium') });
  const errs = [];
  const p = await (await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true })).newPage();
  p.on('pageerror', e => errs.push(e.message));
  await p.route(/fonts\./, r => r.abort());
  await p.goto((process.env.APP_URL||'file://'+require('path').resolve(__dirname,'../../nc_medicaid_bh_dashboard.html')));
  log('tabs', await p.$$eval('#phase-tabs-container button', e => e.map(x => x.innerText.replace(/\s+/g, ' ').trim())));
  log('totals', [await p.textContent('#metric-steps-ratio'), await p.textContent('#metric-subtasks-total'), await p.textContent('#metric-span-weeks'), await p.textContent('#metric-cost-tally')]);
  await p.tap('#phase-tabs-container button:nth-child(6)');
  log('heading', await p.textContent('#phase-heading'));
  log('step cards', await p.$$eval('[id^=step-card-]', e => e.length));
  log('first step open (phone)', await p.$$eval('[id^=step-body-]:not(.hidden)', e => e.map(x => x.id)));
  await p.tap('#phase-tabs-container button:nth-child(5)');
  log('pager from phase 5 -> next label', await p.textContent('#phase-pager button:last-child'));
  await p.tap('#phase-pager button:last-child');
  await p.screenshot({ path: 'p6_phone.png' });
  // 8G-only filter still includes them (all three services)
  await p.evaluate(() => { document.getElementById('setup-panel').open = true; });
  await p.tap('text=Only 8G'); await p.tap('#apply-filter-btn');
  log('8G only: steps', await p.textContent('#metric-steps-ratio'));
  // check every phase-6 row has the Instructions button + generic note
  await p.evaluate(() => { switchPhaseTab(6); if (document.querySelectorAll('[id^=step-body-].hidden').length) toggleAllSteps(); });
  log('p6 rows / buttons', await p.evaluate(() => [document.querySelectorAll('#current-phase-container li').length, [...document.querySelectorAll('#current-phase-container li button')].filter(b => b.innerText.trim() === 'Instructions').length]));
  await p.tap('#current-phase-container li:first-child button');
  log('generic note shown', !(await p.$eval('#modal-generic-note', e => e.classList.contains('hidden'))));
  await p.keyboard.press('Escape');
  // print report includes the phase
  await p.evaluate(() => { printOptions = { scope: 'all', contacts: false }; preparePrint(); });
  log('print report phase 6 title', await p.evaluate(() => [...document.querySelectorAll('.pr-phase-title span')].map(e => e.textContent).filter(t => /Phase 6/.test(t))));
  log('print phase table rows', await p.$$eval('.pr-table tbody tr', e => e.length));
  await p.emulateMedia({ media: 'print' });
  await p.pdf({ path: 'plan_p6.pdf', preferCSSPageSize: true, printBackground: true });
  log('errors', errs);
  await b.close();
})();
