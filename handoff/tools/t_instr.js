const { chromium } = require('playwright-core');
const URL = (process.env.APP_URL||'file://'+require('path').resolve(__dirname,'../../nc_medicaid_bh_dashboard.html'));
const log = (k, v) => console.log(k.padEnd(48), JSON.stringify(v));
(async () => {
  const b = await chromium.launch({ executablePath: (process.env.CHROMIUM||'/opt/pw-browsers/chromium') });
  const errs = [];
  for (const [name, opts] of [['phone', { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true }], ['desktop', { viewport: { width: 1280, height: 900 } }]]) {
    const p = await (await b.newContext(opts)).newPage();
    p.on('pageerror', e => errs.push(e.message));
    await p.route(/fonts\./, r => r.abort());
    await p.goto(URL);
    // every row in every phase has a visible, labeled button
    const report = [];
    for (let ph = 1; ph <= 6; ph++) {
      await p.evaluate(n => switchPhaseTab(n), ph);
      await p.evaluate(() => toggleAllSteps()); // opens (or closes) all; make sure they are open
      if (await p.$$eval('[id^=step-body-].hidden', e => e.length)) await p.evaluate(() => toggleAllSteps());
      report.push(await p.evaluate(() => {
        const rows = [...document.querySelectorAll('#current-phase-container li')];
        const ok = rows.filter(li => { const b = li.querySelector('button'); const r = b.getBoundingClientRect(); return r.width > 0 && b.innerText.trim() === 'Instructions' && r.height >= 44; });
        return [rows.length, ok.length];
      }));
    }
    log(name + ': rows with visible Instructions button [total, ok] per phase', report);
    await p.evaluate(() => switchPhaseTab(1));
    if (await p.$$eval('[id^=step-body-1].hidden', e => e.length)) await p.evaluate(() => toggleStep(1));
    await p.screenshot({ path: `i_${name}.png`, clip: name === 'phone' ? undefined : { x: 0, y: 0, width: 1280, height: 900 } });
    // opens the right content
    await p.evaluate(() => document.getElementById('step-card-1').scrollIntoView());
    await p.click('#step-body-1 li:nth-child(2) button');
    log(name + ': modal title', await p.textContent('#modal-subtask-title'));
    log(name + ': specific instructions (no generic note)', await p.$eval('#modal-generic-note', e => e.classList.contains('hidden')));
    await p.keyboard.press('Escape');
    await p.evaluate(() => switchPhaseTab(2));
    if (await p.$$eval('[id^=step-body-].hidden', e => e.length)) await p.evaluate(() => toggleAllSteps());
    await p.click('#current-phase-container li:first-child button');
    log(name + ': phase 2 first item generic note shown', !(await p.$eval('#modal-generic-note', e => e.classList.contains('hidden'))));
    await p.keyboard.press('Escape');
    log(name + ': overflow-x', await p.evaluate(() => document.documentElement.scrollWidth > innerWidth));
  }
  log('errors', errs);
  await b.close();
})();
