# PXAB PRN Dashboard

**NC Medicaid Behavioral Health Operations & Compliance Dashboard (Interactive HTML)**

A single-file, self-contained interactive dashboard to help providers and program leads plan, track, and complete the operational and regulatory steps needed to stand up behavioral health services (peer support, SAIOP, SACOT) in North Carolina.

## Quick start

- Open `nc_medicaid_bh_dashboard.html` in a web browser (double-click or File → Open). No server or build step required.
- The UI is fully client-side. Use the filters and tabs to explore phases, steps, timelines, and regional contacts.

## Files

- `nc_medicaid_bh_dashboard.html` — Main dashboard (standalone HTML).
- `readme.txt` — Original plain-text README (kept for history).
- `README.md` — This Markdown README.

## Features (what's in the app)

- Header actions
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

- Metrics panel
  - Overall Plan Progress: Percentage and progress bar showing how many steps/subtasks are complete.
  - Subtasks Completed: Count of completed subtasks and linkable instructions for each subtask.
  - Estimated Statutory Fees: Quick tally of statutory filing fees (does not include build-out or payroll costs).
  - Critical Path Span: Timeline total in weeks to provide a high-level schedule estimate.

- Multi-Phase Timeline (Gantt-style)
  - Shows overlapping multi-phase workstreams across weeks (default example up to 32 weeks). Bars are rendered client-side and scale horizontally.
  - Legend indicating Not Started, In Progress, Completed states.

- Phase tabs & Step cards
  - Tabs for Phase 1 → Phase N (rendered dynamically). Each phase contains step cards representing discrete regulatory or operational steps (Entity registration, EIN, NPI, Licensure, Staffing, Inspections, Application, Survey, etc.).
  - Each step card includes title, responsible party, estimated time, cost estimate, and quick actions (open subtask modal / mark complete).

- Subtask detail modal
  - When you open a step/subtask you get: step-by-step execution instructions, executive tips (audit/licensing traps), required authority/portals & contacts, and the ability to change task status (Open / Completed).
  - Save changes persist in the exported/imported JSON state.

- Notes modal
  - Add execution notes or internal ticket numbers for a step and save them as part of the dashboard state.

- Toast notifications
  - Non-blocking status updates and confirmations appear in the lower-right toast container.

- Accessibility & mobile-first design
  - Mobile-first font sizing baseline, minimum touch target sizing, keyboard and ARIA attributes for modals and role/aria labels are present. The UI is designed for use on tablets and phones as well as desktops.

- Data model & embedded content
  - The dashboard contains embedded region data (regional contacts and county lists) and a MASTER_STEPS array with detailed phases, steps, subtasks, statutory fees, and timelines.
  - No separate data files are required; all core content is embedded in the HTML.

- Styling & build notes
  - The file includes a precompiled Tailwind v3.4 CSS block. If you add new Tailwind classes you will need to regenerate the CSS and paste it back into the file. The comment at the top of the HTML explains the regenerate command:
