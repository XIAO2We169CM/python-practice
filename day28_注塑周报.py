import pandas as pd

df = pd.read_csv("11月第4周 注塑记录.csv")
print(df.shape)

print("===== 按机台 =====")
line = df.groupby("机台")[["产量", "不良", "停机分钟"]].sum().reset_index()
line["不良率%"] = round(line["不良"] / line["产量"] * 100, 2)
line = line.sort_values("不良率%", ascending=False)
print(line)

print("===== 按班次 =====")
day = df.groupby("班次")[["产量", "不良"]].sum().reset_index()
day["不良率%"] = round(day["不良"] / day["产量"] * 100, 2)
print(day)

print("===== 总结 =====")
total_qty = df["产量"].sum()
total_bad = df["不良"].sum()
rate = round(total_bad / total_qty * 100, 2)
worst_line = line.sort_values("不良率%", ascending=False)["机台"].tolist()[0]
#worst_line = line["机台"].tolist()[0]
low = line.sort_values("停机分钟", ascending=False)["机台"].tolist()[0]
a = line[line["不良率%"] >= 2]
summary = pd.DataFrame({
    "项目": ["整体不良率%", "不良率最高的机台", "停机分钟最多的机台","预警机台"],
    "数值": [rate,  worst_line,low,a["机台"].tolist()],
})
print(summary)

with pd.ExcelWriter("11月第4周 注塑周报.xlsx") as w:    
    day.to_excel(w, sheet_name="按班次", index=False)
    line.to_excel(w, sheet_name="按机台", index=False)
print("周报已生成：2 个工作表")