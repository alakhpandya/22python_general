# HW-2, Q-1
"""
x = float(input())
h = float(input())
fx = (3 * (x ** 2)) + 2
fxh = (3 * ((x + h) ** 2)) + 2
print((fxh - fx)/h)
"""
# Factorial
"""
8! = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1
5! = 5 x 4 x 3 x 2 x 1

Recursive Definition of Factorial:
    Recursive Step: n! = n * (n - 1)!
    5! = 5 x 4! = 120
    4! = 4 x 3! = 24
    3! = 3 x 2! = 6
    2! = 2 x 1! = 2
    1! = 1 x 0! = 1
    
    
    Non Recursive Step: for n = 0
    0! = 1
"""
"""
if non recursive step
else recursive step
"""
"""
def recursiveFact(n):
    if n == 0:
        return 1
    else:
        return n * recursiveFact(n - 1)
"""
# Write a recursive function to find nth term of an Arithmetic Progression whose first term is 'a' and common difference is 'd' (both given by user.)
"""
Example of an AP:
a = 6, d = 7
AP: 6, 13, 20, 27, 34, 41, 48

formula = a + (n - 1)d
Recursive Step:
    nth term = (n - 1)th term + d
Non Recursive Step:
    1st term = a
"""
# Write a recursive function to find nth term of a Geometric Progression whose first term is 'a' and common ratio is 'r' (both given by user.)
"""
Example of a GP:
a = 3, r = 4
GP: 3, 12, 48, 192
"""
def recursiveGP(a, r, n):
    if n == 1:
        return a
    else:
        return recursiveGP(a, r, n-1) * r
    
a = 3
r = 4
print(recursiveGP(a, r, 4))