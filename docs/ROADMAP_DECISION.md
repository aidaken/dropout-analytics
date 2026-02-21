# Roadmap Decision (now / next / later)

## Now (ship + test)
1) Payment friction reduction (shorter form, better defaults)
2) Trust cues on payment step (why we ask, security cue, fees clarity if true)
3) Better errors + retry path
4) Instrumentation: payment_started / payment_failed / payment_method_added with error categories

Why now:
- hits the biggest revenue-proximate leak
- fast to build, fast to measure
- creates clean data for future work

## Next (after we learn from the test)
1) Express pay (Apple Pay / Google Pay), if not included in v1
2) Payment “save and continue” improvements (resume later)
3) Landing page trust and messaging test (biggest volume leak)

Why next:
- higher dependency on platform support and legal copy
- better after we confirm the main causes

## Later (bigger bets)
1) Skip payment for now (only if business model allows it)
2) Personalized onboarding by segment (country/channel/device)
3) Risk controls tuning based on post-change fraud patterns

Why later:
- bigger policy and risk tradeoffs
- needs real production data and stakeholder alignment

