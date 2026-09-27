# Lesson template: AI Fluency @ Tillerman Freight

Copy this structure for every lesson. File location: `.claude/skills/ai-<module>-<n>/SKILL.md`.
Lesson-specific fixtures (if any) go in that skill's `assets/` folder; shared datasets live in
`data/` at the repo root.

---

```markdown
---
name: ai-M-N
description: |
  Lesson M.N: <Title>. Use when the learner types /ai-M-N.
disable-model-invocation: true
allowed-tools:   # no prompt for these during the lesson's first turn only; restricts nothing
  - Read
  - Write        # only if the lesson's first turn writes (e.g. creating progress.md)
  # never list MCP tools here; see AUTHORING.md section 5
---

## Setup

Read `.claude/rules/teaching-rules.md` and follow it for everything below.

Lesson metadata:
- module: M
- duration: ~NN min
- requires: ["M.N-1"]          # lesson ids that should be checked off in progress.md
- advanced: false              # true → run the Prerequisite check section before teaching
- data: []                     # files in data/ this lesson reads
- produces: []                 # workspace artifacts the learner will create
- live_tools: []               # MCP tools; only a live-system lesson has any

# Lesson M.N: <Title>

<Opening: 2–4 sentences of why this matters at this company. Warm, concrete.>

STOP: <first engagement question>

USER: <expected shape of reply>

---

## <Section name>

<Teach one idea. Keep sections short: one concept, one interaction.>

<Exercise steps state the GOAL of the prompt the learner should write in their own words.
Never hand them copy-paste prompts, except in Module 0, where training wheels are allowed.>

ACTION: <anything the tutor does itself (creating a fixture, listing a folder)>

STOP: <wait point>

USER: <expected reply>

---

## Wrap-up

<1–2 sentences of what they can now do. Connect to their real job.>

**Next up:** <one line teasing the next lesson.>

STOP: Ready for M.N+1? Start a fresh chat and type /ai-M-N+1, or say "keep going" to
continue here.

---

## Important Notes for Claude

- <Common mistakes and how to respond>
- <Hint ladder specifics for the exercise: hint → smaller step → exact prompt>
- <If numbers are involved: which answer-key section to check>

## Success Criteria

The lesson is complete when:
- [ ] <verifiable artifact exists / numbers match the relevant answer-key section
      (§profile, §issues, ...)>
- [ ] <learner explained X in their own words>

Before wrapping up: update progress.md (check the box, date it, move `current:`), then follow
the teaching rules' completion flow (congratulate, offer recap/quiz/break/next lesson).
```

---

## Authoring rules

- **Grading keys and expected answers live ONLY in "Important Notes for Claude"**: never
  inline in the lesson body next to the question. Inline answers are one careless paste away
  from the learner's screen; structurally separated ones aren't. `USER:` lines describe the
  *shape* of an acceptable reply, not a scripted answer to reveal.
- Checkpoints are verifiable artifacts or explanations, never "learner feels comfortable."
- **Teach each concept once.** Later lessons reference established concepts in one clause
  ("the usual fake data"), no re-explanations, and no checkpoints that force the tutor to
  re-quiz something a previous lesson already verified.
- One deliverable per lesson, max. A config file that changes how deliverables are
  produced (a CLAUDE.md) doesn't count against it.
- After Module 0, never spend a STOP on "ask me to show you X". The learner learned that
  mechanic in 0.1; from 1.1 on, inputs are presented as ACTIONs and the STOPs go to
  decisions, prompts, and reviews.
- A verbal "in your own words" checkpoint only when no later lesson tests the concept
  operationally. If a later artifact would reveal whether they understood it (a RULES.md
  line, a failure rule, a done-criteria list), let the artifact be the test.
- `allowed-tools` is a convenience, not a boundary: it skips prompts for the listed tools
  during the turn that starts the lesson and restricts nothing. The boundary is
  `permissions.deny` in `.claude/settings.json` (this demo denies every MCP tool). MCP
  tools appear ONLY under `live_tools:` in a live-system lesson (none in this demo), which
  must open with a prerequisite check and a data gate (the learner restates the
  aggregate-only rule before any live query).
- Advanced lessons fail closed: if the prerequisite check fails, stop teaching and give the
  human next step ("message the course owner"), then offer the synthetic-data fallback
  lesson instead.
- Describe UI conceptually, never exact button text or screenshots: survives Claude Code
  releases.
- No real customer names, no real customer or shipment data, ever, including in examples
  you improvise.
