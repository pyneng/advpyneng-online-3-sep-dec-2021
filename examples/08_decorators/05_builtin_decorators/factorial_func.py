from functools import cache, lru_cache


@cache
def factorial(n):
    print(n)
    return n * factorial(n-1) if n else 1


print(factorial(4))
print(factorial(5))
print(factorial(6))
