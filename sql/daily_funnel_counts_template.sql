-- Template: daily funnel counts from event logs
-- Assumes a table funnel_events(user_id, event_time, step, country, device_type, channel, experiment_id, variant)

WITH step_dim AS (
  SELECT 'landing_viewed' AS step, 1 AS step_order UNION ALL
  SELECT 'signup_started', 2 UNION ALL
  SELECT 'email_verified', 3 UNION ALL
  SELECT 'payment_method_added', 4 UNION ALL
  SELECT 'first_order_completed', 5
),
dedup AS (
  SELECT
    DATE(event_time) AS event_date,
    user_id,
    step
  FROM funnel_events
  GROUP BY 1,2,3
),
counts AS (
  SELECT
    d.event_date,
    sd.step_order,
    d.step,
    COUNT(DISTINCT d.user_id) AS users
  FROM dedup d
  JOIN step_dim sd ON sd.step = d.step
  GROUP BY 1,2,3
)
SELECT *
FROM counts
ORDER BY event_date, step_order;
