#  Родительский (базовый) класс для класса Student
class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def hello(self):
        print(f'Привет, меня зовут {self.name} {self.lastname}')

    def bay(self):
        print('До свидания')


#  Дочерний (производный) класс от класса Person
class Student(Person):
    #  Конструктор дочернего класса должен иметь атрибуты родительского класса и свои (дочернего)
    def __init__(self, name, lastname, age, group, ticket, form_study):
        super().__init__(name, lastname, age)  #  вызываем конструктор родительских классов с их атрибутами
        #  создаем атрибуты дочернего класса
        self.group = group
        self.ticket = ticket
        self.form_study = form_study

    def bay(self):
        print('Goodbay')

class WorkerStudent(Student):
    def __init__(self, name, lastname, age, group, ticket, form_study, job, salary):
        super().__init__(name, lastname, age, group, ticket, form_study)
        self.job = job
        self.salary = salary

    def hello(self):
        print(f'Добрый день! Я работаю в компании {self.job}. Моя заработная плата - {self.salary}')

person_1 = Person(name='Dima', lastname='Ivanov', age=24)
person_1.hello()
student_1= Student(name='Marina', lastname='Petrova', age=22, group='432', ticket='AA456789', form_study='Очная')
student_1.hello()
student_1.bay()
person_1.bay()
worker_1 = WorkerStudent(name='Olga', lastname='Petrova', age=25, group='534', ticket='AA459999', form_study='Очная', job='Яндекс', salary='1 000 000')
worker_1.hello()

class AAA:
    def method(self):
        print('AAA')

class BBB:
    def method(self):
        print('BBB')

class CCC:
    def method(self):
        print('CCC')

class User(AAA, BBB, CCC):
    def hello(self):
        pass

obj = User()
obj.method()