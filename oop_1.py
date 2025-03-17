'''
ООП - объектно-ориентированное программирование - методология или стиль программирования
на основе описания типов (моделей) предметной области и их взаимодействие.
Т.е. создание классов и их экземпляров (объектов), имеющих определенное свойства (атрибыты) и
методы (функции)

Основные понятия:
Инкапсуляция
Наследование
Полиморфизм


'''

class Car: # не наследуемый класс
    # атрибуты класса (общие для всех объектов)
    color = 'black'
    year = 2020
    def __init__(self, color, year, brand, model):
        self.color = color
        self.year = year
        self.brand = brand
        self.model = model
    # метод объекта
    def start(self):
        print(f'Машина {self.brand} {self.model} завелась')

# создание объекта
car_1 = Car(color='red', year = '2020', brand = 'bmw', model = 'x5')
car_2 = Car(color='blue', year = '2023', brand = 'audi', model = 'a5')
# получени доступа к атрибутам класса - через .
print(car_1.color)
print(car_1.year)# через имя объекта
print(car_2.color)
print(car_2.year)
print(Car.color) # через имя класса

# вызов метода объектов
car_1.start()
car_2.start()
