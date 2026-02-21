-- Template: step-to-step conversion by segment (country/device/channel)
-- Assumes funnel_events(user_id, event_time, step, country, device_type, channel)

WITH step_dim AS (
  SELECT 'landing_viewed' AS step, 1 AS step_order UNION ALL
  SELECT 'signup_started', 2 UNION ALL
  SELECT 'email_verified', 3 UNION ALL
  SELECT 'payment_method_added', 4 UNION ALL
  SELECT 'first_order_completed', 5
),
dedup AS (
  SELECT
    user_id,
    country,
    device_type,
    channel,
    step
  FROM funnel_events
  GROUP BY 1,2,3,4,5
),
step_counts AS (
  SELECT
    country,
    device_type,
    channel,
    sd.step_order,
    d.step,
    COUNT(DISTINCT d.user_id) AS users
  FROM dedup d
  JOIN step_dim sd ON sd.step = d.step
  GROUP BY 1,2,3,4,5
),
paired AS (
  SELECT
    country,
    device_type,
    channel,
    step,
    users,
    LAG(users) OVER (PARTITION BY country, device_type, channel ORDER BY step_order) AS prev_users
  FROM step_counts
)
SELECT
  country,
  device_type,
  channel,
  step,
  users,
  ROUND(1.0 * users / NULLIF(prev_users, 0), 4) AS step_rate
FROM paired
ORDER BY step_rate ASC;
