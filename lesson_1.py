birth_date = int(input("Введите год рождения:  "))
month = input("Введите месяц:  ")
day = int(input("Введите день :  "))
star = ["овен", "телец", "близнецы", "рак", "лев", "дева", "весы",
        "скорпион", "стрелец", "козерог", "водолей", "рыбы"]
result = 2020-birth_date
if month == "январь" and day >= 21 or month == "февраль" and day <= 20:
    print("Вам" + " " + str(result), "и вы" + " " + star[10])
if month == "февраль" and day >= 21 or month == "март" and day <= 20:
    print("Вам" + " " + str(result), "и вы" + " " + star[11])
if month == "март" and day >= 21 or month == "апрель" and day <= 20:
    print("Вам" + " " + str(result), "и вы" + " " + star[0])
if month == "апрель" and day >= 21 or month == "май" and day <= 20:
    print("Вам" + " " + str(result), "и вы" + " " + star[1])
if month == "май" and day >= 21 or month == "июнь" and day <= 21:
    print("Вам" + " " + str(result), "и вы" + " " + star[2])
if month == "июнь" and day >= 22 or month == "июль" and day <= 22:
    print("Вам" + " " + str(result), "и вы" + " " + star[3])
if month == "июль" and day >= 23 or month == "август" and day <= 23:
    print("Вам" + " " + str(result), "и вы" + " " + star[4])
if month == "август" and day >= 24 or month == "сентябрь" and day <= 23:
    print("Вам" + " " + str(result), "и вы" + " " + star[5])
if month == "сентябрь" and day >= 24 or month == "октябрь" and day <= 23:
    print("Вам" + " " + str(result), "и вы" + " " + star[6])
if month == "октябрь" and day >= 24 or month == "ноябрь" and day <= 22:
    print("Вам" + " " + str(result), "и вы" + " " + star[7])
if month == "ноябрь" and day >= 23 or month == "декабрь" and day <= 21:
    print("Вам" + " " + str(result), "и вы" + " " + star[8])
if month == "декабрь" and day >= 22 or month == "январь" and day <= 20:
    print("Вам" + " " + str(result), "и вы" + " " + star[9])
