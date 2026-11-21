lines = [
    {"line": "包1线", "output": 2400, "ng": 36},
    {"line": "包2线", "output": 2000, "ng": 50},
    {"line": "包3线", "output": 0, "ng": 0},
    {"line": "包4线", "output": 1600, "ng": 8},
    {"line": "包5线", "output": 1000, "ng": 30},
]

from openpyxl import Workbook

def safe_rate(output, ng):
    try:
        return round(ng / output * 100, 2)
    except ZeroDivisionError:
        return None

def level_of(rate):
    if rate is None:
        return "停线"
    if rate>2:
        return"预警"
    elif rate>1:
        return"关注"
    else :
        return"正常"


wb = Workbook()
ws = wb.active
ws.append(["产线", "产量", "不良", "不良率%", "等级"])
total_output = 0
total_ng = 0
alarm = []
for x in lines:
    y = safe_rate(x["output"], x["ng"])
    ws.append([x["line"], x["output"], x["ng"], y, level_of(y)])
    print(x["line"], y, level_of(y))
    total_output = total_output + x["output"]
    total_ng = total_ng + x["ng"]
    level = level_of(y)
    if level == "预警":
       alarm.append(x["line"])
all_y = safe_rate(total_output, total_ng)
ws.append(["合计", total_output, total_ng, all_y, level_of(all_y)])
wb.save("11月11日 包装日报.xlsx")
print("总产量", total_output, "总不良", total_ng, "整体不良率", all_y, "%")
print("预警班次",  alarm)
print("已保存", ws.max_row, "行")

f = open("包装记录.txt", "a", encoding="utf-8")
f.write("11月11日 整体不良率 " + str(all_y) + " %\n")
f.close()
print("已记录到 包装记录.txt")