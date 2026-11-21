lines = [
    {"line": "A线", "output": 1200, "ng": 30},
    {"line": "B线", "output": 1500, "ng": 16},
    {"line": "C线", "output": 2000, "ng": 10},
    {"line": "D线", "output": 800, "ng": 20},
]
lines.append({"line": "E线", "output": 1000, "ng": 15})
lines[1]["ng"] = 31

print("===== 注塑车间 质检日报 =====")
total_output = 0
total_ng = 0
alarm_names = []
worst = lines[0]

for x in lines:
    rate = round(x["ng"] / x["output"] * 100, 2)
    if rate > 2:
        level = "【预警】"
        alarm_names.append(x["line"])
    elif rate > 1:
        level = "【关注】"
    else:
        level = "【正常】"
    print(x["line"], rate, "%", level)
    total_output = total_output + x["output"]
    total_ng = total_ng + x["ng"]
    if x["ng"] / x["output"] > worst["ng"] / worst["output"]:
        worst = x



print("----------------------------")
all_rate = round(total_ng / total_output * 100, 2)
print("总产量", total_output, "总不良", total_ng, "整体不良率", all_rate, "%")
print("预警产线", len(alarm_names), "条：", alarm_names)
worst_rate = round(worst["ng"] / worst["output"] * 100, 2)
print("最差产线", worst["line"], worst_rate, "%")

f = open("质检日报.txt", "w", encoding="utf-8")
f.write("整体不良率 " + str(all_rate) + " %\n预警产线 " + str(alarm_names))
f.close()