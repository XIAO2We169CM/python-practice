def calc_rate(ng, output):          # 设备 1：算不良率
    return round(ng / output * 100, 2)

def level_of(rate):                 # 设备 2：判断三档
    if rate > 2:
        return "【预警】"
    elif rate > 1:
        return "【关注】"
    else:
        return "【正常】"

def make_report(shifts, title):     # 设备 3：出整份日报
    print("=====", title, "=====")
    total_output = 0
    total_ng = 0
    alarm_names = []
    worst = shifts[0]
    for x in shifts:
        rate = calc_rate(x["ng"], x["output"])
        level = level_of(rate)
        if level == "【预警】":
            alarm_names.append(x["shift"])
        print(x["shift"], rate, "%", level)
        total_output = total_output + x["output"]
        total_ng = total_ng + x["ng"]
        if x["ng"] / x["output"] > worst["ng"] / worst["output"]:
            worst = x
    all_rate = calc_rate(total_ng, total_output)
    print("----------------------------")
    print("总产量", total_output, "总不良", total_ng, "整体不良率", all_rate, "%")
    print("预警班次", len(alarm_names), "条：", alarm_names)
    print("最差班次", worst["shift"], calc_rate(worst["ng"], worst["output"]), "%")
    f = open(title + ".txt", "w", encoding="utf-8")
    f.write("整体不良率 " + str(all_rate) + " %\n预警班次 " + str(alarm_names))
    f.close()
    return all_rate



today = [
    {"shift": "白班", "output": 1800, "ng": 27},
    {"shift": "中班", "output": 1600, "ng": 40},
    {"shift": "夜班", "output": 1000, "ng": 8},
]
yesterday = [
    {"shift": "白班", "output": 2000, "ng": 18},
    {"shift": "中班", "output": 1500, "ng": 36},
    {"shift": "夜班", "output": 1200, "ng": 15},
]
t = make_report(today, "11月8日 班次日报")
y = make_report(yesterday, "11月7日 班次日报")
if t > y:
    print("今天比昨天高", round(t - y, 2), "个百分点，要查原因")
else:
    print("今天比昨天好")