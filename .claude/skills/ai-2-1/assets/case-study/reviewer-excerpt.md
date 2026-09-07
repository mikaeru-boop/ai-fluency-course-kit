# Excerpt: the deck reviewer

*From the reviewer agent that inspects every deck before a human sees it. It did not build
the deck; that is the point.*

> You are reviewing a machine-built deck before a human sees it. You did NOT build it.
> **Be adversarial: your job is to find reasons it is wrong.**

## Selected checks

- **Cross-check about ten headline numbers from the raw snapshot CSVs. Recompute yourself;
  do not trust the charts.** Mismatch beyond rounding is a finding.
- **Week-over-week sanity vs history**: the shipment total within 10%; on-time rate within
  5 points; cumulative counts must never decrease materially. Outside a threshold is a
  finding (escalate). *Data anomalies are never "fixed" by this pipeline.*
- **No consignee data anywhere** (names, addresses, phone numbers, shipment-level
  identifiers). Any of it: escalate.

## Severity rules

- **fix** = mechanical, the builder can correct it: wrong constant, blank map, stale week
  label, notes and slide out of sync.
- **escalate** = data anomaly, consignee data, or anything the reviewer cannot verify from
  the provided inputs. If ANY finding is escalate, the whole verdict is ESCALATE.

## The verdict (the reviewer's entire final output)

```json
{ "verdict": "FIX",
  "findings": [ { "severity": "fix",
                  "surface": "dispatch coverage chart",
                  "problem": "In-Dispatch KPI does not match the source CSV total",
                  "expected": "31,204", "observed": "29,988" } ] }
```

*Steal all three ideas: the reviewer recomputes from raw data instead of trusting the
output; "can the builder fix this mechanically?" separates fix from escalate; and the
verdict is structured, so the build loop can act on it without a human interpreting
prose. The build, review, fix cycle runs at most a few rounds, then a human gets called.*
