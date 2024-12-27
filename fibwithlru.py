from functools import lru_cache

@lru_cache(maxsize=None)
def fibo_naive(n):
    if n<=1:
        return n
    return fibo_naive(n-1) + fibo_naive(n-2)

print(fibo_naive(5))