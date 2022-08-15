## ⚡ Advanced Decorators with *args and **kwargs excercise.
def logging_decorator(function):
    def wrapper(*args):
        list = [a for a in args]
        b = f"You called {function.__name__}({list})"
        print(b.replace("[", "").replace("]", ""))
        print(f"It returned: {function(args)}")
    return wrapper

@logging_decorator
def add_function(a: list):
    return sum(a)

add_function(1, 2, 3)