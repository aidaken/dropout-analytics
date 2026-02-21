# Exec Summary: Payment step drop-off (onboarding)

## Goal
Increase first-order conversion by reducing the biggest revenue-proximate drop in onboarding.

## Data note
We use a synthetic funnel because Northwind/Chinook do not include pre-purchase users.
Those datasets mostly contain customers who already bought, so acquisition funnels go flat.

## What the funnel says (per 10,000 visitors)
- First order conversion: 14% (1,400 users)
- Biggest volume leak: Landing -> Signup start (3,800 lost, 38%)
- Most revenue-proximate leak: Verified email -> Payment method added (1,800 lost, 44%)

## Main hypothesis
The payment add step fails for three common reasons:
1) friction: too many fields, unclear UX
2) context: user does not have card ready, wants to browse first
3) trust: last-second doubt (fees, security, legitimacy)

## Recommendation
Ship a focused “payment friction reduction” bundle and validate via A/B test.

Proposed changes:
- shorter form + better defaults
- express pay (Apple Pay / Google Pay) if available
- trust cues: “why we ask”, security line, no hidden fees note
- cleaner errors and retry path

## Success metrics
Primary: first-order conversion rate  
Secondary: payment-add rate, time-to-first-order  
Guardrails: payment failure rate, fraud flags, chargebacks, support tickets

## Impact math (from script outputs, consistent scenarios)
Baseline:
- Verified email: 4,100
- Payment added: 2,300 (56.1% of verified)
- First orders: 1,400 (60.9% of payment added)

Scenario A (moderate): payment-add improves 56.1% -> 68% (+12pp)
- Payment added: ~2,788
- First orders: 1,400 -> 1,697 (+297)
- At $50 AOV: +$14,852 per 10,000 visitors (before retention)

Scenario B (aggressive): payment-add improves 56.1% -> 71% (+15pp)
- Payment added: ~2,911
- First orders: 1,400 -> 1,772 (+372)
- At $50 AOV: +$18,596 per 10,000 visitors (before retention)

Note: 900 users currently drop between Payment added -> First order (60.9% completion).
Recovering that requires improving purchase completion, not just payment-add.

Therefore, we should prioritize payment friction first because it is the biggest leak at the money step,
then run a landing page trust test in parallel (largest volume leak).
