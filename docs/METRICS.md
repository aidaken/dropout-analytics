# Metrics + Tracking Spec

## Primary metric (success)
- First-order conversion rate
  Definition: users who complete first order / users who visited landing page
  Also track step-level: first order / payment added

## Secondary metrics (diagnostics)
- Payment-add rate: payment_added / email_verified
- Time to complete payment step (median, p90)
- Time-to-first-order (median, p90)

## Guardrails (risk)
- Payment failure rate: payment_failed / payment_started
- Fraud flags rate (if available): fraud_flagged / payment_added
- Chargeback rate (if available): chargebacks / first_orders
- Support tickets related to payment (if available)

## Funnel events (minimum viable)
All events include:
- user_id (stable id)
- event_time (UTC)
- session_id
- country
- device_type (mobile/desktop)
- channel (paid/organic/referral if known)
- experiment_id, variant

Events:
1) landing_viewed
2) signup_started
3) email_verification_sent
4) email_verified
5) payment_started
6) payment_method_added
7) payment_failed
8) first_order_completed

Payment event properties (recommended):
- payment_method_type (card, apple_pay, google_pay)
- error_code (if failed)
- error_category (validation, network, bank_decline, fraud_block, unknown)
- form_fields_count (optional, for UX analysis)
- time_on_page_ms

## Data quality checks
- No future timestamps
- user_id uniqueness and stability
- step ordering sanity:
  landing_viewed -> signup_started -> email_verified -> payment_started -> payment_method_added -> first_order_completed
- SRM check in experiment: variant split close to expected ratio

## Example query outputs (what dashboards need)
- Daily funnel conversion by step
- Payment-add rate by device_type, country, channel
- Payment failure reasons ranked
- Time-to-first-order distribution

