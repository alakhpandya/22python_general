# s1 = "Happy New Year! Wishing everyone of you a great 2023 ahead!"
"""
print(s1.endswith('!'))
print(s1.endswith('head!'))
print(s1.endswith('head..'))
print(s1.endswith('ear!', 0, 15))
print(s1.endswith('ahead!', 58))

print(s1.startswith('H'))
print(s1.startswith('h'))
print(s1.startswith('Hap'))
print(s1.startswith('Wish', 16))
print(s1.startswith('Wish', 16, 50))
"""
"""
print("Subject\t".expandtabs(30) + "Test1\tTest2\tFinal")
print("Maths\t".expandtabs(30) + "23\t20\t77")
print("Machine Learning\t".expandtabs(30) + "22\t19\t91")
print("C\t".expandtabs(30) + "24\t18\t72")
print("Environment\t".expandtabs(30) + "23\t25\t90")
print("C++\t".expandtabs(30) + "17\t22\t80")
print("Artificial Intelligence I\t".expandtabs(30) + "20\t24\t88")
print("Java\t".expandtabs(30) + "21\t23\t82")
print("Python\t".expandtabs(30) + "25\t25\t95")
"""
"""
print(s1.find('Y'))
print(s1.find('e'))
print(s1.find('e', 8))
print(s1.find('e', 12, 40))
print(s1.find('ing', -40, -4))
print(s1.find('z'))
print(s1.find('year'))
print("------------------")

print(s1.index('Y'))
print(s1.index('e'))
print(s1.index('e', 8))
print(s1.index('e', 12, 40))
print(s1.index('ing', -40, -4))
# print(s1.index('z'))
print("------------------")

print(s1.rfind('Y'))
print(s1.rfind('e'))
print(s1.rfind('e', 8))
print(s1.rfind('e', 12, 40))
print(s1.rfind('ing', -40, -4))
print("------------------")

print(s1.rindex('Y'))
print(s1.rindex('e'))
print(s1.rindex('e', 8))
print(s1.rindex('e', 12, 40))
print(s1.rindex('ing', -40, -4))
"""
# Methods starting from 'is': these will always return True/False
# print(s1.isupper())
# print(s1.islower())
# print(s1.istitle())

# s1 = "Happy New Year!\nWishing everyone of you a great 2023 ahead! ©Alakh Pandya2023"
"""
s2 = "RoyalTechnosoft"
print(s1.isalpha())
print(s2.isalpha())

s3 = "9825782290"
print(s3.isnumeric())

s4 = "RoyalTechnosoft9825782290"
print(s4.isalnum())

print(s2.isalnum())
print(s3.isalnum())

print(s3.isnumeric())
"""
# print(s1.isascii())
# s5 = "fortryiselseifwhileelif"
# print(s5.isidentifier())
# print(s1.isprintable())
# s6 = "      \t\t          \t   \n       \n          \t        "
# print(s6.isspace())

s1 = "Happy New Year! Wishing everyone of you a great 2023 ahead!"
# print(s1.split())
# print(s1.split('a'))
# print(s1.split('a', 3))
# print(s1.rsplit('a'))
# print(s1.rsplit('a', 3))
# print(s1.split('everyone'))

# split_list = ['May', 'this', 'year', 'brings', 'you', 'everything', 'you', 'want!']
# s2 = "_".join(split_list)
# s2 = "\t".join(split_list)
# print(s2)

# print(s1.partition('everyone'))
# print(s1.partition('e'))
# print(s1.rpartition('e'))
"""
s2 = "                Happy New Year!!                                       "
print(s2)
print("Length =", len(s2))

s3 = s2.lstrip()
print(s3)
print("Length =", len(s3))

s4 = s2.rstrip()
print(s4)
print("Length =", len(s4))

s5 = s2.strip()
print(s5)
print("Length =", len(s5))

s6 = "$$$$$$$$$$$$$$$$$$$$$Happy$New$Year!$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
# print(s6.lstrip('$'))
# print(s6.rstrip('$'))
print(s6.strip('$'))
"""
"""
s1 = "Hello"
s2 = "Python!"
print(s1 + s2)
s1.__add__(s2)

s3 = 5
s4 = 10
print(s3 + s4)
s3.__add__(s4)
"""
# print(s6.replace('$', '-', 5))
# s1.splitlines()
print("Enter your date of birth (dd/mm):")
dd = input("Date(dd): ")
mm = input("Month(mm): ")
print(f"Your next birthday will come on {dd.zfill(2)}/{mm.zfill(2)}/2023")


# HW: find out the difference between .isnumeric(), .isdigit() & .isdecimal()
# string examples for homework:
"""
1. Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. 
Example:
input: Alakh Janakkumar Pandya
output: A.J.Pandya
2. Write a program to find the number of vowels, consonents and white space characters in a given string.
Example:
input string: Python Programming
output:
vowels: 4
whitel spaces: 1
consonents: 13
3. Write a program to make a new string with the word "the" deleted in the given string.
eg:
input string: This is the lion in the cage.
output: This is lion in cage.
4. Write a Python code that asks a string from user and replace the first occurance of " " with "_" and last occurance of " " with "#".
Example:
input string: Keep yourself mute while not speaking.
output: Keep_yourself mute while not#speaking.

"""
# Next Class: Lists