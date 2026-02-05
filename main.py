#1
def even_suma(a, b):
    total = 0
    for i in range(min(a, b), max(b, a) + 1, 2):
        total += i

    return total


print(even_suma(4, 6))


# 2
def arifmetka(royxat):
    return (max(royxat) + min(royxat)) / 2


# 3
def palidrom(soz):
    soz = soz.lower()
    if soz == soz[::-1]:
        return True
    else:
        return False


# 4
def yigind(son):
    son = str(son)
    s = 0
    for i in son:
        s += int(i)
    return s
