import requests
import time

'''
Декораторы - это функции, которые позволяют расширять или изменять поведение других функций без необходимости изменения самой функции
@simple_decorator
def hello():
    pass
'''

# хотим добавить сообщение перед написанием Hello и после
def simple_decorator(func):
    def wrapper():
        print('Перед вызовом функции')
        func()
        print('После вызова функции')
    return wrapper

@simple_decorator
def hello():
    print('Hello')

hello()

#  хотим измерить время выполнения функции
def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения запроса : {end_time-start_time:.4f} секунд')
    return wrapper

@timing
def google_request(url, name):
    response = requests.get(url)
    print(response.status_code)
    print(name)

url = 'http://google.com'
google_request(url, name = 'Alena')

# неизвестное кол-во позиционных аргументов *args, именованных **kwargs
