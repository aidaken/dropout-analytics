# Experiment Plan: Payment friction reduction

## Experiment name
payment_friction_v1

## Objective
Increase Verified -> Payment conversion and lift first-order conversion, without breaking guardrails.

## Variants
- Control: current payment step
- Variant: friction reduction bundle (shorter form + trust cues + better recovery)
Optional second variant if you want:
- Variant B: same as A + express pay (Apple/Google)

Keep it simple if you can: 2 variants is easier to interpret.

## Eligibility
- New users who reach payment step after email verification
- Exclude: users with existing payment method

## Randomization
- Randomize at user_id
- Sticky assignment (user stays in same variant)

## Metrics
Primary:
- First-order conversion rate (within 7 days of signup)

Secondary:
- Payment-add rate (payment_method_added / email_verified)
- Time-to-first-order

Guardrails:
- Payment failure rate
- Fraud flags rate (if available)
- Chargebacks (if available)
- Support tickets tagged “payment”

## SRM check (must pass)
- Variant allocation close to expected split (ex: 50/50)
- If SRM fails, do not trust results. Fix assignment first.

## Duration
- Run until you hit a minimum sample size for stable read
- Practical default: 1 to 2 weeks, or until each variant has N users at payment_started

## Decision rule
Ship if:
- payment-add rate lifts by meaningful amount AND
- first-order conversion lifts AND
- guardrails do not worsen beyond agreed threshold

Example thresholds (adjust later with real data):
- +10% relative lift in payment-add rate
- no worse than +2% relative increase in payment failure rate
- no meaningful increase in fraud flags / chargebacks

## Segmentation read
After headline result, break down by:
- device_type
- country
- channel
- new vs returning sessions (if available)

