# Aim, Oservation Table, Conclusion

"""
Observations

List        tuple       set - unordered

list        list        No list
tuple       tuple       tuple - immutable
set         set         No set - mutable

We cannot create mutable collections in unordered collections in Python.
"""

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

# frozenset: Immutable version of set
"""
l1 = ["Hello", "World", "How", "Are", "You?"]
fs1 = frozenset(l1)
fs2 = frozenset({56, 32, 12, 99, 0, -43})
s3 = {3,6,9,2}
# fs2 = frozenset(56, 32, 12, 99, 0, -43)
print(fs1)
print(fs2)
s3.add(12)
# s3.intersection_update(s2)
# print(fs1.union(fs2))
# print(fs1.union(s3))
# print(fs2.union(l1))
"""

# Dictionary: Unordered & Mutable collections of key : value pairs
# result = {"Physics" : 83, "Maths" : 91, "Python" : 100}
"""
No Index Nos
No Accessing through index
No Slicing
"""
# print(result)

# Accessing value through key
# print(result["Python"])

# print(result[1])

# Get me a conclusion: What is valid in keys?
# Keys of a dictionary must be immutable & unique.

# Adding new key value pair to a dictionary:
"""
result["English"] = 89
print(result)
result["Chemistry"] = 87
result["Maths"] = 98
print(result)
"""
"""
party = {
    "Vivek" : "Pizza",
    "Ayush" : 23,
    "Jay" : ["Soup", "Main Course", "Gulab Jamun"],
    "Rishi" : ("Dosa", "Pepsi"),
    "Alakh" : {"Dosa", "Pepsi"},
    "Dhiraj" : frozenset({"Rotlo", "Gud", "Buttermilk"}),
    "Marlin" : {"BF" : "Sandwich", "Lunch" : "Punjabi", "Dinner" : "Pau Bhaji"}
}
print(party)
# Take name of the person from user as input and print their dish.
person = input("Name of the person: ").capitalize()
if person == "Jay" or person == "Rishi" or person == "Alakh" or person == "Dhiraj":
    for item in party[person]:
        print(item)
elif person == "Marlin":
    meal = input("BF/Lunch/Dinner?: ")
    print(party[person][meal])
else:
    print(party[person])
"""

result = {"Physics" : 83, "Maths" : 91, "Python" : 100}
# result.clear()
# del result
# del result["Maths"]

# result["Maths"] = ""

# new_result = result.copy()
# result2 = result

# print(result)

consumers = ["Darshan", "Nishkal", "Vidhi", "Devanshi", "Harsh"]
subsidy = dict.fromkeys(consumers, 1000)
"""
subsidy = {}

# Write your code here
for person in consumers:
    subsidy[person] = 1000
"""
print(subsidy)

# output:
"""
{"Darshan" : 1000, "Nishkal" : 1000, "Vidhi" : 1000, "Devanshi" : 1000, "Harsh" : 1000}
"""

# Next Class: the remaining dictionary methods