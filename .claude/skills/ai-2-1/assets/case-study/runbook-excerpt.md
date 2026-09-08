# Excerpt: the weekly build runbook

*From the command that builds the deck. A scheduled job pulls the data and pings the owner;
a supervised Claude session then runs this checklist. Note who is in control: "there is a
human (you) in the loop, so ask when a genuine judgment call comes up rather than
guessing."*

**The prime directive:** *If a step fails twice, skip to FINALIZE with kind=escalated and
describe what broke.* No third attempts, no improvising.

## 0. Load inputs

- Snapshot = the newest data-pull folder. Read its manifest file.
- If the manifest says the core pull did not complete: FINALIZE immediately (pull_failed).
- **GATE ON THE MANIFEST, NOT THE FILESYSTEM**: use an extract's CSV only if its manifest
  entry says `ok: true`. A failed extract can leave a partial CSV on disk that *looks* fine.

## 1. Refresh the data pull (elided)

## 2. Inject data constants (numbers only, never touch layout)

HARD RULES (added after the first dry run improvised):

- NEVER restructure a chart's rows or columns: no invented roll-up rows, no added or
  dropped lanes beyond the data refresh itself. If the data genuinely does not fit the
  existing structure, FINALIZE kind=escalated.
- NEVER write interpretive claims about data anomalies into chart files ("the dispatch
  queue was purged"). Neutral flags go in speaker notes; hypotheses go in the escalation
  message.
- KNOWN SIGNATURE: dispatch coverage collapsing wholesale (many terminals at 0% at once)
  while the shipment total is stable = the dispatch data mirror is probably mid-reload.
  Escalate with that hypothesis named; do not present those numbers as fact.

*Three things to steal: gate on ground truth (the manifest), fail loudly and specifically
(escalate with a description, never a guess), and when reality repeats a failure pattern,
write the pattern down so the automation recognizes it next time.*
