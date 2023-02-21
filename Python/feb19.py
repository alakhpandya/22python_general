# List Comprehension
# Create a list of integers from 0 to 1000
"""
n = []
for i in range(1001):
    n.append(i)
"""
"""
n = [i for i in range(1001)]
print(n)
"""
# create a user-defined list of 5 numbers.
"""
n = []
for i in range(5):
    n.append(int(input()))
"""
"""
n = [int(input(f"no-{i+1}: ")) for i in range(5)]
print(n)
"""
# create a user-defined list of n numbers, where n to be given by user.
"""
no = int(input("Length of the list: "))
n = [int(input(f"no-{i+1}: ")) for i in range(no)]
print(n)
"""
# Create a list of even numbers from 0 to 100 in a list.
"""
n = [i for i in range(101) if i % 2 == 0]
print(n)
"""
# Create a user-defined nxn matrix using nested lists
"""
n = int(input("n: "))
a = [[int(input(f"a[{i}][{j}]: ")) for j in range(n)] for i in range(n)]
print(a)
"""
"""
n = int(input("n: "))       # "1634"
power = len(str(n))
sum = 0
temp = n
while n > 0:
    digit = n % 10      # 4
    sum = sum + digit**power
    n = n//10
n = temp
if sum == n:
    print("Armstrong.")
else:
    print("Not Armstrong.")
"""

"""
n = int(input("n: "))       # "1634" => [1, 6, 3, 4]

# power = len(str(n))

# characters = []
# for x in "Vivek":   # x = 'V', 'i', 'v', 'e', 'k'
#     characters.append(x)

# list_of_digits = []
# for x in str(n):
#     list_of_digits.append(x**4)

# list_of_powers = [int(x)**len(str(n)) for x in str(n)]

# print(list_of_powers)

print("Armstrong.") if sum([int(x)**len(str(n)) for x in str(n)]) == n else print("Not Armstrong.")
"""
"""
myString = "HelloWorld"
for x in range(myString.lower().count('l')):
    print(x)
myList = list(myString)

myList.append("z").sort()
print(myList)
"""

# Remaining Collections:
"""
Mutable     Ordered     list
Immutable   Ordered     tuple
Mutable     Unoredered  set
Mutable     Ordered     frozenset

string: Immutable & Ordered Collection of characters
dictionary: Mutable & Unordered collection of key-value pairs
"""