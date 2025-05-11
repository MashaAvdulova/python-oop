# Определить класс Фигура
# В классе фигура должны быть публичный, защищенный и приватный атрибуты
# Для приватных атрибутов реализовать методы получения и изменения
#
# Определить класс круг,квадрат и треугольник, наследуемый от класса фигура,
# В этих классе , должны быть публичный, защищенный и приватный атрибуты.
# В классах реализовать функции подсчета площади.
#
# Реализовать геттеры и сеттреы для классов.

class Figure:
    def __init__(self, name, square_fg, color):
        #  публичные атрибуты
        self.name = name

        # защищенные атрибуты
        self._square_fg = square_fg

        # приветные атрибуты - не наследуется и не будет доступен в дочернем классе
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        if color.isdigit():
            raise  ValueError ('Некорректно введено значение')
        self.__color = color

#  Дочерний (производный) класс
class Circle(Figure):
    #  Конструктор дочернего класса должен иметь атрибуты родительского класса и свои (дочернего)
    def __init__(self, name, square_fg, color, radius):
        super().__init__(name, square_fg, color)  #  вызываем конструктор родительских классов с их атрибутами
        #  создаем атрибуты дочернего класса
        #  публичные атрибуты
        self.radius = radius

    def square(self):
        self._square_fg = 3.14*self.radius**2
        return self._square_fg

class Square(Figure):
    #  Конструктор дочернего класса должен иметь атрибуты родительского класса и свои (дочернего)
    def __init__(self, name, square_fg, color, side_a):
        super().__init__(name, square_fg, color)  #  вызываем конструктор родительских классов с их атрибутами
        #  создаем атрибуты дочернего класса
        #  публичные атрибуты
        self._side_a = side_a

    def square(self):
        self._square_fg = self._side_a**2
        return self._square_fg

class Triangle(Figure):
    #  Конструктор дочернего класса должен иметь атрибуты родительского класса и свои (дочернего)
    def __init__(self, name, square_fg, color, side_base, height):
        super().__init__(name, square_fg, color)  #  вызываем конструктор родительских классов с их атрибутами
        #  создаем атрибуты дочернего класса
        #  публичные атрибуты
        self.side_base = side_base
        self.__height = height

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if isinstance(height, str):
            raise ValueError('Некорректно введено значение')
        self.__height = height


    def square(self):
        self._square_fg = 0.5*self.side_base*self.__height
        return self._square_fg

circle_1 = Circle(name='Круг 1', square_fg=5, color='Красный', radius=2)
print(circle_1._square_fg)
print(circle_1.get_color())
circle_1.set_color(color='Черный')
print(circle_1.get_color())
print(circle_1.square())

square_1 = Square(name='Квадрат 1', square_fg=7, color='Белый', side_a=10)
print(square_1._square_fg)
print(square_1.get_color())
square_1.set_color(color='Синий')
print(square_1.get_color())
print(square_1.square())

triangle_1 = Triangle(name='Треугольник 1', square_fg=9, color='Зеленый', side_base=4, height=4)
print(triangle_1._square_fg)
print(triangle_1.get_color())
triangle_1.set_color(color='Оранжевый')
print(triangle_1.get_color())
print(triangle_1.square())
print(triangle_1.get_height())
triangle_1.set_height(height=6)
print(triangle_1.get_height())



