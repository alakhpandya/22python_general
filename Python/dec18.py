"""
print("Python\tis fun\n")
print("But also needs \nconsistency.")
"""

# 'end' statement
# print("Python is fun", end="\n")
# print("Python is fun", end="")
# print("Python is fun", end=" ")
# print("Python is fun", end=" Diya ")
print("Python is fun", end="\t")
print("at Royal.")


# variables & Datatypes in Python
# Numeric Datatypes: int, float, complex
"""
a = 5
# print(a)
print("a =", a)
b = 10.5
print("b =", b)
print(type(a))
print(type(b))

c = 5j - 7
print("c =", c)
print(type(c))
d = 8 + 6j

# multiplication = (5j - 7)(8 + 6j)
print(c + d)
print(c - d)
print(c * d)
print(c / d)
"""

# taking input from user
"""
print("Enter one number:")
a = int(input())					# 10
b = float(input("Enter another number: "))		# 15.6
print("a =", a)
print("b =", b)

# print("a + b =", int(a) + float(b))
print(a, "+", b, "=", a + b )			# 10 + 15.6 = 25.6

print("type of a: ", type(a))
print("type of b: ", type(b))


Take 5 integers from user & store them in variables a, b, c, d & e. Calculate their average and print the answer exactly as shown in the following example:

Example:
Enter 5 integers:
2
3
4
5
6

The average of 2, 3, 4, 5 and 6 is: 4.0
"""
print("Enter 5 integers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

print(f"The average of {a}, {b}, {c}, {d} and {e} is: {(a+b+c+d+e)/5}")






