import requests
import pandas as pd

r = requests.get("http://127.0.0.1:8000/mes_today.json", timeout=5)
print("状态码", r.status_code)

data = r.json()
print(data["车间"], data["日期"], "共", len(data["记录"]), "条")

df = pd.DataFrame(data["记录"])
m = df.groupby("机台")[["产量", "不良"]].sum().reset_index()
m["不良率%"] = round(m["不良"] / m["产量"] * 100, 2)
m = m.sort_values("不良率%", ascending=False)
print(m)

rate = round(df["不良"].sum() / df["产量"].sum() * 100, 2)
print("整体不良率", rate)