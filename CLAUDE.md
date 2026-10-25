# CLAUDE.md

Project memory for Claude Code. This file is loaded automatically at the start of every session in this repository.

## What this repo is

The **NC Medicaid BH Operations Navigator** (v4.0): one self-contained HTML file, `nc_medicaid_bh_dashboard.html`, that guides a new North Carolina provider through starting to bill NC Medicaid for **Peer Support (CCP 8G), SAIOP (CCP 8A-12) and SACOT (CCP 8A-13)**. It has 31 steps and 116 tasks in 6 phases, with researched instructions, sources and confidence ratings for each task.

Repository: `Overflow-CI/pxab-prn-dashboard-main` (default branch `master`). It was first `hello-world`, then `tasha-a-coder/pxab-prn-dashboard-main`. Old addresses redirect.

## Read these first, in this order

1. `handoff/HANDOFF.md`: everything the owner asked for (verbatim), what is done, what is open, deadlines, how to test.
2. `docs/SPECIFICATION.md`: technical specification of the app.
3. `NC_Medicaid_Verification_Checklist.md`: facts that still need verifying, with contacts and scripts, and an answer log.
4. `handoff/conversation_context.json`: the same context in structured form.
5. `handoff/NEXT_SESSION_PROMPT.md`: the prompt the owner pastes to start a session, and what to do after reading.

Only open `handoff/conversation_transcript.json` (the whole previous conversation) or `handoff/inputs/` (the research files the owner supplied) when you need exact earlier wording or the raw research. `nc_medicaid_sources.csv` lists every source used.

## Rules (set by the owner)

- The app stays **one self-contained HTML file**.
- Do not change the localStorage key `NC_MEDICAID_NAVIGATOR_FULL_STATE_V3`.
- New Tailwind classes need the inlined CSS rebuilt: `cd handoff/tools && npm install && python3 rebuild.py`.
- When the owner answers the verification checklist, update **the app and the checklist together in one pull request, in the same session**.
- Never mark a fact as verified unless an official source was actually opened. Write "NOT VERIFIED" and say who to ask.
- Do not open or merge a pull request, or force-push, unless the owner asks. Merge pull requests with a merge commit (not squash) when the branch will be reused, so no force-push is needed.
- Keep the quick start guide (`docs/QUICK_START.md`) and the specification in step with any change to the app.
- Do not put patient information or personal contact details of the owner in the repo.

## Run and test

- Open the app: open `nc_medicaid_bh_dashboard.html` in a browser. No server or build.
- Tests (Playwright with Chromium): `cd handoff/tools && npm install && node t_main.js` (also `t_desk.js`, `t_p6.js`, `t_instr.js`, `t_print.js`, `t_details.js`, `t_plans.js`). Each ends with `errors []`. Set `CHROMIUM=/path/to/chromium` if Chromium is not at `/opt/pw-browsers/chromium`.
- Expected counts: 31 steps, 116 tasks, 242 distinct source URLs, schedule 31 weeks, fees $1,358 to $1,705, 27 steps with peer support only.

## Current state (as of 2026-10-22)

- Everything built so far is merged into `master` (PRs #1, #2, #3, #5, #6). No pull request is open.
- Research content is **unverified** (the build sandbox could not reach NC government sites). The verification checklist is the plan to fix that.
- **Time-sensitive:** NC medical frailty policy public comment closes 2026-11-05; Rural Health Innovation Fund application is due 2026-11-16, 11:59 p.m.
- The owner has not yet answered the checklist questions. Open decisions are listed in `handoff/HANDOFF.md` section 6.
- `README.md` has a placeholder `QUICK_START_GUIDE_URL` (twice, one line) to replace once the owner says where the guide is published.
