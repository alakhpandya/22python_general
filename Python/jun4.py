"""
Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Sample data: ('1':['a', 'b'], '2': ['c','d']) Expected Output: ac, ad, bc, bd


s = {'1':['a', 'b'], '2': ['c','d']}
l = len(s)
new = list(s.values())
# print(new)
l1 = new[0]
l2 = new[1]
for char1 in l1:
    for char2 in l2:
        print(char1 + char2)
"""
"""
from important_functions import fibo

print(fibo(10))
"""
"""
from important_functions import recursiveFact as rf

print(rf(6))
"""
"""
# from important_functions import recursiveAP, recursiveFact
# from important_functions import recursiveAP as ra, recursiveFact as rf, recursiveGP

from important_functions import *

print(recursiveAP(10, 12, 13))
"""
# import may7

# a = int(input())
# print(may7.factorial(a))

# from may7 import factorial

# a = int(input())
# print(factorial(a))

# from important_functions import recursiveFact as rf

# p = int(input())
# print(rf(p))
"""
import important_functions as imp

# print(__name__)
print(imp.fibo(10))
p = imp.PI
Dhiraj = imp.Royal()
"""
# Wrong way
"""
import myPackage
myPackage.myModule.myFunc()
"""
# from myPackage import myModule
# myModule.myFunc()
    # OR
# from myPackage import myModule as mm
# mm.myFunc()
    # OR
# from myPackage.myModule import myFunc
# myFunc()
    # OR
# from myPackage.myModule import myFunc as fnc
# fnc()
    # OR
# from myPackage.myModule import *
# myFunc()

# wrong way:
# from myPackage import subPackage

# from myPackage.subPackage import subModule as sm
# sm.subFunc()
    # OR
# from myPackage.subPackage.subModule import subFunc
# subFunc()

# import pandas as pd