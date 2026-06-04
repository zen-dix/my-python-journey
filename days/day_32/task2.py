from functools import wraps
import time


def benchmark(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Время выполнения {func.__name__}: {end-start:5f} сек")
        return res
    return wrapped
@benchmark
def heavy_math(n):
    summary = 0
    for i in range(1, n):
        summary += i**2
    return summary
print(heavy_math(1_000_000)+5)