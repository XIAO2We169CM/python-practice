line = "A线"
output = 1200
ng = 30
rate = ng / output * 100
print(line, "不良率", rate, "%")
if rate > 2:
    print("【预警】", line, "不良率超过 2%")