shifts = [
    {"shift": "白班", "rate": 1.5},
    {"shift": "中班", "rate": 2.5},
    {"shift": "夜班", "rate": 0.8},
    {"shift": "加班", "rate": 2.4},
]

a = shifts[0]
for x in shifts:
    if x["rate"] > a["rate"]:
        a = x

print("最差班次",a["shift"],a["rate"],"%")
