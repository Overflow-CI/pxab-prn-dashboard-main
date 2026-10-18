# PXAB PRN Dashboard

**NC Medicaid Behavioral Health Operations & Compliance Dashboard (Interactive HTML)**

A single-file, self-contained interactive dashboard to help providers and program leads plan, track, and complete the operational and regulatory steps needed to stand up behavioral health services (peer support, SAIOP, SACOT) in North Carolina.

## Quick start

- Open `nc_medicaid_bh_dashboard.html` in a web browser (double-click or File → Open). No server or build step required.
- The UI is fully client-side. Use the filters and tabs to explore phases, steps, timelines, and regional contacts.

## Files

- `nc_medicaid_bh_dashboard.html` — Main dashboard (standalone HTML).
- `README.md` — This Markdown README.

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
  - A dynamic grid shows LME/MCO tailored-plan contacts, NC ROOTS hub leads, and statewide Medicaid provider support (ombudsman, NCTracks, HIE desk) for the counties you selected.
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
  - Phase 6 covers **H.R. 1** (Public Law 119-21): six steps on eligibility checks and six-month renewals, the community engagement requirement and exemption documentation, coverage and cost-sharing changes, program-integrity screening and funding risk, and Rural Health Transformation (NC ROOTS) funding. The step text asks you to confirm every effective date against current NC Medicaid guidance.
  - Each step is a collapsible card showing its status and progress at a glance. On a phone only the first unfinished step starts open; on desktop all steps start open. Expand all / Collapse all is one tap.
  - Tap anywhere on a checklist row to check it off. Every row also has an **Instructions** button that opens that item's instructions, tips and contacts (under the task text on phones, beside it on wider screens).
  - Items without item-specific instructions show general guidance, and the dialog says so.

- Subtask detail modal
  - Opens as a bottom sheet on phones. It shows step-by-step instructions, executive tips (audit/licensing traps), and required authority/portals & contacts, with one button to mark the item complete or open again.
  - Phone numbers and email addresses are tap-to-call / tap-to-email links.

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
  - No separate data files are required; all core content is embedded in the HTML.

- Styling & build notes
  - The file includes a precompiled Tailwind v3.4 CSS block. If you add new Tailwind classes you will need to regenerate the CSS and paste it back into the file. The comment at the top of the HTML explains the regenerate command:
