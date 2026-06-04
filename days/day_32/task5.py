from functools import wraps
from task2 import benchmark
def cache_results(func):
    dct = {}
    @wraps(func)
    def wrapped(*args, **kwargs):
        nonlocal dct
        if args in dct:
            return dct[args]
        else:
            result = func(*args, **kwargs)
            dct[args] = result
        return result
    return wrapped
@benchmark
@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(35)
fibonacci(35)