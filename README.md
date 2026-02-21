# Dropout Analytics: Payment Friction as a Revenue Leak

## Problem Summary

We discovered a significant revenue leak in the onboarding funnel at the most revenue-proximate moment: when users are asked to add a payment method. Of 10,000 landing page visitors, only 1,400 (14%) complete a first order.

The leak: 4,100 users verify their email, but only 2,300 add a payment method. We're losing 1,800 users (44% drop) when asked to provide payment—before they even reach the checkout step. This is the biggest drop at the "money moment" in fintech onboarding.

## The Funnel

![Funnel Chart](assets/funnel_chart.png)

## Key Numbers

| Metric | Value |
|--------|-------|
| Landing page visitors | 10,000 |
| First-order conversion rate | 14% |
| Email verified (reach payment prompt) | 4,100 |
| Payment method added | 2,300 |
| Payment add rate (Verified → Payment) | 56.1% |
| Users lost at payment add step | 1,800 |
| First-order revenue per 10,000 visitors (at $50 AOV) | $70,000 |

## Root Causes (Hypothesized)

Based on common fintech onboarding friction points at the payment add step:
- Form friction: too many fields, unclear required vs optional, validation feels slow
- Card not ready: user hasn’t brought a card to their computer, wants to “look around” first
- Missing payment methods: no Apple Pay / Google Pay / alternatives
- Trust anxiety: no reassurance on data security, no “why we ask”, fear of hidden fees
- Payment failures: unclear error messages, no retry path, form resets on failure

## Our Approach

We will run a focused payment add step friction reduction experiment that combines:
1. Form simplification (fewer fields, smart defaults, better validation)
2. Alternative payment methods (Apple Pay, Google Pay for quick add)
3. Trust reinforcement (security badge, “why we ask”, clear messaging on fees)
4. Better error recovery (clear error messages, easy retry, form preservation)

Expected impact (from payment-add uplift only), using the baseline purchase completion rate (60.9%):
- Scenario A: payment-add improves 56.1% -> 68% (+12pp)
  - First orders: 1,400 -> 1,697 (+297)
  - Revenue: +$14,852 per 10,000 visitors (at $50 AOV)

- Scenario B: payment-add improves 56.1% -> 71% (+15pp)
  - First orders: 1,400 -> 1,772 (+372)
  - Revenue: +$18,596 per 10,000 visitors (at $50 AOV)

Note: 900 users currently drop between Payment added -> First order (60.9% completion). Recovering that requires improving purchase completion, not just payment-add.

## Decision

Ship this behind an A/B test. The data is clear: payment friction is our most revenue-proximate leak. The fix is measurable and low-risk, and the revenue upside justifies engineering investment.

Weekly metrics to watch: first-order conversion rate and time-to-first-order (with guardrails on payment failures, fraud flags, and chargebacks).

---

Full analysis: See `docs/EXEC_SUMMARY.md`, `docs/PRD.md`, `docs/METRICS.md`, `docs/EXPERIMENT_PLAN.md`, and `docs/ROADMAP_DECISION.md`.

---

## Files

| File | What it does |
|------|--------------|
| `README.md` | Project overview + key funnel numbers + decision |
| `docs/EXEC_SUMMARY.md` | One-page summary (problem → evidence → decision → impact) |
| `docs/PRD.md` | PRD with scope, user stories, acceptance criteria, risks |
| `docs/METRICS.md` | Event spec + metric definitions + guardrails |
| `docs/EXPERIMENT_PLAN.md` | A/B test plan + success criteria + segmentation |
| `docs/ROADMAP_DECISION.md` | Now / next / later roadmap with rationale |
| `docs/DECK_OUTLINE.md` | 10-slide outline version of the story |
| `assets/funnel_steps.csv` | Synthetic funnel step table |
| `assets/funnel_chart.png` | Funnel chart used as evidence in README |
| `src/sanity_check_funnel.py` | Prints step rates + drop counts (sanity check) |
| `src/calc_impact_scenarios.py` | Reproduces Scenario A/B impact math + exports outputs |
| `outputs/impact_scenarios.csv` | Scenario table (baseline vs uplift scenarios) |
| `outputs/impact_first_orders.png` | Chart: first orders under each scenario |
| `sql/daily_funnel_counts_template.sql` | Template: daily funnel counts from real event logs |
| `sql/segment_step_rates_template.sql` | Template: step conversion by country/device/channel |

---
Aidar
