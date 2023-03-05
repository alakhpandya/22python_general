# Remaining Collections/Iterables:
"""
Mutable     Ordered     list        [ ]
Immutable   Ordered     tuple       ( )
Mutable     Unoredered  set         { }
Mutable     Ordered     frozenset

string: Immutable & Ordered Collection of characters            " "
dictionary: Mutable & Unordered collection of key-value pairs   { }
"""

# Tuples: Immutable & Ordered collections of members

# t1 = (11, 64, 23, 45, 11, -20, 0, 11, 23, 11, 99)

# Accessing through index numbers
# print(t1[3])
# print(t1[-3])

# Slicing
# print(t1[2 : 10])
# print(t1)       # slicing doesn't change the original collection but always returns a new collection
# print(t1[2 : 12 : 2])
# print(t1[11 : 2 : -1])
# print(t1[11 : 2 : -2])
# print(t1[2 : -3])

# t1[3] = 95        Not possible as tuples are immutable
# print(t1)
# print(type(t1))
"""
cities = ("Surat", "Mahesana", "Dholka", "Ahmedabad", "Palanpur", "Patan")
print(cities)
"""
# Creating tuple with single element
"""
myCity = ("Vadodara",)
print(myCity)
print(type(myCity))

myLuckyNumber = (2, )
print(myLuckyNumber)
print(type(myLuckyNumber))
"""
# Another way to create tuples
"""
students = "Darshan", "Isha", "Vidhi", "Devanshi"
print(students)
print(type(students))

teacher = "Alakh",
print(teacher)

yourLuckyNumber = 13,
print(yourLuckyNumber)
"""
# Modifying a tuple
"""
# cities_list = list(("Surat", "Mahesana", "Dholka", "Ahmedabad", "Palanpur", "Patan"))
cities_list = list(cities)
# print(cities_list)
cities_list[3] = "Surendranagar"
cities_list.sort(reverse=True)
cities = tuple(cities_list)
print(cities)
"""

# Methods on tuples:
# t1 = (11, 64, 23, 45, 11, -20, 0, 11, 23, 11, 99)

# print(t1.count(11))
# print(t1.index(-20))
# print(t1.index(23))
# print(t1.index(23, 3))
# print(t1.index(11, 3, 8))

# Write a program to create a user-defined tuple of length 10. As a user, enter exactly one number multiple times. Print index number of 2nd occurance of that number.
"""
# user-defined tuple
temp = [float(input(f"no-{x+1}: ")) for x in range(10)]
myTuple = tuple(temp)

# Finding the number that is repeating
for number in myTuple:
    if myTuple.count(number) > 1:
        repeating_number = number
        break

# Index no of first occurance of repeating_number
first = myTuple.index(repeating_number)

# Index no of second occurance of repeating_number
second = myTuple.index(repeating_number, first+1)
print(second)
"""

# Unpacking of collections:
# student_data = ("Jay", 22, "Male")
# student_data = ["Nishith", 20, "Male"]

"""
Create 3 variables that store name of the student, age of the student & gender of the student
student_name, student_age, student_gender
"""
# student_name = student_data[0]
# student_age = student_data[1]
# student_gender = student_data[2]
"""
student_name, student_age, student_gender = student_data

print(f"Name: {student_name}\nAge: {student_age}\nGender: {student_gender}")
"""

# student_data = ("Jay", 22, "Male", "Singing")
# student_name, student_age, student_gender = student_data
# print(f"Name: {student_name}\nAge: {student_age}\nGender: {student_gender}")


# student_data = ["Nishith", 20, "Male"]
# student_name, student_age, student_gender, student_hobby = student_data
# print(f"Name: {student_name}\nAge: {student_age}\nGender: {student_gender}\nHobby: {student_hobby}")
