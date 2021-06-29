def decorator(func):
    def wrapper():
        print('Commans before funcion')
        func()
        print('Commands after function!')
    return wrapper

@decorator
def fun():
    print('I am a function')

fun()