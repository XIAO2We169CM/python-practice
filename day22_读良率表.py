import pandas as pd

df = pd.read_excel("11月10日 良率统计.xlsx")
print(df)
print(df.shape)
print(df["产线"].tolist())

df = df[df["产线"] != "合计"]
print("产线数", len(df), "总产量", df["产量"].sum(), "总不良", df["不良"].sum())
ok = df[df["等级"] == "达标"]
print("达标", ok["产线"].tolist())
low = df[df["良率%"] < 98]
print("良率低于98", low["产线"].tolist())
print("停线", df["良率%"].isna().sum(), "条")
print("平均良率", round(df["良率%"].mean(), 2))