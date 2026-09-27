# Authoring a course for a company

This is the process behind the demo in this repository, written so a company can see what
an engagement involves and a practitioner can repeat it.

## 1. Discovery

Sit with the team that will learn. Collect three things: the recurring tasks they do by
hand (weekly summaries, reconciling a customer file, turning call notes into action items),
the files they actually receive (a manifest, an inbox of messy notes, a status export), and
the vocabulary they use for them. Ask which data classes must never enter a training
folder: personal data, payment data, health data, anything under contract. Pick two or
three pilot learners who are not technical.

## 2. Domain model

Invent a customer. Design four or five files that mirror the real ones, each with the one
business rule that matters most: which status means done, which flag lies, which count the
boss asks for. In the demo: a shipment manifest, service issues, delivery events (only
`delivered` counts), carrier calls, and a dirty second manifest with a load log. Real work
is full of rows that look fine and are not; the data should be too.

## 3. Synthetic data

One script generates every file and the answer key from the same rows, with a fixed seed,
so a run today matches a run next year. `--check` re-derives everything and diffs it
against disk; run it before every release. Make fake data obvious at a glance: IDs that
start with 99, surnames from the NATO alphabet, 555 phone numbers, streets named "Example
Ave", "Sample St", or "Placeholder Rd". Every number a lesson expects comes from the generated key, never from a person's
memory. See `tools/make_synthetic_data.py`; its docstring says which parts to change.

## 4. Lessons

Each lesson is a Claude Code skill, invoked by a command like `/ai-1-1`, written from
`tutor/lesson-template.md`. The template's stage directions (STOP, USER, ACTION, bracketed
conditions) tell the tutor when to wait, what an acceptable answer looks like, and what it
does itself. Grading keys live only in the "Important Notes for Claude" section, never
next to the question. One deliverable per lesson. Teach each concept once and refer back
in a clause. The learner writes every prompt in their own words; the tutor offers a hint,
then a smaller step, then the exact prompt only if asked.

## 5. Sensitive data and tool boundaries

`.claude/rules/teaching-rules.md` carries the tutor's hard rules. Hard rule 2 is the
sensitive-data rule and has a customize marker: name the data classes and regulations that
bind the company, and what the tutor says when a learner pastes something real.

The hard rules are instructions, so the enforced boundary lives in `.claude/settings.json`.
This demo denies every MCP tool (`"deny": ["mcp__*"]`), which keeps live systems out of the
tutor's reach whatever connectors the learner has installed, and puts an `ask` rule on
`rm` so a deletion always prompts. A lesson's `allowed-tools` frontmatter is not a
boundary: it skips the prompt for the listed tools during the turn that starts the lesson,
and restricts nothing. Never list MCP tools there.

A lesson that touches a live system (a database through an MCP server, for example) names
its tools under `live_tools:` in its Setup metadata and opens with a prerequisite check and
a data gate: the learner restates the aggregate-only rule before any live query. If the
check fails, the lesson stops and offers a synthetic fallback. A deny rule outranks every
allow rule, so a course with such a lesson replaces the blanket deny with an `ask` rule on
that server's tools (`mcp__<server>__*`), which makes every query show the learner a
prompt, and keeps deny rules for any other server it knows about.

## 6. Pilot and smoke test

Pilot with the learners from discovery and read the tutor's notes in their progress files.
Then run the smoke test in `MAINTENANCE.md`: fresh folder, no progress file, a novice
roleplay, eight checks. A scripted pass is cheap: copy the packaged folder to a scratch
directory and drive lessons with `claude -p` in a loop, reading the transcript afterward.
It never shows a permission prompt, so the prompt check always needs one interactive run.
Turn each defect a pilot finds into one sentence in teaching-rules.md, so the fix holds for
every lesson.

## 7. Trim and release

After the pilot, review every lesson for redundancy: concepts taught twice, stops spent on
mechanics the learner already knows, verbal quizzes that a later artifact tests anyway.
Bump `course_version` in CLAUDE.md, tag the release, and ship either a git clone or a zip
with the learner state removed (see "Packaging" in MAINTENANCE.md).
