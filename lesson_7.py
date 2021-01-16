class Worker:

    salary = 500

    def work(self):
        print("Сотрудник за смену получает", self.salary)

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
Voditel.salary = 250
Voditel.work()
