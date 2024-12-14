def func():
    return 1
func()

def hello(name='Bartek'):
    print('Hello function has been executed')
    
    def greet():
        return '\t This is greet'
    
    def welcome():
        return '\t This is welcome'

    print('End of function')
    
    if name == 'Bartek':
        return greet
    else:
        return welcome
    
new_func = hello('Bartek')
new_func

def cool():
    
    def super_cool():
        return 'I am very cool'
    
    return super_cool

bad = cool()
bad()


def hello():
    return 'Hi Bartek'

def other(some_function):
    print('Other code')
    print(some_function())
    
other(hello)




def new_decorator(original_function):
    
    def wrap_func():
        print('Some extra code')
        
        original_function()
        print('Extra code after function')
        
    return wrap_func

def func_needs_decorator():
    print('I want to decorate')
    
decorated_function = new_decorator(func_needs_decorator)
decorated_function()

@new_decorator
def func_needs_decorator():
    print('I want to be decorator')
    
func_needs_decorator()