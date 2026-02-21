import pandas as pd

df = pd.read_csv("assets/funnel_steps.csv")
steps = df["step"].tolist()
users = df["users"].tolist()

print("Funnel sanity check\n")
print(f"{steps[0]}: {users[0]:,}\n")

for i in range(1, len(steps)):
    prev_step = steps[i-1]
    step = steps[i]
    prev_users = users[i-1]
    cur_users = users[i]
    rate = cur_users / prev_users if prev_users else 0
    drop = prev_users - cur_users
    print(f"{prev_step} -> {step}: rate={rate:.4f} ({rate*100:.1f}%), drop={drop:,}")

