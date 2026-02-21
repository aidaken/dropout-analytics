from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ASSETS = Path("assets")
OUT = Path("outputs")
OUT.mkdir(exist_ok=True)

AOV = 50

# Load funnel steps generated earlier (synthetic)
df = pd.read_csv(ASSETS / "funnel_steps.csv")
steps = df["step"].tolist()
users = df["users"].tolist()

# Expected step names in your funnel_steps.csv
# 0: Visited landing page
# 1: Started signup
# 2: Verified email
# 3: Added payment method
# 4: Completed first order

landing = users[0]
signup = users[1]
verified = users[2]
payment_added = users[3]
first_orders = users[4]

# Baseline rates
r_landing_to_signup = signup / landing
r_signup_to_verified = verified / signup
r_verified_to_payment = payment_added / verified
r_payment_to_order = first_orders / payment_added

def scenario(payment_add_rate: float):
    payment_added_new = verified * payment_add_rate
    first_orders_new = payment_added_new * r_payment_to_order
    return payment_added_new, first_orders_new

scenarios = [
    ("Baseline", r_verified_to_payment),
    ("Scenario A: 56% -> 68%", 0.68),
    ("Scenario B: 56% -> 71%", 0.71),
]

rows = []
for name, pay_rate in scenarios:
    pay_added_new, first_orders_new = scenario(pay_rate)
    lift_orders = first_orders_new - first_orders
    lift_rev = lift_orders * AOV
    rows.append({
        "scenario": name,
        "payment_add_rate": pay_rate,
        "payment_added": round(pay_added_new),
        "first_orders": round(first_orders_new),
        "lift_first_orders": round(lift_orders),
        "lift_revenue_$": round(lift_rev),
    })

out_df = pd.DataFrame(rows)
out_df.to_csv(OUT / "impact_scenarios.csv", index=False)

# Plot: first orders by scenario
fig, ax = plt.subplots(figsize=(9, 4.8))
ax.bar(out_df["scenario"], out_df["first_orders"])
ax.set_title("First orders per 10,000 visitors (baseline vs scenarios)")
ax.set_ylabel("First orders")
ax.tick_params(axis="x", rotation=15)
plt.tight_layout()
plt.savefig(OUT / "impact_first_orders.png", dpi=200)

print(out_df.to_string(index=False))
print(f"\nSaved: {OUT / 'impact_scenarios.csv'}")
print(f"Saved: {OUT / 'impact_first_orders.png'}")
