data = list()


def my_func(**kwargs):
    data.append(kwargs)


while len(data) < 3:
    my_func(
            car=input("Введите марку машины: "),
            model=input("Введите модель: "),
            year=input("Введите год выпуска: ")
            )

print(data)
