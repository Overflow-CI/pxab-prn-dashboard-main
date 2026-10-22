const { chromium } = require('playwright-core');
const fs = require('fs');
const log = (k, v) => console.log(k.padEnd(46), JSON.stringify(v));
(async () => {
  const b = await chromium.launch({ executablePath: (process.env.CHROMIUM||'/opt/pw-browsers/chromium') });
  const p = await (await b.newContext({ viewport: { width: 1280, height: 900 } })).newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  p.on('dialog', d => d.accept());
  await p.route(/fonts\./, r => r.abort());
  await p.goto((process.env.APP_URL||'file://'+require('path').resolve(__dirname,'../../nc_medicaid_bh_dashboard.html')));

  log('desktop: steps open in phase 1', await p.$$eval('[id^=step-body-]:not(.hidden)', e => e.length));
  log('desktop first run: panels open (setup only)', await p.$$eval('.panel', e => e.map(x => x.open)));
  // county dropdown regressions
  await p.click('#county-dropdown-trigger');
  await p.click('[data-region="1"] button');
  log('menu stays open after Toggle Region', await p.isVisible('#county-dropdown-menu'));
  await p.fill('#county-search-input', 'wake');
  log('visible groups for "wake"', await p.$$eval('.county-region-group:not(.hidden)', e => e.map(x => x.dataset.region)));
  await p.click('[data-region="4"] button');
  log('search kept after toggle', await p.$$eval('.county-item-label:not(.hidden)', e => e.length));
  await p.click('#apply-filter-btn');
  log('desktop: setup stays open after apply', await p.$eval('#setup-panel', e => e.open));
  log('region cards', await p.$$eval('#regional-contacts-grid > div', e => e.length));
  // 8G only filter -> metrics
  await p.click('text=Only 8G'); await p.click('#apply-filter-btn');
  log('8G: steps shown / fees / span', [await p.$$eval('[id^=step-card-]', e => e.length), await p.textContent('#metric-cost-tally'), await p.textContent('#metric-span-weeks')]);
  log('8G: schedule summary', await p.textContent('#schedule-summary'));
  await p.click('text=Select All'); await p.click('#apply-filter-btn');
  // modal keyboard behavior
  await p.click('#step-body-1 li:first-child button');
  await p.keyboard.press('Tab'); await p.keyboard.press('Tab'); await p.keyboard.press('Tab'); await p.keyboard.press('Tab');
  log('focus stays inside dialog after 4 Tabs', await p.evaluate(() => !!document.activeElement.closest('#subtask-detail-modal')));
  await p.keyboard.press('Escape');
  log('Escape closes + focus back on Guide button', [!(await p.isVisible('#subtask-detail-modal')), await p.evaluate(() => document.activeElement.textContent.trim())]);
  await p.click('button:has-text("Print")'); await p.keyboard.press('Escape');
  log('Escape closes print modal', !(await p.isVisible('#print-modal')));
  await p.click('button:has-text("Print")'); await p.mouse.click(5, 5);
  log('backdrop click closes print modal', !(await p.isVisible('#print-modal')));
  // keyboard: space on a row toggles
  await p.focus('[data-check-key="step_2_sub_0"]'); await p.keyboard.press('Space');
  log('space toggles checkbox, focus kept', [await p.isChecked('[data-check-key="step_2_sub_0"]'), await p.evaluate(() => document.activeElement.dataset.checkKey)]);
  // notes escaped
  await p.click('#step-body-1 button:has-text("Add note")');
  await p.fill('#modal-notes-textarea', '<img src=x onerror=window.__x=1> & note');
  await p.click('text=Save Notes');
  log('note escaped / no script', [await p.evaluate(() => window.__x === undefined), (await p.textContent('#step-body-1')).includes('<img src=x')]);
  // import malformed / partial
  fs.writeFileSync('bad.json', JSON.stringify({ foo: 1, stepStatuses: { 1: 'bogus' }, activePhase: 99 }));
  await p.setInputFiles('#import-json-input', 'bad.json'); await p.waitForTimeout(200);
  log('partial import -> sane state', await p.evaluate(() => [appState.activePhase, appState.stepStatuses[1], appState.selectedServices.length]));
  fs.writeFileSync('bad2.json', '[1,2]'); await p.setInputFiles('#import-json-input', 'bad2.json'); await p.waitForTimeout(200);
  // reset
  await p.click('#step-body-1 li:first-child label');
  await p.click('button:has-text("Reset")');
  log('after reset: subtasks / storage', [await p.textContent('#metric-subtasks-count'), await p.evaluate(() => localStorage.getItem('NC_MEDICAID_NAVIGATOR_FULL_STATE_V3'))]);
  await p.reload();
  log('after reload: subtasks', await p.textContent('#metric-subtasks-count'));
  // print: real window.print() path (stub to avoid blocking) + Ctrl+P hook
  await p.evaluate(() => { window.__printed = 0; window.print = () => { window.__printed++; }; });
  await p.click('button:has-text("Print")'); await p.click('text=Print / Save PDF'); await p.waitForTimeout(150);
  log('window.print called / report built', [await p.evaluate(() => window.__printed), await p.evaluate(() => document.getElementById('print-report').children.length > 0)]);
  log('errors', errs);
  await b.close();
})();
