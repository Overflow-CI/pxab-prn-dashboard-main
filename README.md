# PXAB PRN Dashboard

**NC Medicaid Behavioral Health Operations & Compliance Dashboard (Interactive HTML)**

A single-file, self-contained interactive dashboard to help providers and program leads plan, track, and complete the operational and regulatory steps needed to stand up behavioral health services (peer support, SAIOP, SACOT) in North Carolina.

## Quick start

- **Quick start guide (illustrated):** [QUICK_START_GUIDE_URL](QUICK_START_GUIDE_URL) <!-- PLACEHOLDER: replace both occurrences of QUICK_START_GUIDE_URL with the published URL of the quick start guide. The source is docs/QUICK_START.md. -->
- Open `nc_medicaid_bh_dashboard.html` in a web browser (double-click or File → Open). No server or build step required.
- The UI is fully client-side. Use the filters and tabs to explore phases, steps, timelines, and regional contacts.

## Files

- `nc_medicaid_bh_dashboard.html` — Main dashboard (standalone HTML).
- `README.md` — This Markdown README.
- `docs/QUICK_START.md` — Illustrated quick start guide for users (screenshots in `docs/images/`).
- `docs/SPECIFICATION.md` — Full technical specification of the app.
- `NC_Medicaid_Verification_Checklist.md` — Facts to verify, who to contact and what to say.
- `nc_medicaid_sources.csv` — Every source used in the app and the research.

## Features (what's in the app)

- Header actions
  - Print: Open the print options and save your plan as a PDF (see "Printable plan" below).
  - Export: Download the current dashboard state as a JSON file so you can save or share your progress.
  - Import: Re-load a previously exported JSON state to restore filters, progress, and notes.
  - Reset: Clear the active dashboard state and return to the initial/default configuration.

- Geographic Footprint (County selector)
  - Multi-select county dropdown grouped by NC Medicaid regions. Searchable and supports "Select All" / "Clear" shortcuts.
  - Selected counties render as pills and drive which regional contacts and tailored-plan details are shown.

- Clinical Coverage Policy (CCP) Multi-select
  - Multi-select control for the target services: CCP 8G (Peer Support), CCP 8A-12 (SAIOP), CCP 8A-13 (SACOT).
  - Each CCP option includes a short summary (billing code, supervision expectations, typical hours) to help you choose.
  - Quick actions: Select All / Reset (defaults to 8G preset) are provided.

- Filters & Apply
  - Draft filter model: you can make filter choices and either discard or apply them.
  - Apply filters updates the visible steps, timeline, metrics, and regional contacts based on selected counties and services.

- Regional contacts & governance cards
  - Tailored Plans are matched by county (Alliance Health, Trillium, Vaya Partners), with provider lines, UM contacts, payer IDs and whether each plan is taking SAIOP, SACOT or peer support applications. NC ROOTS hub leads are shown by Medicaid region, followed by statewide support (Provider Ombudsman, Contact Center, NCTracks, HIEA). Contacts were checked against public pages on 2026-10-18 and cite what was not confirmed.
  - Contact cards include phone, email, portal URLs, and quick references.

- Overview card
  - Overall progress (percentage, bar, steps done, items checked) and a "Next up" button that jumps to the first unfinished step.

- Fees & timeline panel
  - Estimated Statutory Fees and Critical Path Span are calculated from the active steps' data (`statutoryFees` and the scheduled weeks), not typed in.

- Multi-Phase Timeline (Gantt-style)
  - Shows overlapping multi-phase workstreams across weeks (default example up to 32 weeks). Bars are rendered client-side and scale horizontally.
  - Legend indicating Not Started, In Progress, Completed states.

- Phase tabs & Step cards
  - Pinned phase tabs with per-phase progress, plus previous/next phase buttons under the list.
  - Phase 6 covers **H.R. 1** (Public Law 119-21): six steps on eligibility checks and six-month renewals, the community engagement requirement and exemption documentation, coverage and cost-sharing changes, program-integrity screening and funding risk, and Rural Health Transformation (NC ROOTS) funding. Dates and requirements were researched in October 2026; NC's work requirement policy and attestation form were still drafts open for comment until Nov 5, 2026, so recheck them.
  - Each step is a collapsible card showing its status and progress at a glance. On a phone only the first unfinished step starts open; on desktop all steps start open. Expand all / Collapse all is one tap.
  - Tap anywhere on a checklist row to check it off. Every row also has an **Instructions** button that opens that item's instructions, tips and contacts (under the task text on phones, beside it on wider screens).

- Subtask detail modal
  - Opens as a bottom sheet on phones. It shows step-by-step instructions, executive tips (audit/licensing traps), and required authority/portals & contacts, with one button to mark the item complete or open again.
  - Phone numbers, email addresses and web addresses are tappable links.
  - Each researched entry ends with a **Check before relying on this** section: a confidence rating (high, medium or low), what a person must still verify, and links to the sources it used. Phase 6 entries also say whether the item is required, expected from NC, or good practice, and the date it applies from. Entries for Steps 1 to 3 came with the original file and are labeled "Not yet checked against sources".

- Printable plan (Print button)
  - Builds a clean, black-and-white-friendly report from your current state: summary and per-phase progress, every step with its status, checked and unchecked items (drawn as boxes), your notes, cost, owner, dependencies and source URLs.
  - Choose "Entire plan" or "Unfinished work only", and optionally include the regional contacts for your counties.
  - Use your browser's print window and choose Save as PDF (on a phone: Print, then Save as PDF or Share). Ctrl/Cmd+P prints the same report.

- Notes modal
  - Add execution notes or internal ticket numbers for a step and save them as part of the dashboard state.

- Toast notifications
  - Non-blocking status updates and confirmations appear in the toast container (full width on phones, lower right on larger screens).

- Mobile-first design & accessibility
  - Layout is built for a phone first: compact header, progress and "Next up" at the top, reference panels (Setup, Regional contacts, Fees & timeline) folded into one-line summaries, and dialogs that slide up as bottom sheets.
  - 44px+ touch targets, 16px form fields (no iOS zoom on focus), larger secondary text, and no horizontal scrolling.
  - Keyboard and screen-reader support: focus is kept inside dialogs and returned afterwards, Escape closes them, controls are labeled, and there is a skip link. Animations are disabled for users who prefer reduced motion.

- Data model & embedded content
  - The dashboard contains embedded region data (regional contacts and county lists) and a MASTER_STEPS array with detailed phases, steps, subtasks, statutory fees, and timelines.
  - Every one of the 116 tasks has its own instructions, tips and contacts. They come from an October 2026 research pass against NC Medicaid, NCTracks, DHSR, NC legislature and federal sources, and keep their source links, confidence rating and verify notes.
  - No separate data files are required; all core content is embedded in the HTML (about 440 KB).

- Styling & build notes
  - The file includes a precompiled Tailwind v3.4 CSS block. If you add new Tailwind classes you will need to regenerate the CSS and paste it back into the file. The comment at the top of the HTML explains the regenerate command:
