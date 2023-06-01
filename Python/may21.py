# Ask an integer from user and print that term of Fibonacci sequence using recursive function that takes an integer 'n' as argument and returns nth term of Fibonacci Sequance. (n >= 1)
"""
1, 1, 2, 3, 5, 8, 13........
recursive formula:
nth term = (n-1)th term + (n-2)th term
"""
# Memoization (Explicit)
"""
cache_memory = {}
def fibo(n):
    if n in cache_memory:
        return cache_memory[n]
    if n == 1 or n == 2:
        cache_memory[n] = 1
        return 1
    else:
        term = fibo(n-1) + fibo(n-2)
        cache_memory[n] = term
        return term

n = int(input("Enter term:"))
print("Sr.No.\tTerm")
for i in range(1,n+1):
    # print(f"{i}.\t",fibo(i))
    fibo(i)
print(cache_memory)
"""
# Memoization (Implicit)
"""
from functools import lru_cache

# Decorators = Wrapper Function
@lru_cache(maxsize=3)
# @lru_cache(maxsize=128)
# @lru_cache(maxsize=1000)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter term:"))
print("Sr.No.\tTerm")
for i in range(1,n+1):
    print(f"{i}.\t",fibo(i))
"""

# Organizing our Code in Modules & Packages
"""
import important_functions

print(important_functions.recursiveFact(5))
"""
"""
import important_functions as imp

print(imp.recursiveFact(5))
"""

# import speech_recognition as sr
# import numpy as np
# import pandas as pd

# Next class: some more ways to import, __name__, creating packages etc