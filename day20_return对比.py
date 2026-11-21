def count_4(rates):
    n = 0
    for r in rates:
        if r > 2:
            n = n + 1
    return n

def count_8(rates):
    n = 0
    for r in rates:
        if r > 2:
            n = n + 1
        return n

data = [2.5, 2.6, 2.7]
print("4格", count_4(data))
print("8格", count_8(data))