# Case study: a weekly reporting automation

These three excerpts describe a **weekly customer-review deck** built by Claude Code: data
pulled, charts refreshed, numbers validated, and the result adversarially reviewed before a
human opens it. The automation shown here is a fictional composite written for this
course. Its structure and its rules are the kind that real automations of this shape
accumulate after a few months of weekly runs.

What to notice:

- **rules-excerpt.md**: business definitions written down ONCE, so they are never
  re-litigated. Note how specific they are, and how often they say *never*.
- **runbook-excerpt.md**: the weekly build as a step-by-step command. Note the failure
  handling: what happens when a step fails twice, and the rules added *after* the
  automation improvised on its first dry run.
- **reviewer-excerpt.md**: a separate agent whose only job is to prove the deck wrong
  before a human sees it. It recomputes numbers from raw data rather than trusting the
  charts, and it distinguishes "fix" from "escalate".

The first two rungs of that ladder (rules and a runbook) are what you build for Larkspur
in this lesson, in miniature. The review loop comes later in the full course.
