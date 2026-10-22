const { chromium } = require('playwright-core');
const URL = (process.env.APP_URL||'file://'+require('path').resolve(__dirname,'../../nc_medicaid_bh_dashboard.html'));
(async () => {
  const b = await chromium.launch({ executablePath: (process.env.CHROMIUM||'/opt/pw-browsers/chromium') });
  const p = await (await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true })).newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.route(/fonts\./, r => r.abort());
  // seeded state: some progress, a blocked step, notes (incl. markup that must be escaped), two regions
  await p.addInitScript(() => {
    localStorage.setItem('NC_MEDICAID_NAVIGATOR_FULL_STATE_V3', JSON.stringify({
      selectedCounties: ['Wake', 'Durham', 'Buncombe'], selectedServices: ['8G', '8A-12', '8A-13'],
      subtaskChecks: { step_1_sub_0: true, step_1_sub_1: true, step_1_sub_2: true, step_1_sub_3: true, step_1_sub_4: true, step_2_sub_0: true, step_2_sub_1: true, step_3_sub_0: true },
      stepStatuses: { 1: 'completed', 2: 'in_progress', 3: 'in_progress', 4: 'blocked' },
      stepNotes: { 2: 'EIN letter filed in Drive/Legal. Ref #CP575 <b>not bold</b> & more', 4: 'Landlord waiting on zoning letter.\nFollow up Monday 9am.' },
      activePhase: 1 }));
  });
  await p.goto(URL);
  // the real user flow
  await p.tap('button:has-text("Print")');
  console.log('modal open', await p.isVisible('#print-modal'), '|', await p.textContent('#print-preview-text'));
  await p.screenshot({ path: 'pm_modal.png' });
  for (const scope of ['all', 'open']) {
    await p.evaluate(s => { document.querySelector(`input[name=print-scope][value=${s}]`).checked = true; }, scope);
    await p.evaluate(() => { printOptions = { scope: document.querySelector('input[name="print-scope"]:checked').value, contacts: true }; preparePrint(); });
    console.log(scope, 'title during print:', await p.title());
    await p.emulateMedia({ media: 'print' });
    console.log(scope, 'visible body children in print:', await p.evaluate(() => [...document.body.children].filter(e => getComputedStyle(e).display !== 'none').map(e => e.id || e.tagName)));
    await p.pdf({ path: `plan_${scope}.pdf`, preferCSSPageSize: true, printBackground: true, displayHeaderFooter: false });
    await p.emulateMedia({ media: 'screen' });
    await p.evaluate(() => finishPrint());
    console.log(scope, 'title restored:', await p.title());
  }
  console.log('report has escaped markup:', await p.evaluate(() => document.getElementById('print-report').innerHTML.includes('&lt;b&gt;not bold&lt;/b&gt;')), '| raw <b> leaked:', await p.evaluate(() => document.getElementById('print-report').innerHTML.includes('<b>not bold')));
  console.log('errors', errs);
  await b.close();
})();
