# Множественное наследование (наследование от нескольких родителей)
class Father:
    def skills(self):
        print('Ремонт техникиб спорт')

class Mother:
    def skills(self):
        print('Кулинария, искусство')

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print('Программирование')

child = Child()
child.skills()

# Порядок поиска методов (порядок обращения к методам нескольких родителей)
class A:
    def method(self):
        print('A')

class B(A):
    def method(self):
        print('B')

class C(A):
    def method(self):
        print('A')

class D(B, C):
    def method(self):
        print('A')

d = D()
d.method()

print(D.__mro__) # выводит порядок обращения к классу
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# Мексины - классы для добавления функциональности через множественное наследование
