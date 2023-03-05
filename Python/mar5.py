"""
student_data = ("Ritesh", 21, "Male", "Guitar", "Canada", "Software Engineer")
# name, age, gender, *other_details = student_data
# print(f"Name: {name}\nAge: {age}\nGender: {gender}\nOther Details: {other_details}")

# *others, country, profession = student_data
# print(f"Country: {country}\nProfession: {profession}\nOther Info: {others}")

# name, *info, profession = student_data
# print(f"Name: {name}\nProfession: {profession}\nExtra info: {info}")
"""

# set: Mutable & Unordered collection of members in which repeatition is eliminated
"""
s1 = {"Ahmedabad", "Jamnagar", "Bhavnagar", "Dwarka", "Somnath"}
# print(s1)
# print(type(s1))
s2 = {23, 12, 11, 15, 45, 76, 9, 10, 11}
# print(len(s2))
# print(s2)

# s3 = {}
l1 = [1,2,3,4]
t1 = (5,6,7,8)
s3 = set(l1)
s4 = set(t1)
name = "akshat"
s5 = set(name)
print(s3)
print(s4)
print(s5)

# Creating empty set
empty = set()
print(empty)
print(type(empty))
print(len(empty))


# Example of a dictionary
result = {"Maths" : 34, "Chemistry" : 39, "Physics" : 50}
"""
# Sets are unordered means,
"""
No index no
No accessing through index no
No slicing
"""
"""
s1 = {23, 12, 11, 15, 45, 76, 9, 10, 11}
# s1[2] = 13    Can't access through index nos
print(min(s1))
print(max(s1))
print(sorted(s1))   # sorted always returns a NEW LIST
"""

# set Methods:
# s1 = {23, 12, 11, 15, 45, 76, 9, 10, 11}
# s1.add(13)

# s1.clear()
# del s1
"""
s2 = s1.copy()
s3 = s1
s1.clear()
print(s1)
print(s2)
print(s3)
"""

# s1.discard(101)
# s1.remove(101)
# print(s1.pop())

# s2 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
# s1.update(s2)
# print(s1)


# Set Operations
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = {5,6,7,8}
s4 = {5, 7, 1, 3, 6, 4, 8}

# uni = s1.union(s2)
# print(uni)
# inter = s1.intersection(s2)
# s1.intersection_update(s2)
# print(inter)


# diff1 = s1.difference(s2)
# print(diff1)
# s1.difference_update(s2)        # same as: s1 = s1.difference(s2)

# diff2 = s2.difference(s1)
# print(diff2)
# new = diff1.union(diff2)        # symmetric diff of s1 & s2
# print(new)

# sym_diff = s1.symmetric_difference(s2)
# print(sym_diff)
# s1.symmetric_difference_update(s2)      # same as: s1 = s1.symmetric_difference(s2)
# print(s1)

# s1.update(s2)
# print(s1)

# print(s1.issubset(s4))
# print(s2.issubset(s4))
# print(s4.issuperset(s2))

# print(s1.isdisjoint(s3))
# print(s1.isdisjoint(s2))

"""
HW: Try to create every collection in every collections & get some conclusion.
"""