from openpyxl import Workbook

def yield_of(output, ng):
    try:
        return round((output - ng) / output * 100, 2)
    except ZeroDivisionError:
        return None

def grade_of(y):
    if y is None:
        return "停线"
    if y >= 98:
        return "达标"
    elif y >= 95:
        return "关注"
    else:
        return "不达标"

lines = [
    {"line": "A线", "output": 2000, "ng": 30},
    {"line": "B线", "output": 1500, "ng": 60},
    {"line": "C线", "output": 1800, "ng": 108},
    {"line": "D线", "output": 0, "ng": 0},
]

wb = Workbook()
ws = wb.active
ws.append(["产线", "产量", "不良", "良率%", "等级"])
total_output = 0
total_ng = 0
for x in lines:
    y = yield_of(x["output"], x["ng"])
    ws.append([x["line"], x["output"], x["ng"], y, grade_of(y)])
    print(x["line"], y, grade_of(y))
    total_output = total_output + x["output"]
    total_ng = total_ng + x["ng"]
all_y = yield_of(total_output, total_ng)
ws.append(["合计", total_output, total_ng, all_y, grade_of(all_y)])
wb.save("11月10日 良率统计.xlsx")
print("已保存", ws.max_row, "行")

f = open("良率记录.txt", "a", encoding="utf-8")
f.write("11月10日 整体良率 " + str(all_y) + " %\n")
f.close()
print("已记录到 良率记录.txt")