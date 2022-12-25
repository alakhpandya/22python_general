# string datatype
"""
a = "my string"
b = 'your string'
c = "c"
print(c, type(c))

length_of_a = len(a)
print("Length of a:", length_of_a)
"""

# concat
"""
print(a + " " + b)
"""

# string: Ordered & Immutable collection of characters

d = 	"Marry Christmas to all of you and a very very HAPPY NEW YEAR!"
# index: 0123456789..................................................60
# -ve:	 ....................................................987654321

# print(len(d))

# Accessing through index
"""
print(d[8])
print(d[-8])
print(d[0])
"""
# slicing
"""
print(d[2 : 9])

print(d[6 : 60 : 2])
print(d[10 : ])
print(d[ : 50])
print(d[ : ])
print(d[10 : 50 : ])
print(d[ : : ])
print(d[ : : 3])

print(d[-59 : -52])
print(d[-10 : 10 : -1])
print(d[4 : -3])
print(d[ : : -1])
print(d[ : : -3])
print(d[ : : 0])
"""

# functions vs. methods

print(d)
type(d)
len(d)


# methods:

# Case-related methods
"""
# capitalize(string)	wrong
e = d.capitalize()
print(e)
print(d.upper())
print(d.lower())
print(d.title())
print(d.swapcase())
print(d.casefold())
"""

# allignment related methods
"""
print(d.center(100))
print(d.center(100, "-"))
print(d.rjust(100))
print(d.rjust(100, "$"))
print(d.ljust(100))
print(d.ljust(100, "."))
"""

# count
"""
print(d.count('a'))
print(d.count('a', 6))
print(d.count('a', 6, 20))

print(d.count('very'))
print(d.count('very', 35))
print(d.count('very', 35, 42))
"""

print(d.encode('utf-16'))

# Next Class: methods starting from endswith