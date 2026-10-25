# Technical specification: NC Medicaid BH Operations Navigator

| | |
|---|---|
| **Product** | NC Medicaid Behavioral Health Operations & Compliance Dashboard ("Navigator") |
| **Version** | 4.0 |
| **Deliverable** | One self-contained file: `nc_medicaid_bh_dashboard.html` (about 440 KB) |
| **Document date** | 2026-10-19 |
| **Audience** | Developers and maintainers. For end users, see [QUICK_START.md](QUICK_START.md). |

---

## 1. Purpose and scope

The Navigator guides a new North Carolina provider through the steps needed to start billing NC Medicaid for three behavioral health services:

| Code | Service |
|---|---|
| CCP 8G | Peer Support Services |
| CCP 8A-12 | Substance Abuse Intensive Outpatient Program (SAIOP) |
| CCP 8A-13 | Substance Abuse Comprehensive Outpatient Treatment (SACOT) |

It does five things:

1. Presents a checklist of **31 steps and 116 tasks in 6 phases**, filtered by the services and counties the user selects.
2. Tracks progress, per-step status and per-step notes, saved in the browser.
3. Calculates fees and schedule from the step data, and draws a timeline.
4. Shows plan, hub and statewide contacts for the user's counties.
5. Produces a printable plan (PDF through the browser's print dialog).

Every task has researched instructions, tips, contacts, sources and a confidence rating.

**Not in scope:** user accounts, a server, multi-user sync, legal advice, or automatic updates of regulatory content. The content is a research summary and needs verification (see [`NC_Medicaid_Verification_Checklist.md`](../NC_Medicaid_Verification_Checklist.md)).

## 2. Design constraints

| Constraint | How it is met |
|---|---|
| Single HTML file | CSS, JavaScript and data are inline. Nothing to build or deploy. |
| No backend | State is saved in `localStorage` and can be exported or imported as JSON. |
| Works offline | The file makes no network requests and uses the device's system fonts. |
| Mobile first | Layout starts at 390 px. Wider layouts are enhancements (`sm` 640 px, `lg` 1024 px). |
| Accessible | Labeled controls, focus-trapped dialogs, Escape to close, 44 px touch targets, reduced-motion support, skip link. |
| Printable | A separate print-only report is built from state on demand. |

## 3. Architecture

### 3.1 File layout

| Region of `nc_medicaid_bh_dashboard.html` | Contents |
|---|---|
| `<head>` | Meta tags, a large inline `<style>` with the **precompiled Tailwind CSS v3.4**, then a second `<style>` with the master stylesheet and functional CSS (see 3.3). No font or script links. |
| `<body>` markup | Header, overview card, "Next up" card, Setup, Regional contacts and Fees & timeline panels, phase tabs, step cards container, three dialogs (instructions, notes, print), toast container, `#print-report`. |
| `<script>` | All data constants, then state, rendering and event code, in that order. No modules, no libraries. |

### 3.2 Runtime model

The app uses a simple **state, render** loop with no framework.

```
user action ─► mutate appState ─► saveState() ─► renderDashboard()
                                                   ├─ renderProgress()  (metrics, Next up, timeline, phase tabs)
                                                   ├─ updateRegionalContactsDisplay()
                                                   └─ renderCurrentPhaseCards()
```

- `appState` is the only persisted state. `draftFilters` holds un-applied county and service choices.
- `expandedSteps` and `initializedPhases` (both `Set`) are UI-only and are **not** saved.
- Rendering writes HTML strings into containers (`innerHTML`). User-supplied text (notes) always goes through `escapeHtml`.

### 3.3 Styling

- **Tailwind CSS v3.4, precompiled and inlined.** The browser never compiles CSS. If you add a new Tailwind class, regenerate: `npx tailwindcss@3 --content nc_medicaid_bh_dashboard.html --minify -o tw.css`, then paste the output into the first `<style>` block. Classes that are not in the compiled CSS silently do nothing.
- **Master stylesheet block** (second `<style>`) is the corrected Option B data-driven dashboard stylesheet, applied unchanged apart from the notes below. It defines the colour tokens on `:root` (`--bg-main`, `--bg-card`, `--bg-surface`, `--border-color`, `--text-main`, `--text-sub`, `--text-dim`, `--accent-gold`, `--accent-teal`, `--accent-red`). A short alias block maps the older token names the markup uses (`--text-primary`, `--text-secondary`, `--text-muted`, `--accent-teal-hover`, `--color-gold`, `--color-red`). Its layout rules include a sticky header, `.plan-overview-card` for the Plan Progress card, `.step-trigger-row` and `.step-panel-expanded` / `.step-panel-collapsed` for steps.
- **Overview card scope:** the sheet's overview rule matched `section:first-of-type`, which squeezed the first section that follows the header. The rule now applies only to the `.plan-overview-card` class on the overview section, and a functional rule stacks its grid into one column so the progress and next-step content fits.
- **Deviations from the master, to meet WCAG AA:** the teal accent is used as a fill only with dark text (`--bg-main`) on the Apply button, and the hover teal is `#0E7C66` (white text on it passes).
- **Functional rules kept alongside it:** `.touch-target` (min 48 px), a visible focus ring, 16 px input text on phones (prevents iOS zoom on focus), `details`/`summary` chevrons, the `body.modal-open` scroll lock, and the `@page` margin boxes and `#print-report` / `.pr-*` print layout for the binder printout.
- **Reduced motion** is handled in JavaScript: `toggleStep` checks `prefers-reduced-motion` and skips the slide animation.
- **Dialog stacking:** the sticky header has `z-index: 200`, so a functional rule lifts `.fixed[role="dialog"]` to 300. Without it the header covers the dialogs.
- **Minimum text size** is 12 px (Tailwind `text-xs`). The master stylesheet does not set a text floor. Form fields are 16 px on phones.

## 4. Data model

All data is JavaScript constants defined at the top of the script. Nothing is fetched.

### 4.1 `MASTER_STEPS` (31 entries)

| Field | Type | Meaning |
|---|---|---|
| `id` | number | Unique, 1 to 31. Used in saved state and DOM ids. |
| `phase` | 1–6 | Phase number. |
| `phaseName` | string | Full phase title. `PHASE_NAMES` is derived from it. |
| `stepNumber` | string | Display label, for example `Step 14`. |
| `title`, `description` | string | Card heading and summary. |
| `services` | string[] | Subset of `['8G','8A-12','8A-13']`. A step shows only if it shares a service with the user's selection. |
| `responsible` | string | Suggested owner. |
| `timeWeeks` | string | Human-readable duration. |
| `timelineStartWeek`, `timelineDurationWeeks` | number | Drive the timeline and the schedule metric. |
| `costEstimate` | string | Display text. |
| `statutoryFees` | `{label, min, max, perPerson?}[]` | Drive the fee metric. `perPerson: true` fees are totalled separately. |
| `resourceName`, `resourceUrl` | string | Primary authority link. |
| `dependencies` | string | Display text. |
| `subtasks` | string[] | The checklist items. Index order matters (see state keys). |

Steps per phase: 1 → 8, 2 → 8, 3 → 4, 4 → 1, 5 → 4, 6 → 6.

Services per step: most steps list all three. Four steps list only `8A-12` and `8A-13`: Steps 14, 15 and 16 (DHSR application, survey, plan of correction), because peer support does not need a DHSR license, and one other step. One step lists only `8G`. With peer support (8G) alone selected, 27 steps show.

### 4.2 `SUBTASK_DETAILS_MAP` (116 entries)

Keyed by `step_<stepId>_sub_<index>`, for example `step_4_sub_1`.

| Field | Present on | Meaning |
|---|---|---|
| `instructions`, `tips`, `contacts` | all 116 | String arrays shown in the instructions dialog. `contacts` pass through `linkify`. |
| `sources` | 105 | Integer indexes into `DETAIL_SOURCES`. |
| `confidence` | 105 | `high`, `medium` or `low`. |
| `verify` | 105 | What the user must still check. May contain "NOT VERIFIED" for unconfirmed facts. |
| `basis` | 26 (Phase 6) | `required`, `expected` or `recommended`. |
| `effectiveDate` | 26 (Phase 6) | Free text, for example `2027-01-01`. |

The 11 entries for Steps 1–3 have no `sources`, `confidence` or `verify`. The dialog labels them **"Not yet checked against sources"**.

### 4.3 `DETAIL_SOURCES`

An array of 242 unique URLs. Index positions are referenced from `SUBTASK_DETAILS_MAP.sources`, so **do not reorder or delete entries**. Append new URLs at the end. The full list with publishers and categories is in [`nc_medicaid_sources.csv`](../nc_medicaid_sources.csv).

### 4.4 Plans, counties and regions

| Constant | Shape | Notes |
|---|---|---|
| `PLAN_ORDER` | `['Alliance Health','Trillium Health Resources','Vaya Partners']` | Display order. |
| `PLANS` | `{ [planName]: {...} }` | Contacts for each Tailored Plan: `phone`, `phoneNote`, `website`, `office`, `umPhone`, `umEmail`, `networkEmail`, `portalLabel`, `portalUrl`, `portalNote`, `joinUrl`, `needsUrl`, `payerId`, `intake {peer, saiop, sacot}`, `note`, `asOf`. `intake` values are `open` or `closed`. |
| `COUNTY_PLAN` | `{ [county]: planName }` | All 100 counties. Plans are assigned **by county**. (Vaya Partners 47, Trillium 46, Alliance 7.) |
| `NC_REGIONS_DATA` | `{1..6: {id, name, rootsHub, rootsHubDetails, counties[]}}` | The six Medicaid regions. Used for the county picker grouping and for NC ROOTS hub leads, which are organized by region. |
| `STATE_PROVIDER_SUPPORT` | `{ombudsman, contactCenter, nctracks, hieDesk}` | Statewide contacts, plain strings. |
| `REGIONS`, `ALL_COUNTIES` | derived | `Object.values(NC_REGIONS_DATA)` and its flattened county list. |

**Invariant:** every county in `NC_REGIONS_DATA` must be a key in `COUNTY_PLAN`, and the two must agree on the 100-county set.

### 4.5 Other constants

| Constant | Purpose |
|---|---|
| `STORAGE_KEY` | `'NC_MEDICAID_NAVIGATOR_FULL_STATE_V3'`. Unchanged since v3, so saved progress carries over. |
| `ALL_SERVICES` | `['8G','8A-12','8A-13']` |
| `PHASE_TITLES`, `PHASE_SHORT`, `PHASE_NAMES` | Long titles, tab labels, and titles derived from steps. |
| `STATUS_META` | `not_started`, `in_progress`, `completed`, `blocked`, each with a label, plain text and CSS classes. |
| `SERVICE_NAMES` | Full policy names. |
| `CONFIDENCE_META`, `BASIS_LABELS` | Text and colors for the review block. |
| `INTAKE_META`, `INTAKE_ROWS` | Labels for plan intake chips. |

## 5. Application state

### 5.1 Shape

```json
{
  "selectedCounties": ["Wake", "Mecklenburg"],
  "selectedServices": ["8G", "8A-12", "8A-13"],
  "subtaskChecks": { "step_1_sub_0": true },
  "stepStatuses": { "1": "in_progress" },
  "stepNotes": { "1": "Called the Secretary of State." },
  "activePhase": 1,
  "startDate": "2027-03-01",
  "verification": { "1": { "status": "source_checked", "source": "sosnc.gov", "date": "2026-10-25" } },
  "roleFilter": "billing",
  "setupDone": true
}
```

`startDate`, `verification`, `roleFilter` and `setupDone` were added in v006. Saves from earlier versions load without them, and `setupDone` is treated as true for any save that already has service lines, so existing users are not shown the setup wizard again.

### 5.2 Validation (`normalizeState`)

Every load path (localStorage, imported file) passes through `normalizeState`, which returns a well-formed object and silently drops anything invalid:

- Counties not in `ALL_COUNTIES` are removed.
- Services not in `ALL_SERVICES` are removed. If none remain, all three are restored.
- Statuses not in `STATUS_META` are removed.
- Notes that are not non-empty strings are removed.
- `activePhase` falls back to 1 if it is not a real phase.
- Non-object input returns the default state.

### 5.3 Persistence

- `saveState()` writes JSON to `localStorage` inside `try/catch`. If storage is unavailable, the app still works but does not remember anything.
- `initState()` reads and parses inside `try/catch`, then builds the county dropdown and loads state.
- **Export** downloads `NC_Medicaid_BH_Navigator_Backup_YYYY-MM-DD.json` (the raw `appState`).
- **Import** parses the file, rejects non-objects, runs `loadState` (which normalizes), saves and shows a toast.
- **Reset** asks `window.confirm`, removes the storage key and reloads the default state.

### 5.4 Step status rules

`evaluateStepStatusFromSubtasks(stepId)` runs when a checkbox changes:

| Checked tasks | Status |
|---|---|
| 0 | `not_started` (unless the step is `blocked`, which is kept) |
| 1 to n−1 | `in_progress` |
| all | `completed` |

The user can also set a step's status from its dropdown, including `blocked`. A manual status is overwritten the next time a checkbox changes, except that `blocked` survives a return to zero checked tasks.

## 6. Calculations

All come from step data. Nothing is typed in by hand.

| Metric | Rule |
|---|---|
| **Overall %** | `round(checked tasks / total tasks)` over the **filtered** steps. |
| **Steps done** | Count of filtered steps whose status is `completed`. |
| **Fees (headline)** | Sum of `min` and `max` of `statutoryFees` where `perPerson` is false, over filtered steps. Shown as a range. With all services: **$1,358–$1,705**. |
| **Per-person fees** | Sum of fees with `perPerson: true`, shown as "+ $x–$y per staff member". With all services: **$73–$113**. |
| **Schedule span** | `last end week − first start week + 1`, where end week = `timelineStartWeek + timelineDurationWeeks − 1`. With all services: **31 weeks**. |
| **Open work runs through** | The latest end week among filtered steps that are not complete. |
| **Timeline axis length** (`TOTAL_WEEKS`) | Latest end week across **all** steps, rounded up to a multiple of 8. |
| **Next up** | The first filtered step, in order, whose status is not `completed`. |

Fees and weeks recompute whenever the service filter changes. Fee estimates that are not statutory (insurance, build-out, accreditation) are display text only and are not included in totals.

## 7. Filtering

Two filters, staged in `draftFilters` and applied together:

1. **Services:** checkboxes for 8G, 8A-12, 8A-13. At least one must stay selected (a toast blocks unchecking the last one).
2. **Counties:** a searchable multi-select grouped by region, with "Toggle Region", "All 100" and "Clear".

`checkFilterChanges()` compares the draft with `appState` and enables the **Apply Filters** and **Discard** buttons. `applyFilters()` copies draft to state, saves, re-renders and shows a toast. Counties do not change which steps show. They drive the **Regional contacts** panel and the printed contacts. Services change which steps show and the fee and schedule totals.

## 8. User interface

### 8.1 Page structure (top to bottom)

| Element | Notes |
|---|---|
| Header (`#site-header`) | Title, version badge, and four actions: **Print**, **Export**, **Import** (file input), **Reset**. |
| Overview card | Overall % with a progress bar (`role="progressbar"`), steps done, items checked. |
| **Next up** (`#next-up`) | The next unfinished step with an Open button. When all are done, a Print button instead. |
| **Setup** panel (`#setup-panel`, a `<details>`) | County dropdown, services dropdown, status line, Apply and Discard. A one-line summary shows when closed. |
| **Regional contacts** panel (`#regional-panel`) | Plan cards by county, hub cards by region, statewide support. |
| **Fees & timeline** panel (`#schedule-panel`) | Fee and weeks tiles and the Gantt-style timeline. Tapping a bar opens its step. |
| Phase tabs (`#phase-tabs-container`) | Six tabs with per-phase %. The active tab scrolls into view. |
| Step cards (`#current-phase-container`) | One card per step in the active phase, with an "Expand all / Collapse all" control. |
| Phase pager | Previous and next phase buttons. |

Panels start collapsed on a phone. On a desktop (`min-width: 1024px`) the Setup panel opens on first visit with no counties, and a phase opens with all its steps expanded. On a phone only the first unfinished step in a phase opens.

### 8.2 Step card

Header (step number, status badge, title, per-step progress bar) toggles the body. The body has the description, service chips, a **status dropdown**, an **Add note / Edit note** button, a facts grid (cost, duration, authority link, dependency), and the checklist.

Each checklist row is a `<label>` wrapped around a checkbox, so **tapping anywhere on the row checks it**. A separate **Instructions** button on every row opens the instructions dialog. After a re-render, focus returns to the checkbox that changed.

### 8.3 Dialogs

All dialogs are `role="dialog"` elements managed by `openModal` and `closeModal`.

| Dialog | Content |
|---|---|
| Instructions (`#subtask-detail-modal`) | Step-by-step instructions, tips, contacts and the **Check before relying on this** block (confidence pill, "Basis" and "Applies from" for Phase 6, verify note, source links). Footer: Close, and Mark complete or Mark incomplete. |
| Notes (`#notes-modal`) | A textarea saved per step. Saving an empty note removes it. |
| Print (`#print-modal`) | Choose "Entire plan" or "Unfinished work only", and whether to include contacts. |

Behavior:
- Phone: bottom sheet. Desktop: centered dialog.
- Opening a dialog saves the previously focused element, locks body scroll (`body.modal-open`) and focuses the first `[data-autofocus]` element or button. Closing restores focus.
- `keydown` handler: **Escape** closes the topmost dialog. **Tab** and **Shift+Tab** wrap focus within it.
- Clicking the backdrop closes it.

### 8.4 Regional contacts rendering

For the applied counties:
- `getPlanGroups` groups counties by plan, in `PLAN_ORDER`. One card per plan lists only the user's counties in that plan.
- `getActiveRegionIds` finds regions that contain at least one selected county. One hub card per region.
- A statewide block always shows.

Plan cards show provider line, UM contact, network email, office, claims payer ID, three intake chips (peer support, SAIOP, SACOT), links to "How to join" and the portal, and the "checked" date. All phones and emails are turned into links by `linkify`.

### 8.5 Toasts

`showToast(title, message)` appends a message to `#toast-container`. They dismiss themselves after a few seconds.

## 9. Printing

- `openPrintModal` → `startPrint` → `preparePrint` builds the report into `#print-report` with `buildPrintReport(options)`, sets `document.title` to `NC_Medicaid_BH_Plan_YYYY-MM-DD` (so the saved PDF has that name), then calls `window.print()`.
- `beforeprint` also runs `preparePrint`, so **Ctrl/Cmd + P** prints the same report. `afterprint` runs `finishPrint`, which restores the title.
- In print media, everything except `#print-report` is hidden.
- The report contains a title block, services and county footprint, summary tiles, a per-phase progress table, the estimated fees line, then each step: status in words, drawn checkboxes (checked ones struck through), owner, time, cost, dependencies, notes and (optionally) the plan, hub and statewide contacts.
- **Unfinished work only** omits completed steps and says so if none are left.
- All text is escaped (`e()` = `escapeHtml`).
- Page numbers ("Page X of Y") use `@page` margin boxes. These are supported by **Chrome and Edge**. Other browsers print without page numbers.

## 10. Security and privacy

| Topic | Behavior |
|---|---|
| Data leaves the device? | **No.** There is no network call that carries user data. No request is made after the page loads. |
| Stored data | Checks, statuses, notes, counties and services in `localStorage` for this file's origin. |
| XSS | Notes and imported values are escaped before display. `linkify` escapes first, then wraps recognized phones, emails and URLs. Imports are validated by `normalizeState`. |
| External links | `target="_blank"` with `rel="noopener noreferrer"`. |
| PHI | The app is not designed for patient data. Do not enter any in notes. |

## 11. Accessibility

- A skip link; landmarks for header, nav and main areas; `aria-expanded` and `aria-controls` on step toggles; `aria-current="page"` on the active phase tab; `role="progressbar"` with `aria-valuenow`.
- Interactive targets are at least 44 px (`.touch-target` is 48 px).
- Focus trap and restore in dialogs; Escape closes.
- Status is conveyed by text as well as color.
- Animations are disabled under `prefers-reduced-motion`.
- The browser's text zoom works. Text is never below 14 px.

## 12. Browser support

Current Chrome, Edge, Safari and Firefox. Requires `localStorage`, `Set`, `Map`, template literals, `Blob` downloads and `matchMedia`. Page numbers in print need Chrome or Edge. Real iOS and Android devices were **not** tested; the layout was verified in headless Chromium at 390 px and 1280 px.

## 13. Build, test and release

### 13.1 Build

There is no build step for the app. The only generated artifact is the inlined Tailwind CSS (see 3.3). Keep the header comment with the regeneration command.

### 13.2 Tests performed on v4.0

Automated runs with Playwright (Chromium) against the single file, plus PDF rasterization for print checks:

| Area | What was checked |
|---|---|
| Phone and desktop interaction | Opening steps, row taps, expand all, focus restore, next-up, phase pager, tab strip scrolling. |
| Filters and metrics | Services and counties, metric recalculation (for example 8G only shows 27 steps), draft vs applied state. |
| Dialogs and keyboard | Focus trap, Escape, backdrop click, restore focus. |
| State | Note escaping, malformed and partial imports, reset and reload. |
| Content | All 116 instruction dialogs open, have specific content, valid links (no bad hrefs, all with `noopener`) and review blocks. |
| Print | Both scopes, visible body in print is only the report, title restored, escaped markup. |
| Regional cards | Plan grouping by county, hub cards, statewide block, no old numbers. |
| Console | No page errors in any run. |

The test scripts were not committed. Recreate them from this list if needed.

### 13.3 Known limitations

- Content accuracy: researched but **not independently verified**. See the verification checklist.
- Contacts and policy details change. Plan and hub data carry an `asOf` date of 2026-10-18.
- The `.text-xs` override means "extra small" is 14 px everywhere.
- Print page numbers need Chrome or Edge.
- `localStorage` is per browser and per file location. Opening the file from a different path or browser starts empty. Use Export and Import to move progress.
- There is no undo for Reset (use Export first).

## 14. Maintenance guide

### 14.1 Update a task's instructions
Edit the entry in `SUBTASK_DETAILS_MAP` (key `step_<id>_sub_<index>`). Keep `sources` as indexes into `DETAIL_SOURCES`. Set `confidence` and `verify` honestly.

### 14.2 Add a source
Append the URL to the end of `DETAIL_SOURCES` and reference its new index. Never insert in the middle.

### 14.3 Add or change a step or task
Add to `MASTER_STEPS` with a unique `id`. **Appending a task to the middle of `subtasks` shifts later indexes**, which changes saved check keys and the details map keys. Append new tasks at the end of the list, or renumber the details map and accept that existing users' checks for that step shift. Update `timelineStartWeek` and `statutoryFees` so metrics stay correct.

### 14.4 Change a service scope
Edit the step's `services` array. For example, to show a step for peer support, add `'8G'`.

### 14.5 Update a plan or hub contact
Edit `PLANS` or `NC_REGIONS_DATA[n].rootsHubDetails`, and update `asOf`.

### 14.6 Move a county
Edit `COUNTY_PLAN` (plan assignment) and `NC_REGIONS_DATA` (region). Keep both consistent.

### 14.7 Change the saved-state format
If the shape changes in a way old saves can't handle, update `normalizeState` first. Changing `STORAGE_KEY` discards existing users' progress, so prefer a compatible change.

### 14.8 Release checklist
1. Regenerate Tailwind CSS if you added classes.
2. Open the file on a phone-width window and a desktop window. Check the console for errors.
3. Open a few instruction dialogs, including one Phase 6 task.
4. Select counties from all three plans and check the contacts panel.
5. Print both scopes and check the PDF.
6. Export, Reset, Import, and confirm progress returns.
7. Update the version badge and the README.

## 15. Function reference

| Group | Functions |
|---|---|
| Data helpers | `subtaskKey`, `countDoneSubtasks`, `getRegionColor`, `getPlanGroups`, `getActiveRegionIds`, `linkify`, `escapeHtml` |
| State | `defaultState`, `normalizeState`, `loadState`, `initState`, `saveState` |
| Filters | `toggleDropdown`, `buildCountyDropdown`, `syncCountyCheckboxes`, `setDraftCounties`, `onCountyCheckboxChangeDraft`, `toggleRegionCountiesDraft`, `selectAllCountiesDraft`, `clearCountyFilterDraft`, `filterCountiesInMenu`, `updateCountyDropdownLabel`, `toggleDraftServiceSelection`, `selectAllServicesDraft`, `resetServiceFilterDraft`, `syncDraftServiceCheckboxes`, `checkFilterChanges`, `updateSetupSummary`, `applyFilters`, `discardDraftFilters` |
| Rendering | `renderDashboard`, `renderProgress`, `renderPhaseTabs`, `renderCurrentPhaseCards`, `renderPhasePager`, `renderTimeline`, `updateRegionalContactsDisplay`, `planCardHtml`, `hubCardHtml`, `statewideHtml`, `intakeChips` |
| Navigation | `switchPhaseTab`, `goToStep`, `toggleStep`, `toggleAllSteps`, `updateExpandAllButton`, `findNextStep`, `updateNextUp` |
| Progress | `onSubtaskCheckboxToggled`, `onStepStatusChange`, `evaluateStepStatusFromSubtasks`, `focusCheckbox`, `updateMetrics`, `computeFeeTotals`, `computeSpan`, `updateFeeMetric`, `updateSpanMetric` |
| Dialogs | `openModal`, `closeModal`, `openSubtaskDetailModal`, `closeSubtaskModal`, `toggleSubtaskFromModal`, `renderDetailReview`, `openNotesModal`, `closeNotesModal`, `saveStepNotesFromModal`, `openPrintModal`, `closePrintModal`, `showToast` |
| Import and export | `exportStateJson`, `importStateJson`, `confirmResetModal` |
| Print | `startPrint`, `preparePrint`, `finishPrint`, `buildPrintReport` |

## 16. Related files

| File | Purpose |
|---|---|
| `nc_medicaid_bh_dashboard.html` | The app. |
| `README.md` | Overview and feature list. |
| `docs/QUICK_START.md` | End-user guide with screenshots. |
| `NC_Medicaid_Verification_Checklist.md` | Facts that need verification, with contacts and scripts. |
| `nc_medicaid_sources.csv` | Every source used in the app and the research. |
