# Collections in Python
"""
Ordered     Mutable     list        []
Ordered     Immutable   tuple       ()
Unordered   Mutable     set         {}
Unordered   Immutable   frozenset

Special Collections:
strings: Ordered & Immutable collections of characters              " "/' '
dictionaries: Unordered & Mutable collections of key : value pairs  {}
"""

# Lists: Ordered & Mutable collections of members
# l1 =    [13, 90, -45, 90, 80, 45.7, 90, 1005, -48.84, 90, -8085]
# index:  0   1   2    3   4    5    6     7      8     9     10
# -ve:  -11 -10  -9   -8  -7   -6   -5    -4     -3    -2    -1
# print(l1)
# print(type(l1))
# print(len(l1))

# Ordered means:
"""
Each & Every element has +ve & -ve index no
Accessing through +ve or -ve index no
slicing with step with -ve or +ve index
"""
# a = l1[5]
# print(a)
# l1[5] = 192.92      # item assignment
# print("l1 =",l1)
# l1[5] = a

# l2 = l1[2 : 9]      # slicing never changes the original data
# print(l2)

# print(l1[1 : 10 : 2])
# print(l1[-5])
# print(l1[2 : -3])

# print(l1[-1 : -11 : -1])

# myCity = "Ahmedabad"
# myCity[4] = 'D'

# print(min(l1))
# print(max(l1))
# print(sorted(l1))               # sorted will always return a NEW LIST
# print(sorted(l1, reverse=True))
# print(sum(l1))

# vegetables = ["potato", "Ladyfinger", 5, " tomato", "onion", "beetroot", "peas"]
# print(vegetables)
# print(min(vegetables))
# print(max(vegetables))
# print(sorted(vegetables))

# ASCII

# list methods:
l1 = [13, 90, -45, 90, 80, 45.7, 90, 1005, -48.84, 90, -8085]
# print(l1.append(500))
# l1.append(500)
# print(l1)
# l1.clear()
# print(l1)
# del l1
# print(l1)
# del l1[4]

# l2 = l1.copy()
# l3 = l1

# l1.append(200)
# l3.clear()

# print("l1 =", l1)
# print("l2 =", l2)
# print("l3 =", l3)

# print(l1.count(90))
# print(l1.count(9000))

# l2 = [100, 200, 300]
# l1.append(l2)
# print(len(l1))
# print(l1.extend(l2))

# print(l1.index(1005))
# print(l1.index(90))
# print(l1.index(90, 2))
# print(l1.index(90, 5, 7))
# print(l1.index(9009, 5, 10))
# l1.insert(6, 101)
# print(l1.pop(3))
# l1.remove(101)
# l1.remove(90)
# l1 = l1[::-1]
# l1.reverse()
# l1.sort()
# l1.sort(reverse=True)

print(l1)
# Next Class: Operators