# PRD: Reduce payment friction in onboarding

## 1) Context
We see a steep drop at the payment step. This is a classic fintech onboarding failure point.
It is also the closest step to revenue, so improvements show up quickly.

Synthetic funnel (per 10,000 visitors):
- Landing: 10,000
- Signup start: 6,200
- Email verified: 4,100
- Payment added: 2,300
- First order: 1,400

## 2) Problem statement
Users who already showed intent (verified email) abandon when asked to add a payment method.
This reduces first-order conversion and delays revenue.

## 3) Goals
- Increase payment-add rate (Verified -> Payment)
- Increase first-order conversion
- Reduce time-to-first-order

## 4) Non-goals
- Redesign the entire onboarding flow
- Change pricing or fee structure
- Build a fraud model (out of scope here, but we track guardrails)

## 5) Who is this for?
New users who completed signup and reached the payment step.

## 6) Hypotheses (root causes)
H1: Form friction is too high (fields, validation, UX)
H2: “Card not ready” moment (user wants to continue without payment)
H3: Trust anxiety (security, hidden fees, legitimacy)
H4: Payment failures with weak recovery (unclear error states, no retry guidance)

## 7) Proposed solution (v1 scope)
Bundle a small set of changes that target H1, H3, H4:

A) Reduce form friction
- fewer required fields where possible
- better defaults (country, billing)
- clearer progress state (you are 1 step away)

B) Add express pay (if supported)
- Apple Pay / Google Pay buttons above manual form
- fallback to manual entry

C) Add trust cues
- one line: why payment is needed now
- security cue: encrypted / secure processing
- clarify fees: “no hidden fees” (only if true)

D) Improve failure recovery
- map common errors to human messages
- allow immediate retry
- preserve entered data on failure

## 8) User stories
- As a new user, I want to add payment quickly so I can place my first order.
- As a new user, I want to trust the payment step so I feel safe entering my card.
- As a new user, if payment fails, I want a clear reason and an easy retry.

## 9) Requirements (acceptance criteria)
Friction:
- payment form loads under X seconds (set with eng)
- required fields reduced or justified
- error messages are specific and actionable

Trust cues:
- “why we ask” message displayed on payment page
- security cue visible without scrolling

Express pay:
- express pay shown when eligible device/browser supports it
- fallback to manual entry always available

Recovery:
- payment failure shows error category + next action
- retry does not wipe the form

## 10) Tracking and metrics
Event spec and metric definitions are in docs/METRICS.md.

We will measure:
- step conversion: Verified -> Payment added
- first-order conversion
- time-to-first-order
- payment errors and reasons

## 11) Experiment plan
A/B test details in docs/EXPERIMENT_PLAN.md.

## 12) Risks and tradeoffs
- Express pay may change fraud patterns, watch guardrails
- Trust copy must be accurate (legal/compliance)
- Faster flow can increase bad actors, watch fraud flags and chargebacks
- UX changes can shift support volume temporarily

## 13) Rollout plan
- Stage 1: internal / small % traffic to validate events and SRM check
- Stage 2: 10% -> 50% ramp with daily monitoring
- Stage 3: full rollout if metrics hit decision rule

## 14) Open questions
- Are we allowed to let users “skip payment for now”?
- Any compliance constraints on security copy?
- Most common payment failures today (need real logs to confirm)
