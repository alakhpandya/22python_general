from sys import getsizeof

# Comparing list, tuples & objects
"""
l1 = [x for x in range(1, 101)]
# print(l1)
print(getsizeof(l1))
t1 = tuple(l1)
print(getsizeof(t1))
temp_dict = dict.fromkeys(l1, 1000)
# print(temp_dict)
dict_object = temp_dict.keys()
print(getsizeof(dict_object))
"""

# result = {"Physics" : 83, "Maths" : 91, "Python" : 100}
# print(result.get("Astrology"))
# print(result["Astrology"])
# print(result.keys())
# all_keys = list(result.keys())
# all_keys = result.keys()
# print(all_keys)
# all_keys.append("Astrology")
# print(all_keys)
# for x in all_keys:
#     print(x)
# all_values = result.values()
# print(all_values)

# print(result.items())
# maths_marks = result.pop("Maths")
# print(result)
# print(maths_marks)

# print(result.popitem())
# print(result)

# result2 = {"Chemistry" : 90, "java" : 99, "SQL" : 10}
# result.update(result2)
# print(result)


result = {"Physics" : 83, "Maths" : 91, "Python" : 100, "Chemistry" : 90, "java" : 99, "SQL" : 10}

# print(result.setdefault("C", 95))
# result["C++"] = 99
# result["Chemistry"] = 80
# print(result.setdefault("Chemistry", 80))
# print(result)


"""
Write a program to ask name & marks of a subject. Add them in the following dictionary if the subject doesn't exist in it and print "Success". If the subject already exists, show user the old marks of that subject and ask whether they want to overwrite the marks or not. If user chooses 'no', print "Aborted" or if user chooses 'yes' then, update the marks of that subject in the dictionary. In all cases, print the final dictionary at last. Use setdefault method.

result = {"Physics" : 83, "Maths" : 91, "Python" : 100, "Chemistry" : 90, "java" : 99, "SQL" : 10}


sub = input("Subject Name: ")
marks = int(input("Marks: "))

marks_returned = result.setdefault(sub, marks)
if marks_returned == marks:
    print("Success")
else:
    print(f"Subject {sub} already exists with {marks_returned} marks.")
    overwrite = input("Do you want to overwrite? Yes/No? - ").lower()
    if overwrite == "yes":
        result[sub] = marks
        print("Marks overwritten successfully.")
    elif overwrite == "no":
        print("Aborted")
print(result)
"""

"""
Advanced examples of List and Dictionary:
1. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.

for example:
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input string = 'bug'
output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']

2. Create a Python program to generate user-defined set. Then ask user to eneter any value & check if the given value is present in a set or not.

3. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

4. Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.

5. Ask user to give name and marks of 10 different students. Store them in dictionary.

6. Sort the above dictionary by the names of students.

7. Sort the dictionary in ex-5 by the marks.

8. Make a Python program to count letters of the word: MISSISSIPPI. Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user.

9. Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""


# Next Class: Functions