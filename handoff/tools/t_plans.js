// v006: the setup wizard opens for new users and would block clicks, so tests close it after load.
async function dismissSetupWizard(page) {
  await page.evaluate(() => { const d = document.getElementById('setup-wizard'); if (d && d.open) d.close(); });
}
const { chromium } = require('playwright-core');
(async()=>{const b=await chromium.launch({executablePath:(process.env.CHROMIUM||'/opt/pw-browsers/chromium')});
const p=await b.newPage({viewport:{width:390,height:844}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto((process.env.APP_URL||'file://'+require('path').resolve(__dirname,'../../nc_medicaid_bh_dashboard.html'))); await dismissSetupWizard(p);
const r=await p.evaluate(()=>{
 const cs=['Wake','Cabarrus','Dare','Buncombe','Guilford','Mecklenburg'];
 appState.selectedCounties=cs; updateRegionalContactsDisplay();
 const txt=document.getElementById('regional-contacts-grid').textContent;
 const groups=getPlanGroups(cs).map(g=>g.name+':'+g.counties.join('/'));
 buildPrintReport&&0;
 return {groups,badge:document.getElementById('regions-active-count-badge').innerText,
  has:['866-304-7062','Vaya Partners','Alliance Health','Trillium Health Resources','Impact Health','Taking applications','Closed network'].map(s=>txt.includes(s)),
  old:['877-201-3750','Partners Health Management','Executive Director'].map(s=>txt.includes(s)),
  counts:Object.values(COUNTY_PLAN).reduce((a,v)=>(a[v]=(a[v]||0)+1,a),{})};});
console.log(JSON.stringify(r));
await p.evaluate(()=>{document.getElementById('regional-panel').open=true});
await p.screenshot({path:'plans_phone.png',fullPage:false});
await p.locator('#regional-contacts-grid').screenshot({path:'plans_grid.png'});
const pr=await p.evaluate(()=>{preparePrint&&0;return typeof buildPrintReport});console.log(pr,errs);
await b.close();})();
