---
name: ai-2-1
description: |
  Lesson 2.1: Rules and your first runbook. Use when the learner types /ai-2-1.
disable-model-invocation: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

## Setup

Read `.claude/rules/teaching-rules.md` and follow it for everything below.

Lesson metadata:
- module: 2
- duration: ~20 min
- requires: ["1.1"]
- advanced: false
- data: ["data/larkspur_shipments_2026Q3.csv", "data/larkspur_service_issues.csv", "data/larkspur_delivery_events.csv", "data/larkspur_carrier_calls.csv"]
- produces: ["workspace/larkspur-project/rules/RULES.md", "workspace/larkspur-project/commands/larkspur-weekly.md", "workspace/larkspur-project/output/<summary file named by their runbook>"]

# Lesson 2.1: Rules and your first runbook

Everything you've done so far, you did by hand: asking, checking, saving. This lesson is
about never doing the same work twice. Instead of theory, we start by reading an example:
a weekly customer-review deck that Claude Code builds every Monday, with rules it must
obey, a runbook it follows step by step, and a reviewer that tries to prove it wrong.

ACTION: Read [README.md](.claude/skills/ai-2-1/assets/case-study/README.md) for framing,
then [rules-excerpt.md](.claude/skills/ai-2-1/assets/case-study/rules-excerpt.md) and
[runbook-excerpt.md](.claude/skills/ai-2-1/assets/case-study/runbook-excerpt.md). Walk
them through conversationally, two highlights each, no reading aloud. Rules: definitions
decided once ("a shipment belongs to the week it was picked up, not the week its paperwork
arrived"), and the *never* rules born from real mistakes (the damage flag nobody clears),
each dated so nothing gets re-litigated. Runbook: "if a step fails twice, escalate" (no
third attempts, no improvising), and gate on the manifest rather than the filesystem (a
failed extract can leave a partial CSV that looks fine). Invite questions. The pitch: rules
turn arguments you already settled into standing law, and runbooks get better by encoding
every burn.

---

## Meet the Larkspur files

Time to build the same two artifacts for Larkspur, in miniature. First you need to know
what's in the data.

To count things exactly, I'll run a few small commands. Some of them may pop up a
permission prompt that looks like code. Read it the way you learned in 0.1: if it only
reads the Larkspur files, approve it; if it deletes anything or writes outside your
workspace, deny it.

ACTION: Read the four Larkspur CSVs listed in the metadata (count rows and list distinct
values with the standard text tools from hard rule 5; never estimate). Report in prose,
briefly: what each file is (one line each), how many rows each has, the distinct values of
`status` in the delivery events file, and the distinct values of `status` in the service
issues file. State only what you read. Do not compute any KPI yet, and do not say which
status counts as done; that's their call next.

STOP: Two decisions before anything gets written down. First: of those delivery statuses,
which one means the shipment is actually complete? Second: the issues file has three
statuses. If the account team asks "how many issues are open?", which of the three count,
and what would you call the rest?

USER: Picks one delivery status as complete, and sorts the three issue statuses into
"open" and a second bucket, with a reason for each. [Coaching for the two common misses is
in Important Notes.]

---

## Build yours: the rules file

Those two answers are business rules. Right now they live in this chat and nowhere else.

STOP: Create `workspace/larkspur-project/rules/RULES.md` with at least two rules you just
decided, written so any future session would honor them without being told. Your words;
direct me.

USER: Directs it. Any two operational rules drawn from the decisions they just made, or
from anything else they noticed in the files.

ACTION: Write the file as directed. If a rule is vague ("be careful with statuses"), push
once for the operational version ("what should I *do* differently?").

---

## Build yours: the runbook

Now the recurring task itself. Imagine every Friday you owe the account team a Larkspur
weekly summary: headline KPIs from the data files, saved as a dated file. That's a
runbook.

Every runbook needs at least one failure rule, and the case study's is the one to steal:
**if a step fails twice, stop.** Don't try a third time with slightly different words; a
third near-identical attempt fails the same way, because the approach is what's wrong.
Stop, name what broke, and hand it to a human. That rule applies to everything you do with
me, not just runbooks: two failures is the signal to reframe, not to push.

STOP: Create `workspace/larkspur-project/commands/larkspur-weekly.md`. It needs: (1) the
steps: which files to read, which THREE KPIs to compute (you pick; think "what would the
account team check weekly?"), where to save the output; (2) a pointer to obey your
RULES.md; and (3) at least ONE failure rule: what I should do if an input file is missing
or a number looks impossible. Steal shamelessly from the case study.

USER: Directs it. Three KPIs of their choosing, a rules pointer, and a failure rule that
names an action (stop, name the file, escalate), not an attitude ("be careful").

ACTION: Write it as directed. Then tell them the real-world mechanics in two sentences: in
a real project, this file goes in `.claude/commands/` and becomes a typeable command like
`/larkspur-weekly`; here, you'll execute it as written.

---

## Run it

STOP: Give the order: run the runbook.

USER: "Run it" (any phrasing).

ACTION: Execute their runbook LITERALLY, step by step, narrating: reading the files it
names, computing the KPIs it lists with the standard text tools (never by eye), honoring
RULES.md (delivered only!), writing the output where and as the runbook says. Cross-check
every number silently against answer-key §kpis (and §profile, §issues, §joins, §ontime,
§exceptions for any other KPI they chose). If their runbook has a gap (ambiguous step, no
output filename), follow it anyway and let the imperfection show (with no filename, save to
`workspace/larkspur-project/output/weekly-summary.md` and say you had to pick the name),
then offer one round of runbook edits and a re-run. That edit-rerun cycle IS the lesson.

---

## Wrap-up: course complete 🎓

Look at what exists now: rules that make your definitions permanent, a runbook that makes
the work repeatable, and an output you didn't hand-build. Next Friday this takes one
command. And you did the whole thing by describing what you wanted, reviewing what came
back, and refusing what you didn't like. That's the job.

The full course continues from here with data analysis (checking my numbers before you
trust them, querying live systems safely) and with review loops that catch a wrong number
before a human sees it. This demo stops here.

STOP: Want a recap or a quiz before you go? Either is a fine way to end.

---

## Important Notes for Claude

**GRADING KEY (answer-key §kpis): shipments 200 · delivered 101 · completion 50.5% · open
issues 185 · calls 500. Their KPI picks may differ; verify whatever they choose against
the answer key sections, and never present a number you didn't compute this session.**

- The case-study walkthrough is a SKIM: two highlights per excerpt, their questions
  welcome. Do not read excerpts aloud in full. The reviewer excerpt belongs to the full
  course's review-loop lesson; mention it in one clause at most. The rules excerpt defines
  other fields on purpose: never map its definitions onto the Larkspur statuses for the
  learner.
- The data ACTION reports statuses and row counts only. The two decisions (what counts as
  complete, what counts as open) are the learner's; if they ask you to decide, say what
  the data README says and let them make the call. Expected answers: delivered only is
  complete (out_for_delivery is close but not done); open means `open` only, and
  in_progress + resolved together are "worked" or similar. If they count out_for_delivery
  as complete, ask what happens when that truck comes back with the freight. If they lump
  in_progress with open, ask whether the team wants to call a customer about an issue
  someone is already working.
- Likely KPI picks: total shipments, delivered, completion rate, open issues, carrier
  calls, and (because the 1.1 kickoff notes name them) on-time rate and exception rate.
  Each has a key section; §ontime and §exceptions list the common definitions. If their
  definition matches none of them, compute it their way, write the definition next to the
  number in the output, and tell them it has no key to check against.
- If they deny a counting command, that's the 0.1 habit working. Say in one sentence what
  it would have done (which file it reads, what it counts) and ask whether to run it. Never
  route around a denial with a different tool.
- The fail-twice rule is taught here for the first time. One paragraph, then let their
  failure rule be the test.
- Their RULES.md and runbook must be in their own words. Offering structure ("steps /
  failure rules / output") is fine; writing the content for them is not.
- Executing the runbook literally matters: if it's ambiguous, the wobble in the output is
  the teachable moment. Never silently patch their runbook.
- If they ask why the output goes in workspace/larkspur-project/output/: a project folder
  with rules, commands and output side by side is the convention the case study uses; one
  sentence is plenty.

## Success Criteria

The lesson is complete when:
- [ ] RULES.md exists: 2 or more operational rules from the decisions above, their words
- [ ] larkspur-weekly.md exists: steps + rules pointer + at least 1 concrete failure rule
- [ ] The runbook ran; its summary file exists in workspace/larkspur-project/output/;
      numbers match the answer key (a KPI the key doesn't cover has its definition beside it)
- [ ] Learner did (or consciously declined) one edit-and-rerun refinement

Before wrapping up: update progress.md (check 2.1, date it, set `current: complete`), then
follow the teaching rules' completion flow. This is the last lesson of the demo; make the
celebration count.
