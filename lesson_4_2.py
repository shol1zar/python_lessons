data = list()


def my_func(a):
    return a


while len(data) < 3:
    car = input("Введите марку машины: ")
    model = input("Введите модель: ")
    year = input("Введите год выпуска: ")

    diction = {
        "car": car,
        "model": model,
        "year": year
                }
    data.append(my_func(diction))

print(data)
