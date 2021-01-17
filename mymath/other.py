def rounds(a):
    return round(a)


def minimum():
    listo = list()
    i = 0
    while i < 3:
        intg = int(input("Введите число: "))
        listo.append(intg)
        i += 1
        print(listo)
    return min(listo)


def maximum():
    listo = list()
    i = 0
    while i < 3:
        intg = int(input("Введите число: "))
        listo.append(intg)
        i += 1
        print(listo)
    return max(listo)
