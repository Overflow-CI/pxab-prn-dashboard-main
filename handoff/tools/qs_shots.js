// v006: the setup wizard opens for new users and would block clicks, so tests close it after load.
async function dismissSetupWizard(page) {
  await page.evaluate(() => { const d = document.getElementById('setup-wizard'); if (d && d.open) d.close(); });
}
const { chromium } = require('playwright-core');
const URL=(process.env.APP_URL||'file://'+require('path').resolve(__dirname,'../../nc_medicaid_bh_dashboard.html'));
const OUT=require('path').resolve(__dirname,'../../docs/images')+'/';
(async()=>{
const b=await chromium.launch({executablePath:(process.env.CHROMIUM||'/opt/pw-browsers/chromium')});
const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});
const p=await ctx.newPage(); p.on('dialog',d=>d.accept()); await p.route(/fonts\./,r=>r.abort());
await p.goto(URL); await p.waitForTimeout(300); await dismissSetupWizard(p);
const shot=async(n,opt={})=>{await p.waitForTimeout(250);await p.screenshot({path:OUT+n+'.png',...opt});console.log(n)};
const el=async(sel,n,h)=>{const l=p.locator(sel);await l.scrollIntoViewIfNeeded();const bb=await l.boundingBox();await p.waitForTimeout(250);
  await p.screenshot({path:OUT+n+'.png',fullPage:true,clip:{x:0,y:bb.y+await p.evaluate(()=>scrollY),width:390,height:h?Math.min(h,bb.height):bb.height}});console.log(n)};
// 01 first screen
await shot('01-first-screen');
// 02 setup open, county menu open with a few counties
await p.tap('#setup-panel > summary'); await p.waitForTimeout(200);
await p.tap('#county-dropdown-trigger'); await p.waitForTimeout(200);
await p.fill('#county-search-input','a'); await p.fill('#county-search-input','');
await p.evaluate(()=>{setDraftCounties(['Wake','Mecklenburg','Dare']);});
await shot('02-choose-counties');
// close dropdown
await p.tap('#county-dropdown-trigger'); await p.waitForTimeout(200);
await p.tap('#ccp-dropdown-trigger'); await p.waitForTimeout(200);
await shot('03-choose-services');
await p.tap('#ccp-dropdown-trigger'); await p.waitForTimeout(200);
await el('#setup-panel','04-apply-filters');
await p.tap('#apply-filter-btn'); await p.waitForTimeout(600);
await p.evaluate(()=>scrollTo(0,0)); await shot('05-after-apply'); await p.waitForTimeout(4500); await p.evaluate(()=>{document.getElementById('toast-container').innerHTML=''});
// regional panel
await p.evaluate(()=>{document.getElementById('regional-panel').open=true});
await el('#regional-panel','06-regional-contacts',1500);
// schedule
await p.evaluate(()=>{document.getElementById('regional-panel').open=false;document.getElementById('schedule-panel').open=true});
await el('#schedule-panel','07-fees-and-timeline',1100);
await p.evaluate(()=>{document.getElementById('schedule-panel').open=false});
// phases + steps
await p.evaluate(()=>{document.getElementById('setup-panel').open=false});
await p.evaluate(()=>{const n=document.getElementById('phase-heading');scrollTo(0,n.getBoundingClientRect().top+scrollY-100)}); await shot('08-phases-and-steps');
// check rows
if(await p.getAttribute('#step-toggle-1','aria-expanded')!=='true'){await p.tap('#step-toggle-1');} await p.waitForTimeout(150);
const first=p.locator('#step-body-1 li:first-child label'); await p.tap('#step-body-1 li:first-child label'); await p.waitForTimeout(250);
await p.locator('#step-card-1').scrollIntoViewIfNeeded();
await el('#step-card-1','09-checklist-and-instructions-button',1250);
// instructions modal
await p.evaluate(()=>openSubtaskDetailModal('step_4_sub_1',4,1)); await p.waitForTimeout(400);
await shot('10-instructions-dialog');
await p.evaluate(()=>{const b=document.getElementById('modal-review-block'); b.scrollIntoView({block:'center'})}); await shot('11-check-before-relying');
await p.tap('#subtask-detail-modal button[aria-label*="lose"], #subtask-detail-modal button:has-text("Close")').catch(()=>{});
await p.evaluate(()=>closeSubtaskModal()); await p.waitForTimeout(250);
// notes
await p.tap('#step-body-1 button:has-text("Note")'); await p.waitForTimeout(300);
await p.fill('#modal-notes-textarea','Called the Secretary of State. Filed on Oct 20. Confirmation number saved in the shared drive.');
await shot('12-notes-dialog');
await p.evaluate(()=>closeNotesModal()); await p.waitForTimeout(200);
// status dropdown / step card
await p.locator('#step-status-1').scrollIntoViewIfNeeded();
// header buttons
await p.evaluate(()=>scrollTo(0,0)); 
await p.screenshot({path:OUT+'13-header-actions.png',clip:{x:0,y:0,width:390,height:150}});console.log('13');
// print dialog
await p.tap('nav[aria-label="Plan actions"] button:has-text("Print")'); await p.waitForTimeout(300);
await shot('14-print-dialog');
await p.evaluate(()=>closePrintModal());
// pdf page
await p.evaluate(()=>{printOptions={scope:'all',contacts:true};preparePrint&&preparePrint();});
await p.emulateMedia({media:'print'});
await p.pdf({path:(process.env.TMPDIR||'/tmp')+'/qs.pdf',format:'Letter',printBackground:true,preferCSSPageSize:true});
await p.evaluate(()=>finishPrint&&finishPrint());
// desktop
const d=await b.newContext({viewport:{width:1280,height:900},deviceScaleFactor:1});
const q=await d.newPage(); await q.route(/fonts\./,r=>r.abort()); await q.goto(URL); await dismissSetupWizard(q);
await q.evaluate(()=>{loadState({selectedCounties:['Wake','Mecklenburg','Dare'],subtaskChecks:{step_1_sub_0:true,step_1_sub_1:true},activePhase:1});saveState();});
await q.reload(); await q.waitForTimeout(400);
await q.screenshot({path:OUT+'15-desktop.png'});console.log('15');
await b.close();})();
