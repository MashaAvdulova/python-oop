from datetime import  datetime
'''
Инкапсуляция - одоин из основных принципов ООП, который подразумевает сокрытие внутреннего состояния объекта
и предоставление доступа к нему только через специальные методы.
Это позволяет защитить данные от некорректного использования.
В Python реализуется через использование приватных и защищенных атрибутов
'''

class Person:
    def __init__(self, name, lastname, age, passport):
        #  публичные атрибуты
        self.name = name
        self.lastname = lastname

        # защищенные атрибуты
        self._age = age

        # приветные атрибуты - не наследуется и не будет доступен в дочернем классе
        self.__passport = passport

    def change_name(self, name):
        self.name = name

    # def get_passport(self):
    #     return self.__passport
    #
    # def set_passport(self, passport):
    #     if not passport.isdigit():
    #         raise  ValueError ('паспорт должен быть цифрой')
    #     self.__passport = passport


    #  Декораторы
    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        if not passport.isdigit():
            raise  ValueError ('паспорт должен быть цифрой')
        self.__passport = passport

    @property
    def current_time(self):
        return  datetime.today().strftime('%d.%m.%Y')


person_1= Person(name='Nokita', lastname='Ivanov', age='15', passport='123456')
person_1.change_name(name='Vova') # для защищенных и незащищенных атрибутов (в Rython это только на уровне договоренностей)
person_1.name = 'Valera' # для незащищенных атрибутов
print(person_1.name)
person_1._age = 20
print(person_1._age)

# некорректное использование языка:
person_1.__passport = 2
print(person_1.__passport)

# корректное использование языка:
# print(person_1.get_passport()) # _Person__passport - настоящее имя атрибута
# print(dir(person_1))
#
# person_1.set_passport('7777777')
# print(person_1.get_passport())

print(person_1.passport)
person_1.passport= '111111'
print(person_1.passport)

print(person_1.current_time)
