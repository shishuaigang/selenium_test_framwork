import functools
import timeit


def gettime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bg_time = timeit.default_timer()
        func(*args, **kwargs)
        end_time = timeit.default_timer()
        print(end_time - bg_time)

    return wrapper
