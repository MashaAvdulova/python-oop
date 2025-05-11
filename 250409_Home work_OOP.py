# Создайте класс`Book`с # методом @ classmethod, который# создает объект из строки "Название, Автор, Год".
#
# Добавьте в класс Book @ staticmethod для проверки, является ли год выпуска допустимым (например, не отрицательным)

class Book:
    def __init__(self, name, author, year):
        #  публичные атрибуты
        self.name = name
        self.author = author
        self.year = year

    @classmethod
    def from_string(cls, string):
        name, author, year_str = string.split(',')
        year = float(year_str)
        return cls(name, author, year)  # создаем экземпляр класса

    @staticmethod
    def is_year(year):
        return year > 0

book_1 = Book.from_string('Война и мир,Лев Толстой,1869')
print(book_1.name, book_1.author, book_1.year)
print(Book.is_year(book_1.year))
