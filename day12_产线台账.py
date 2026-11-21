lines = [
    {"line": "A线", "output": 1200, "ng": 30},
    {"line": "B线", "output": 1500, "ng": 16},
    {"line": "C线", "output": 2000, "ng": 10},
    {"line": "D线", "output": 800, "ng": 20},
]

lines.append({"line": "E线", "output": 1000, "ng": 15})
lines[1]["ng"] = 31

for x in lines:
    rate = round(x["ng"] / x["output"] * 100, 2)
    if rate > 2:
        level = "【预警】"
    elif rate > 1:
        level = "【关注】"
    else:
        level = "【正常】"
    print(x["line"], rate, "%", level)

total_ng = 0
alarm_count = 0
for x in lines:
    total_ng = total_ng + x["ng"]
    if x["ng"] / x["output"] * 100 > 2:
        alarm_count = alarm_count + 1
print("总不良数", total_ng, "预警线数", alarm_count)

print(lines[5])