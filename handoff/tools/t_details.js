const { chromium } = require('playwright-core');
const log = (k, v) => console.log(k.padEnd(52), JSON.stringify(v));
(async () => {
  const b = await chromium.launch({ executablePath: (process.env.CHROMIUM||'/opt/pw-browsers/chromium') });
  const errs = [];
  const p = await (await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true })).newPage();
  p.on('pageerror', e => errs.push(e.message));
  await p.route(/fonts\./, r => r.abort());
  await p.goto((process.env.APP_URL||'file://'+require('path').resolve(__dirname,'../../nc_medicaid_bh_dashboard.html')));
  // open every one of the 116 dialogs and inspect what renders
  const res = await p.evaluate(() => {
    const out = { opened: 0, empty: [], noReview: [], genericNote: [], badLinks: 0, links: 0, noopener: 0, pillCounts: {}, basis: 0 };
    MASTER_STEPS.forEach(step => step.subtasks.forEach((_, i) => {
      const key = subtaskKey(step.id, i);
      openSubtaskDetailModal(key, step.id, i);
      out.opened++;
      const ins = document.querySelectorAll('#modal-instructions-body > div').length;
      const tips = document.querySelectorAll('#modal-tips-body > div').length;
      if (ins < 3 || tips < 1) out.empty.push(key);
      if (document.getElementById('modal-review-block').classList.contains('hidden')) out.noReview.push(key);
      if (!document.getElementById('modal-generic-note').classList.contains('hidden')) out.genericNote.push(key);
      const pill = document.getElementById('modal-confidence-pill').innerText.split(':')[0];
      out.pillCounts[pill] = (out.pillCounts[pill] || 0) + 1;
      if (document.getElementById('modal-review-body').innerText.includes('Basis:')) out.basis++;
      document.querySelectorAll('#subtask-detail-modal a[href]').forEach(a => {
        out.links++;
        if (!/^(https?:|tel:|mailto:)/.test(a.getAttribute('href'))) out.badLinks++;
        if (a.target === '_blank' && !/noopener/.test(a.rel)) out.noopener++;
      });
      closeSubtaskModal();
    }));
    return out;
  });
  log('dialogs opened', res.opened); log('thin instructions/tips', res.empty); log('missing review block', res.noReview);
  log('generic note shown (should be none)', res.genericNote); log('links / bad hrefs / missing noopener', [res.links, res.badLinks, res.noopener]);
  log('confidence pills', res.pillCounts); log('entries with a Basis line (H.R. 1)', res.basis);
  // visual check of one sourced entry and one H.R. 1 entry
  for (const [key, step, idx, file] of [['step_18_sub_1', 18, 1, 'd_step18.png'], ['step_28_sub_1', 28, 1, 'd_step28.png']]) {
    await p.evaluate(([k, s, i]) => openSubtaskDetailModal(k, s, i), [key, step, idx]);
    await p.locator('#subtask-detail-modal > div').screenshot({ path: file });
    // scroll the body to the review block and shoot again
    await p.evaluate(() => document.getElementById('modal-review-block').scrollIntoView());
    await p.locator('#subtask-detail-modal > div').screenshot({ path: file.replace('.png', '_review.png') });
    await p.evaluate(() => closeSubtaskModal());
  }
  log('errors', errs);
  await b.close();
})();
