def save_log(title, all_rate):
    f = open("质检记录.txt", "w", encoding="utf-8")
    f.write(title + " 整体不良率 " + str(all_rate) + " %\n")
    f.close()

save_log("11月7日", 1.47)
save_log("11月8日", 1.7)

f = open("质检记录.txt", "r", encoding="utf-8")
print(f.read())
f.close()