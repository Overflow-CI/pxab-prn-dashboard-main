import re
F='/home/user/hello-world/nc_medicaid_bh_dashboard.html'
t=open(F).read()
def cut(t,start,end,new):
    s=t.index(start); e=t.index(end,s)
    return t[:s]+new+t[e:]

# ---- helpers + pills
t=t.replace("""    function getActiveRegionIds(counties) {""","""    function getPlanGroups(counties) {
      const selected = new Set(counties);
      return PLAN_ORDER.map(name => ({ name, counties: ALL_COUNTIES.filter(c => selected.has(c) && COUNTY_PLAN[c] === name) }))
        .filter(g => g.counties.length > 0);
    }

    const INTAKE_META = {
      open: { text: 'Taking applications', cls: 'bg-emerald-50 text-emerald-800 border-emerald-200' },
      closed: { text: 'Closed network', cls: 'bg-rose-50 text-rose-800 border-rose-200' }
    };
    const INTAKE_ROWS = [['peer', 'Peer support (8G)'], ['saiop', 'SAIOP (8A-12)'], ['sacot', 'SACOT (8A-13)']];

    function getActiveRegionIds(counties) {""",1)
t=t.replace("""      const activeRegionIds = getActiveRegionIds(draftFilters.selectedCounties);
      document.getElementById('active-regions-pills').innerHTML = activeRegionIds.length === 0""","""      const activeRegionIds = getActiveRegionIds(draftFilters.selectedCounties);
      const draftPlans = getPlanGroups(draftFilters.selectedCounties);
      document.getElementById('active-regions-pills').innerHTML = activeRegionIds.length === 0""",1)
t=t.replace("""              Reg ${id}: ${reg.tailoredPlan} &bull; ${reg.rootsHub}
            </span>
          `;
          }).join('');""","""              Reg ${id}: ${reg.rootsHub}
            </span>
          `;
          }).join('') + draftPlans.map(g => `
            <span class="inline-flex items-center gap-1.5 text-xs font-bold px-3 py-1 rounded-full bg-slate-100 text-slate-800 border border-slate-300">
              ${g.name}: ${g.counties.length} ${g.counties.length === 1 ? 'county' : 'counties'}
            </span>`).join('');""",1)

# ---- panel render
new_panel = r'''    function intakeChips(plan) {
      return INTAKE_ROWS.map(([key, label]) => {
        const m = INTAKE_META[plan.intake[key]];
        return `<span class="inline-flex items-center gap-1 text-xs font-semibold px-2 py-1 rounded-lg border ${m.cls}">${label}: ${m.text}</span>`;
      }).join('');
    }

    function planCardHtml(g) {
      const p = PLANS[g.name];
      const row = (label, val) => `<div><strong class="text-slate-900">${label}:</strong> ${val}</div>`;
      return `
        <div class="bg-slate-50/80 p-3 sm:p-4 rounded-2xl border border-slate-200 space-y-2.5">
          <div class="flex items-center justify-between gap-2">
            <span class="text-xs font-black uppercase text-sky-800 tracking-wider">Tailored Plan</span>
            <a href="${p.website}" target="_blank" rel="noopener noreferrer" class="text-xs text-sky-700 hover:underline font-bold">Provider site</a>
          </div>
          <div class="font-bold text-slate-900 text-sm sm:text-base">${g.name}</div>
          <p class="text-xs sm:text-sm text-slate-600"><strong class="text-slate-800">Your ${g.counties.length === 1 ? 'county' : 'counties'}:</strong> ${g.counties.join(', ')}</p>
          <div class="text-xs sm:text-sm text-slate-700 space-y-1">
            ${row('Provider line', `${linkify(p.phone)} (${p.phoneNote})`)}
            ${row('Utilization management', linkify(p.umPhone))}
            ${row('UM email', linkify(p.umEmail))}
            ${row('Network and contracting', linkify(p.networkEmail))}
            ${row('Office', p.office)}
            ${row('Claims payer ID', p.payerId)}
          </div>
          <div>
            <div class="text-xs font-bold uppercase text-slate-600 mb-1">New-provider intake</div>
            <div class="flex flex-wrap gap-1.5">${intakeChips(p)}</div>
            <p class="text-xs text-slate-600 mt-1.5 leading-snug">${p.note}</p>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            <a href="${p.joinUrl}" target="_blank" rel="noopener noreferrer" class="touch-target inline-flex items-center justify-center py-2.5 px-3 text-xs sm:text-sm font-bold text-sky-700 bg-white border border-sky-300 rounded-xl hover:bg-sky-50 transition">How to join the network</a>
            <a href="${p.portalUrl}" target="_blank" rel="noopener noreferrer" class="touch-target inline-flex items-center justify-center py-2.5 px-3 text-xs sm:text-sm font-bold text-sky-700 bg-white border border-sky-300 rounded-xl hover:bg-sky-50 transition">${p.portalLabel}</a>
          </div>
          <p class="text-xs text-slate-500">${p.portalNote}${p.needsUrl ? ` <a href="${p.needsUrl}" target="_blank" rel="noopener noreferrer" class="text-sky-700 hover:underline font-semibold">Current service needs</a>.` : ''} Checked ${p.asOf}.</p>
        </div>`;
    }

    function hubCardHtml(id, selected) {
      const reg = NC_REGIONS_DATA[id];
      const h = reg.rootsHubDetails;
      const color = getRegionColor(id);
      const mine = reg.counties.filter(c => selected.has(c));
      const row = (label, val) => `<div><strong class="text-slate-900">${label}:</strong> ${val}</div>`;
      return `
        <div class="bg-amber-50/50 p-3 sm:p-4 rounded-2xl border border-amber-200 space-y-2">
          <div class="flex items-center justify-between gap-2">
            <span class="text-xs font-black uppercase tracking-wider px-2.5 py-1 rounded-full text-white whitespace-nowrap" style="background-color: ${color}">Region ${id}</span>
            <a href="${h.website}" target="_blank" rel="noopener noreferrer" class="text-xs text-amber-800 hover:underline font-bold">Hub page</a>
          </div>
          <div class="font-bold text-slate-900 text-sm sm:text-base">${h.name}</div>
          <p class="text-xs sm:text-sm text-slate-600">${reg.name}: ${mine.length} of ${reg.counties.length} counties selected. Serves ${h.serves}.</p>
          <div class="text-xs sm:text-sm text-slate-700 space-y-1">
            ${row('Contact', h.contact)}
            ${row('Email', linkify(h.email))}
            ${row('Phone', h.phone ? `${linkify(h.phone)} (${h.phoneNote})` : h.phoneNote)}
            ${row('Address', h.address)}
          </div>
          ${h.note ? `<p class="text-xs text-amber-950/80 bg-white/70 p-2 rounded-lg border border-amber-200/60 leading-snug">${h.note}</p>` : ''}
        </div>`;
    }

    function statewideHtml() {
      const s = STATE_PROVIDER_SUPPORT;
      const cell = (label, val) => `
        <div class="bg-white p-2.5 rounded-xl border border-teal-100">
          <span class="font-bold block text-xs uppercase text-teal-800">${label}</span>
          <span class="text-xs sm:text-sm text-slate-700 block mt-0.5">${linkify(val)}</span>
        </div>`;
      return `
        <div class="bg-teal-50/50 border border-teal-200/90 rounded-2xl p-3 sm:p-4">
          <div class="text-xs font-black uppercase text-teal-900 tracking-wider mb-2">Statewide Medicaid provider support</div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
            ${cell('Provider Ombudsman', s.ombudsman)}
            ${cell('Medicaid Contact Center', s.contactCenter)}
            ${cell('NCTracks', s.nctracks)}
            ${cell('NC HealthConnex', s.hieDesk)}
          </div>
        </div>`;
    }

    function updateRegionalContactsDisplay() {
      const container = document.getElementById('regional-contacts-grid');
      const badge = document.getElementById('regions-active-count-badge');
      const activeIds = getActiveRegionIds(appState.selectedCounties);
      const groups = getPlanGroups(appState.selectedCounties);

      if (activeIds.length === 0) {
        badge.innerText = 'No counties selected';
        container.innerHTML = `
          <div class="p-6 text-center bg-white rounded-2xl border border-slate-200 shadow-xs">
            <h3 class="text-sm sm:text-base font-bold text-slate-800">No counties selected</h3>
            <p class="text-xs sm:text-sm text-slate-500 max-w-lg mx-auto mt-1">Select one or more counties in the filter above and tap <span class="font-bold text-sky-700">Apply Filters</span> to see the Tailored Plans, NC ROOTS hub leads and Medicaid provider support for your area.</p>
          </div>
          ${statewideHtml()}`;
        return;
      }

      badge.innerText = `${groups.length} ${groups.length === 1 ? 'plan' : 'plans'} · ${activeIds.length} ${activeIds.length === 1 ? 'hub region' : 'hub regions'} · ${countyCount(appState.selectedCounties.length)}`;
      const selected = new Set(appState.selectedCounties);
      container.innerHTML = `
        <div>
          <h3 class="text-sm font-bold text-slate-900 mb-2">Tailored Plans for your counties</h3>
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-3">${groups.map(planCardHtml).join('')}</div>
        </div>
        <div>
          <h3 class="text-sm font-bold text-slate-900 mb-2">NC ROOTS hub leads for your regions</h3>
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-3">${activeIds.map(id => hubCardHtml(id, selected)).join('')}</div>
        </div>
        ${statewideHtml()}`;
    }

'''
t=cut(t,"    function updateRegionalContactsDisplay() {","    function getFilteredSteps() {",new_panel)

# ---- print contacts
new_print = r'''      let contactsHtml = '';
      if (opts.contacts && activeRegionIds.length > 0) {
        const groups = getPlanGroups(appState.selectedCounties);
        const intakeLine = p => INTAKE_ROWS.map(([k, l]) => `${l}: ${INTAKE_META[p.intake[k]].text}`).join('; ');
        contactsHtml = `
          <section class="pr-contacts">
            <h2 class="pr-phase-title"><span>Plans and contacts</span></h2>
            <p class="pr-desc" style="margin-bottom: 6pt;"><b>Check before you call.</b> Plan and hub contacts were checked against public pages on Oct 18, 2026. Vaya Health and Partners merged on Oct 1, 2026. Confirm your county's plan at ncmedicaidplans.gov.</p>
            ${groups.map(g => {
              const p = PLANS[g.name];
              return `
              <article class="pr-region">
                <h3>${e(g.name)} <small>Tailored Plan</small></h3>
                <p class="pr-counties">Your counties: ${e(g.counties.join(', '))}</p>
                <div class="pr-cols">
                  <div>
                    <p>Provider line: ${e(p.phone)} (${e(p.phoneNote)})</p>
                    <p>Utilization management: ${e(p.umPhone)}</p>
                    <p>UM email: ${e(p.umEmail)}</p>
                    <p>Network and contracting: ${e(p.networkEmail)}</p>
                    <p>${e(p.office)}</p>
                  </div>
                  <div>
                    <p>Portal: ${e(p.portalUrl)}</p>
                    <p>How to join: ${e(p.joinUrl)}</p>
                    <p>Claims payer ID: ${e(p.payerId)}</p>
                    <p>New-provider intake: ${e(intakeLine(p))}</p>
                    <p>${e(p.note)}</p>
                  </div>
                </div>
              </article>`;
            }).join('')}
            ${activeRegionIds.map(id => {
              const reg = NC_REGIONS_DATA[id];
              const hub = reg.rootsHubDetails;
              return `
              <article class="pr-region">
                <h3>${e(reg.name)} <small>NC ROOTS hub lead</small></h3>
                <p class="pr-counties">Your counties: ${e(reg.counties.filter(c => selected.has(c)).join(', '))}</p>
                <div class="pr-cols">
                  <div>
                    <p><b>${e(hub.name)}</b></p>
                    <p>Contact: ${e(hub.contact)}</p>
                    <p>Email: ${e(hub.email)}</p>
                  </div>
                  <div>
                    <p>Phone: ${e(hub.phone || 'none published')}${hub.phone ? ` (${e(hub.phoneNote)})` : ''}</p>
                    <p>${e(hub.address)}</p>
                    <p>${e(hub.website)}</p>
                  </div>
                </div>
              </article>`;
            }).join('')}
            <article class="pr-region">
              <h3>Statewide Medicaid provider support</h3>
              <div class="pr-cols">
                <div><p>${e(STATE_PROVIDER_SUPPORT.ombudsman)}</p><p>${e(STATE_PROVIDER_SUPPORT.contactCenter)}</p></div>
                <div><p>${e(STATE_PROVIDER_SUPPORT.nctracks)}</p><p>${e(STATE_PROVIDER_SUPPORT.hieDesk)}</p></div>
              </div>
            </article>
          </section>`;'''
s=t.index("      let contactsHtml = '';")
e_=t.index("          </section>`;",s)+len("          </section>`;")
t=t[:s]+new_print+t[e_:]

# ---- generic modal fallback + banner
t=t.replace("`NC Medicaid Provider Support: 877-201-3750`","`NC Medicaid Provider Ombudsman: 866-304-7062`",1)
t=re.sub(r'<p class="text-sm text-amber-900 bg-amber-50[^>]*><strong>Check your plan first\.</strong>[^<]*</p>',
 '<p class="text-sm text-amber-900 bg-amber-50 border border-amber-200 rounded-xl px-3 py-2"><strong>Check before you call.</strong> Plans are matched by county. Contacts were checked against public pages on Oct 18, 2026, and Vaya Health and Partners merged on Oct 1, 2026. Confirm your county at ncmedicaidplans.gov. NC ROOTS hub leads are organized by region.</p>',t,count=1)
t=t.replace("LME/MCO tailored plans, NC ROOTS hubs and Medicaid provider support for your selected counties.","Tailored Plans by county, NC ROOTS hubs by region, and statewide Medicaid provider support.",1)
open(F,'w').write(t)
print('ui ok')
