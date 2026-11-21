import pandas as pd

records = [
    {"班次": "白班", "产线": "A线", "产量": 2000, "不良": 30},
    {"班次": "夜班", "产线": "A线", "产量": 1800, "不良": 45},
    {"班次": "白班", "产线": "B线", "产量": 1500, "不良": 60},
    {"班次": "夜班", "产线": "B线", "产量": 1400, "不良": 28},
    {"班次": "白班", "产线": "C线", "产量": 1800, "不良": 108},
    {"班次": "夜班", "产线": "C线", "产量": 0, "不良": 0},
]
df = pd.DataFrame(records)
df["不良率%"] = round(df["不良"] / df["产量"] * 100, 2)
print(df)

print("===== 按班次 =====")
g = df.groupby("班次")[["产量", "不良"]].sum().reset_index()
g["不良率%"] = round(g["不良"] / g["产量"] * 100, 2)
print(g)

print("===== 按产线 =====")
p = df.groupby("产线")[["产量", "不良"]].sum().reset_index()
p["不良率%"] = round(p["不良"] / p["产量"] * 100, 2)
p = p.sort_values("不良率%", ascending=False)
print(p)
print("最差产线", p["产线"].tolist()[0])

g.to_excel("11月16日 班次汇总.xlsx", index=False)
print("已导出", len(g), "个班次")