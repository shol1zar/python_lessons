class Worker:

    def __init__(self, salary=500):
        self.salary = salary
        print("Сотрудник за смену получает", self.salary)

    def work(self):
        print("Труженик")

    def __del__(self):
        print("Данные о рабонике удалены")


class Driver(Worker):

    def __init__(self, salary=200):
        self.salary = salary

    def work(self):
        print("Водитель за поездку берет", self.salary)


Rabotyaga = Worker()
Rabotyaga.work()
Voditel = Driver()
Voditel.work()
