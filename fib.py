import functools
from functools import lru_cache
import time


# array to hold times of each function call
times = []

#timer function that prints the runtime of the decorated function
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        startTime = time.perf_counter()
        value = func(*args, **kwargs)
        endTime = time.perf_counter()
        totalTime = endTime - startTime
        times.append(totalTime)
        print(f"Finished in {totalTime:.8f}s: {func.__name__}({args[0]}) -> {value!r}")
        return value
    return wrapper_timer

@lru_cache
@timer
#fibonacci function
def fib(n) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)



if __name__ == "__main__":
    fib(100)