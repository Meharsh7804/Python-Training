def decorator(fun):
    def wrapper():
        print(f"Before calling function {fun.__name__}")
        fun()
        print(f"After calling function {fun.__name__}")  
    return wrapper

@decorator
def greet():
    print("Hello, World!")

def date_time():
    from datetime import datetime
    print("Current date and time:", datetime.now())

greet()
date_time()

def decorator_with_args(fun):
    def wrapper(*args, **kwargs):
        print(f"Before calling function {fun.__name__} with args: {args} and kwargs: {kwargs}")
        result = fun(*args, **kwargs)
        print(f"After calling function {fun.__name__} with args: {args} and kwargs: {kwargs}")
        return result
    return wrapper

@decorator_with_args
def print_sum(a, b):
    print(f"The sum of {a} and {b} is: {a + b}")

print_sum(5, 3)

# Decorator with parameters
def repeat(n):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                fun(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Meharsh")