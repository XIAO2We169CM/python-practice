import pandas as pd

logs = [
    {"设备": "注塑1号", "状态": "运行", "分钟": 600},
    {"设备": "注塑1号", "状态": "停机", "分钟": 60},
    {"设备": "注塑1号", "状态": "待料", "分钟": 60},
    {"设备": "注塑2号", "状态": "运行", "分钟": 480},
    {"设备": "注塑2号", "状态": "停机", "分钟": 240},
    {"设备": "冲压1号", "状态": "运行", "分钟": 700},
    {"设备": "冲压1号", "状态": "停机", "分钟": 20},
]
df = pd.DataFrame(logs)
print(df.shape)

total = df.groupby("设备")["分钟"].sum()
run = df[df["状态"] == "运行"].groupby("设备")["分钟"].sum()
print(total)
print(run)

print("===== 稼动率 =====")
out = pd.DataFrame({"运行分钟": run, "总分钟": total})
out["稼动率%"] = round(out["运行分钟"] / out["总分钟"] * 100, 1)
out = out.reset_index().sort_values("稼动率%")
print(out)
print(out.shape)
print("最低", out["设备"].tolist()[0])

print("===== 损失 =====")
loss = df[df["状态"] != "运行"].groupby("状态")["分钟"].sum()
print(loss)

out.to_excel("11月18日 设备稼动率.xlsx", index=False)
print("已导出", len(out), "台设备")
