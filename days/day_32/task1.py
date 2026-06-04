from functools import wraps
def log_action(func):
    @wraps(func)
    def wrapped(*args,**kwargs):
        print(f"[LOG] Выполняется: {func.__name__}")
        res = func(*args, **kwargs)
        print(f"[LOG] Завершено: {func.__name__}")
        return res
    return wrapped
@log_action
def multiply(a, b):
    return a*b
print(multiply(4,5))

