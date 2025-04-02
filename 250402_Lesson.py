'''
eg =
gt >
ge >=
lt <
le <=
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name
    def __add__(self, other):
        return self.age + other.age
    def __sub__(self, other):
        return self.age - other.age
    def __mul__(self, other):
        return self.age * other.age
    def __truediv__(self, other):
        return self.age / other.age
    def __gt__(self, other):
        return len(self.name) > len(other.name)


Alex =Person(name='Alexandr', age=25)
Dima =Person(name='Dima', age=40)
print(Alex+Dima)
print(Alex/Dima)
print(Alex>Dima)
print(Alex)