def hello(name1, name2, name3):
    print('Hello',name1)
    print('Hello',name2)
    print('Hello',name3)

hello('Alena','Masha',"Sasha")

def hello_set(*args):
    print(args)
    print(len(args))
    for name in args:
        print(f'Hello, {name}')

hello_set('Alena','Masha',"Sasha")

def car_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f'{key} - {value}')


car_info(brand='BMW')
car_info(brand='BMW', model='x5')
car_info(brand='BMW', model='x5', color='Black')

def person_info(*args, **kwargs):
    print(kwargs)
    print(args)

person_info('Ivan', 'Petrov', gender='male', phone='1234567')