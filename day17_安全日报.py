def safe_rate(ng, output):
    try:
        return round(ng / output * 100, 2)
    except ZeroDivisionError:
        return 0

shifts = [
    {"shift": "白班", "output": 1800, "ng": 27},
    {"shift": "中班", "output": 1600, "ng": 40},
    {"shift": "夜班", "output": 0, "ng": 0},
]
for x in shifts:
    print(x["shift"], safe_rate(x["ng"], x["output"]), "%")

for name in ["11月7日 班次日报.txt", "11月6日 班次日报.txt"]:
    try:
        f = open(name, "r", encoding="utf-8")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("没有找到", name)
print("日报完成")