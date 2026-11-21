import pandas as pd

records = [
    {"产线": "A线", "产量": 2000},
    {"产线": "A线", "产量": 1800},
    {"产线": "B线", "产量": 1500},
]
df = pd.DataFrame(records)

g1 = df.groupby("产线")[["产量"]].sum()
print(g1)
print(g1.shape)

print("-----")
g2 = df.groupby("产线")[["产量"]].sum().reset_index()
print(g2)
print(g2.shape)