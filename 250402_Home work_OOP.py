class Employee:
    def __init__(self, name, lastname, age, post):
        #  публичные атрибуты
        self.name = name
        self.lastname = lastname

        # защищенные атрибуты
        self._age = age

        # приветные атрибуты - не наследуется и не будет доступен в дочернем классе
        self.__post = post

    def change_name(self, name):
        self.name = name

    @property
    def post(self):
        return self.__post

    @post.setter
    def post(self, post):
        if post.isdigit():
            raise  ValueError ('Некорректно введено значение')
        self.__post = post


#  Дочерний (производный) класс
class Programmer(Employee):
    #  Конструктор дочернего класса должен иметь атрибуты родительского класса и свои (дочернего)
    def __init__(self, name, lastname, age, post, experience, language, position):
        super().__init__(name, lastname, age, post)  #  вызываем конструктор родительских классов с их атрибутами
        #  создаем атрибуты дочернего класса
        #  публичные атрибуты
        self.experience = experience
        # защищенные атрибуты
        self._language = language
        # приветные атрибуты - не наследуется и не будет доступен в дочернем классе
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if position.isdigit():
            raise ValueError('Некорректно введено значение')
        self.__position = position

employee_1 = Employee(name='Dima', lastname='Ivanov', age=24, post='Engineer')
programmer_1= Programmer(name='Marina', lastname='Petrova', age=22, experience=5, language='Python', post='Programmer', position='Data scientist')

print(employee_1.name)
employee_1.change_name(name='Vladimir')
print(employee_1.name)

print(programmer_1.post)
print(employee_1.post)

employee_1.post='Programmer'
programmer_1.post='Engineer'

print(employee_1.post)
print(programmer_1.post)

print(programmer_1.position)
programmer_1.position='Data analytic'
print(programmer_1.position)