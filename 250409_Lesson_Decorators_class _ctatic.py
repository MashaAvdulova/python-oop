# Классовые методы с помощью декоратора @classmethod (создаем экземпляр класса, есть cls)

class MyClass:
    def instance_method(self, x):
        print(f'Вызовем метод экземпляра. Self = {self}, x = {x}')

obj = MyClass()
obj.instance_method(10) # self автоматически передается как obj

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, string):
        name, salary_str = string.split(',')
        salary = float(salary_str)
        return cls(name, salary) # создаем экземпляр класса

emp = Employee.from_string('Иван,5000')
print(emp.name, emp.salary) # Иван 5000

# с помощью классовых методов меняем атрибут класса
class Pizza:
    default_topping = "Сыр"

    @classmethod
    def set_default_topping(cls, topping):
        cls.default_topping = topping

Pizza.set_default_topping('Грибы')
print(Pizza.default_topping)
# наследование

class Child(Pizza):
    pass

Child.set_default_topping('Оливки')
print(Child.default_topping)
print(Pizza.default_topping)

# статик метод (не создает экземпляр класса)
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18

# проверка без создания экземпляра
print(User.is_adult(27))

# Пример
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
print(Calculator.add(9,1))

