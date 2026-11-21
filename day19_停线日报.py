from openpyxl import Workbook

def safe_rate(ng,output):
    try:
        return round(ng/output*100,2)
    except ZeroDivisionError:
        return

def level_of(rate):
    if rate is None:
        return "无数据"
    if rate>2:
        return"预警"
    elif rate>1:
        return"关注"
    else :
        return"正常"

shifts = [
    {"shift": "白班", "output": 1800, "ng": 27},
    {"shift": "中班", "output": 1600, "ng": 40},
    {"shift": "夜班", "output": 0, "ng": 0},
]

wb = Workbook()
ws =wb.active
ws.append(["班次", "产量", "不良", "不良率%", "等级", "备注"])
total_output = 0
total_ng = 0
for x in shifts:
    rate = safe_rate(x["ng"], x["output"])
    ws.append([x["shift"], x["output"], x["ng"], rate, level_of(rate),
               "停线" if x["output"] == 0 else ""])
    total_output = total_output + x["output"]
    total_ng = total_ng + x["ng"]
all_rate = safe_rate(total_ng, total_output)
ws.append(["合计", total_output, total_ng, all_rate, level_of(all_rate), ""])
wb.save("11月9日 停线日报.xlsx")
print("已保存", ws.max_row, "行")
    
        