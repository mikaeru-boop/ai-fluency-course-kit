# Excerpt: business rules

*From the rules file of a weekly customer-reporting automation. These are the load-bearing
decisions; the automation reads them every run, so they are decided once and never
re-litigated.*

## Definitions

- **Shipment week** = the Monday-to-Sunday week of `pickup_date`, never the week the
  manifest row arrived. A late manifest otherwise lands last week's freight in this week's
  count (decided 2026-01-12).
- **Damage count** = claims in the claims table. NEVER use the `damage_flag` on the
  shipment table; drivers set it at the dock for scuffed packaging, and nobody clears it
  when no claim follows (added 2026-04-20, after a deck overstated damage by a third).
- **On-time** = delivered on or before `promised_date`. Weather holds are excluded from the
  on-time denominator (customer agreement, dated 2026-03-12), never from the issue counts.
- **Active lanes** = the lane table for the current quarter. Do NOT use the legacy
  per-shipment lane column; it has been stale since February.

## Exclusions (by design, dated decisions)

- One customer program is excluded from the on-time leaderboard (dated decision): after a
  warehouse closure it is a 30-shipment denominator, and its 95% rate is an artifact that
  distorts the chart. It stays on every other slide; the exclusion is one chart only.
- White-glove deliveries are scheduled outside the dispatch system (by design), so they are
  excluded from dispatch-coverage tables and from any chart where they read over 100%.

## Presentation

- The rejected-rows card counts known, deliberate holds ONLY. The cumulative rejects query
  is an ops-review upper bound, NEVER a deck number (the error table is append-only; manual
  fixes are invisible to it).
- No consignee names, addresses, or phone numbers on slides. Aggregate counts only.

*Notice the pattern: each rule exists because getting it wrong once cost someone an
afternoon. The dates mark decisions: "we discussed this, here is the answer, move on."*
