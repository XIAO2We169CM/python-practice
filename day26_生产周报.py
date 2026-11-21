import pandas as pd

df = pd.read_csv("11月第3周 生产记录.csv")
print(df.shape)

print("===== 按天 =====")
day = df.groupby("日期")[["产量", "不良"]].sum().reset_index()
day["不良率%"] = round(day["不良"] / day["产量"] * 100, 2)
print(day)

print("===== 按产线 =====")
line = df.groupby("产线")[["产量", "不良", "停机分钟"]].sum().reset_index()
line["不良率%"] = round(line["不良"] / line["产量"] * 100, 2)
line = line.sort_values("不良率%", ascending=False)
print(line)

print("===== 总览 =====")
total_qty = df["产量"].sum()
total_bad = df["不良"].sum()
rate = round(total_bad / total_qty * 100, 2)
worst_day = day.sort_values("不良率%", ascending=False)["日期"].tolist()[0]
worst_line = line["产线"].tolist()[0]
summary = pd.DataFrame({
    "项目": ["总产量", "总不良", "整体不良率%", "不良率最高的一天", "不良率最高的产线"],
    "数值": [total_qty, total_bad, rate, worst_day, worst_line],
})
print(summary)

with pd.ExcelWriter("11月第3周 生产周报.xlsx") as w:
    summary.to_excel(w, sheet_name="总览", index=False)
    day.to_excel(w, sheet_name="按天", index=False)
    line.to_excel(w, sheet_name="按产线", index=False)
print("周报已生成：3 个工作表")