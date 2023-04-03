# 2. Create a Python program to generate user-defined set. Then ask user to eneter any value & check if the given value is present in a set or not.
"""
n = int(input("No of elements: "))
s1 = set()
for i in range(n):
    inp = input(f"Element-{i}: ")
    s1.add(inp)
"""
# 4. Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.
"""
antonyms = {
    'Right' : 'Left',
    'up' : 'down',
    'positive' : 'negative',
    'big' : 'small'
}

for word in antonyms:
    print(word)

word = input("Enter word: ")
print("Antonym:", antonyms[word])
"""
# 6. Sort the above dictionary by the names of students.
"""
students = {
    "Aakash" : 80,
    "Jeet" : 78,
    "Raksha" : 94,
    "Jigna" : 92,
    "Sweety" : 90,
    "Mahesh" : 95
}

sorted_list = dict(sorted(students.items()))
print(sorted_list)

"""
"""
temp1 = students.items()
print(temp1)
temp2 = []
for item in temp1:
    temp2.append(item[ : :-1])
temp2.sort()
print(temp2)
temp3 = []
for item in temp2:
    temp3.append(item[ : : -1])
final_dictionary = dict(temp3)
print(final_dictionary)
"""


# 1. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.

# for example:
# list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
# input string = 'bug'
# output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']
"""
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
test = input("Enter string: ")
list2 = []
for string in list1:
    count = string.count(test)
    list2.append((count, string))
list2.sort(reverse=True)
print(list2)
sorted_list = []
for item in list2:
    sorted_list.append(item[1])
print(sorted_list)
"""

# Functions:
# syntax:
"""
def function_name(argument1, argument2...):
    code line 1
    code line 2
    .
    .
    .
    return answer
"""
# Defining a function
"""
def printMail():
    print("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\nWhy do we use it?\nIt is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution ")


total_amount = int(input("Total amount: "))
amount_paid = int(input("Amount Paid: "))
if amount_paid < total_amount:
    printMail()     # function call
"""
"""
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

myMatrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
printMatrix(myMatrix)
"""
"""
def scanMatrix():
    rank = int(input("Rank: "))
    matrix = []
    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(float(input(f"a[{i}][{j}]: ")))
        matrix.append(row)
    return matrix

m1 = scanMatrix()
print(m1)
"""
def average(a, b):
    return (a + b)/2

# print(a)
a = average(10,20)
print(a)
# print(b)

# HW Examples: DO ATLEAST 4 EXAMPLES FROM BELOW-
"""
Functions Examples:
1. Ask two integers from user, add their factroials. Now ask two more integers from user and add their factorials too. calculate average of the factorials you computed. Now finally ask one last integer from user and add its factorial to the average.


2. Write a function that prints whether the number passed in its argument is prime or not. Using a main program pass the number given by the user to that function.


3. Write a function to find average of 5 given numbers and a main program that takes 5 integers from user, uses the factorial function to find factorial of each one of them and using average function prints the average of factorials of them.

4. Make a program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.
    ap:
    first term = a = 5
    difference = d = 4
    ap = 5, 9, 13, 17, 21, 25,...
    nth term = a + (n-1)d

5. Develop a program that uses a function to find nth term of an geometric progression whose first term is 'a' & common ratio is 'r'.
formula: a * r^(n-1)

6. Make a function that checks whether the given number is a perfect number or not. Make a program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.

7. Write a function that determines whether the number given in its argument is a Prime number or not. Build a main program that takes two integers from user and print all the Prime numbers between those two integers using that function.

8. Write a function that determines whether the number given in its argument is Armstrong number or not. Build a main program that takes two integers from user and print all the Armstrong numbers between those two integers using that function.

9. Royal Kids Bank

Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()
"""

def perfectCheck(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        # print("Perfect")
        return True
    else:
        # print("Not Perfect")
        return False

a = int(input("Enter two integers:\n"))
b = int(input())
print(f"Perfect numbers between {a} and {b} are:")
for x in range(a, b+1):
    if perfectCheck(x) == True:
        print(x)