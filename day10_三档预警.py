line = "A线"
output = 1200
ng = 30
rate = round(ng / output * 100, 2)
print(line, "不良率", rate, "%")
if rate > 2:
    print("【预警】停线排查")
elif rate > 1:
    print("【关注】班组长巡检")
else:
    print("【正常】继续生产")
    
