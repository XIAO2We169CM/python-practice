shifts = [
    {"shift": "白班", "output": 1800, "ng": 27},
    {"shift": "中班", "output": 1600, "ng": 40},
    {"shift": "夜班", "output": 1000, "ng": 8},
]
shifts.append({"shift": "加班", "output": 500, "ng": 12})


print("===== 注塑车间 班次日报 =====")
total_output = 0
total_ng = 0
alarm_names = []
worst = shifts[0]

for x in shifts:
    a = round(x["ng"] / x["output"] * 100, 2)
    if a > 2:
        b = "【预警】"
        alarm_names.append(x["shift"])
    elif a > 1:
        b = "【关注】"
    else :
        b = "【正常】"
    print(x["shift"],a,"%",b)
    total_output = total_output + x["output"]
    total_ng = total_ng + x["ng"]
    if x["ng"] / x["output"] > worst["ng"] / worst["output"]:
        worst = x


print("----------------------------")
c = round(total_ng / total_output * 100, 2)
print("总产量：",total_output,"总不良：",total_ng,"整体不良率：",c,"%")
print("预警产线",len(alarm_names),"条：",alarm_names)
d = round(worst["ng"] / worst["output"]* 100, 2)
print("最差产线",worst["shift"],d)