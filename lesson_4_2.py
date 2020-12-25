data = list()


def my_function():
    diction = {
        "brand": car,
        "model": model,
        "year": year
    }
    data.append(diction)


while len(data) < 3:
    car = input("Введите марку машины: ")
    model = input("Введите модель: ")
    year = input("Введите год выпуска: ")

    my_function()
print(data)
