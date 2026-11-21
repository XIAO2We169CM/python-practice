def count_alarm(rates):
    n = 0
    for r in rates:
        if r > 2:
            n = n + 1
        return n

print(count_alarm([1.5, 2.5, 2.4]))
print(count_alarm([2.5, 1.5, 2.4]))