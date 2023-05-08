# map
"""
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

numbers = [2,3,4,5,6,7,8,9]
"""
# use the above function and create another list named 'factorials' that contains factorials of all the members of list 'numbers'
# Write your code here
# factorials = []
# for n in numbers:
#     factorials.append(factorial(n))
"""
factorials = map(factorial, numbers)
# print(factorials)
# for n in factorials:
#     print(n)
f2 = list(factorials)
print(factorials.__sizeof__())
print(f2.__sizeof__())
"""
# from sys import getsizeof

# filter:
"""
def hugeTransactions(transaction):
    return abs(transaction) >= 50000

transactions = [1000, 25000, -31000, -60000, 40000, 49900, 120000, -70000]

bigTransactions = []
# Write your code here
for transaction in transactions:
    if hugeTransactions(transaction):
        bigTransactions.append(transaction)

bigTransactions = tuple(filter(hugeTransactions, transactions))
print(bigTransactions)
"""
"""
from functools import reduce

def absoluteTotal(a, b):
    return abs(a) + abs(b)

transactions = [1000, 25000, -31000, -60000, 40000, 49900, 120000, -70000]
# april = [10, -10, 20, -20]
# print(absoluteTotal(10, -10))
# Use above function and the list of transaction, use the topics taught (especially for loop) and write your code below to get total amount transacted.
# print(reduce(absoluteTotal, transactions))

total = 0
for transaction in transactions:
    total = total + abs(transaction)

print(total)
"""
# Next Class: Recursive functions, organizing our code in modules & packages