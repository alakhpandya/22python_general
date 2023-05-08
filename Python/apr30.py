# chr: ascii to character
"""
print(chr(65))
"""
# eval:
"""
a = "print('Hello World!')"
eval(a)
# print(a)

b = "int(input(f'Enter a number: '))"
p = eval(b)
print(p)
"""

# isinstance
"""
a = float(input("a: "))
b = 25
print(isinstance(a, int))
print(isinstance(b, int))
"""

# next
"""
marks = [
    ["Sr.", "Name", "Sub-1", "Sub-2"],
    [1, "Darshan", 30, 31],
    [2, "Rishi", 29, 33],
    [3, "Jay", 32, 32]
]
# print(marks[0])
title = next(marks)
print(marks)
"""

# pow: as using **

# round
"""
print(round(3.4))           # 3
print(round(3.7))           # 4
print(round(3.141569, 2))   # 3.14
print(round(3.141569, 3))   # 3.142
print(round(3.142596))      # 3
print(round(3.142596, 0))   # 3.0
print(round(4568.239, 2))   # 4568.24
print(round(4568.239, 0))   # 4568.0
print(round(4568.239, -1))  # 4570
print(round(4568.239, -3))  # 5000

print(round(-3.4))
print(round(-4.8))
"""
import math
# floor & ceil
"""
print(math.floor(5.9))
print(math.floor(3.001))

print(math.ceil(3.0001))

print(math.floor(-2.2))
print(math.floor(-3.2))

print(math.ceil(-2.2))
print(math.ceil(-3.2))
"""
# zip
"""
roll_no = [1, 2, 3, 4, 5]
names = ["A", "B", "C", "D", "E"]
print(list(zip(roll_no, names)))
percentage = [75, 82, 93, 58, 90]
print(list(zip(roll_no, names, percentage)))
"""

# map
"""
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

numbers = [2,3,4,5,6,7,8,9]
"""
# use the above function and create another list named 'factorials' that contains factorials of all the members of list 'numbers'
# Write your code here


# HW
"""
1.what is the result of following expression i python ?
    print("54"+"23")

    a)77
    b)5423
    c)54
    d)23

2.what is the result of following expression  python ?
    print(true==1)

    a)True
    b)False
    c)Error

3.what is the result of following expression  python ?
    print("1" == 1)

    a)True
    b)False
    c)Error

4.what is output of following statements ?
    x=55/11
    print(x)

    a)5
    b)5.0
    c)6.0

5.Print the result of the following expression:
    (3+4)//2+6

6. Set the value of variable a, b and c such that the following condition evaluates to true:
    a = -1 # change this
    b = -1 # change this
    c = -1 # change this

    # DO NOT CHANGE THE FOLLOWING:

    x = a < b + c

    print(x) # this should be True
    Note: You need to write the code from scratch in the code editor.

7. Problem Description:
    Given total bills amount and amount of a single bill. Print number of bills.

    Note: The total amount is equally splitted in all bills. The number of bills should be an integer value.

    Input Format:
    The first line contains a real number N denoting the total budget. The second line contains an integer M denoting the value of a single bill

    Output Format:
    Print in a single line denoting the total number of bills that can fit in the total budget.

    Problem Constraints:
    1 < N <= 10000; 1 <= M <= 100

    Examples
    Input:
    126.3
    5

    Output: 
    25

8. Problem Description:
    A group of spammers is troubling Varun by calling on his mobile phone repeatedly. After a while, Varun observed a pattern that the mobile number from which the spammers call him is always lesser than his mobile number when compared on the number line. The mobile number of Varun is 1234880990. Given a mobile number as an input print True if the number belongs to the spammers else False.

    Input Format:
    The input will be a single integer representing a mobile number.

    Output Format:
    The output would be True if the condition holds else False

    Sample Input:
    9999999999

    Sample Output:
    False

    Note: All the mobile numbers in this problem are hypothetical
"""
# HW - 2
"""
1. Numerical Derivative
    Problem Description:
    The derivative of a function is a value that tells us how much the output of a mathematical function would change, if we were to make a very, very tiny change in its input. In mathmetical terms, the limit definition of a derivative is defined as: limo Where x and hare both inputs to the h
    function f. You can safely ignore the lim part in the expression.
    Given the values of x and your task is to evaluate the expression for the function f(x) = 3x² + 2 and print the value obtained.

    Input Format:
    The input will contain two numbers.
    The first line will be the x value.
    The second line will be the h value.

    Output Format:
    The output would be a single line float value of the expression in problem description.
    
    Input:
    1
    1
    Output:
    9.0

    Note: The value of hwill always be more than for this problem.

2.Is the third one greater?
    Problem Description:
    Given three integer values as input, your task is to print True if the third number is greater than the first two else False.

    Input Format:
    Input will contain three lines denoting three integer values.

    Output Format:
    The output would be True if the condition holds else False.

    Input:
    1
    2
    3
    Output:
    True

    Explanation:
    Here 3 is greater than 1 and 3 is also greater than 2 and hence the output is True.

3.	Floors and Ceilings
    Problem Description:
    The floor function floor(x) is defined as the greatest integer less than or equal to the given number.
    For example, floor(7.64)=7.
    Likewise, the ceiling function ceil(x) is defined as the smallest integer greater than or equal to the given number.
    For example, ceil(7.64)=8.
    Given a number x as input, output its floor(x) and ceil(x) values.

    Note: Assume that the input will never be an integer.

    Input Format:
    One line float value

    Output Format:
    Print two integers, first one denoting the floor value and second one the ceiling value of the given number.
    
    Input:
    7.64
    Output:
    7
    8
    
    Example Explanation:
    The greatest integer that is less than or equal to 7.64 is clearly 7.
    The smallest integer that is greater than or equal to 7.64 is clearly 8.

4. Multiply Chain
    Problem Description:
    Given a number n as input, multiply it with the number (n-1) and (n-2) and print the resultant output.

    Input Format:
    A single line containing an integer.

    Output Format:
    A single line output according to the problem description.

    Input:
    10
    Output:
    720

5.Module Trouble
    Problem Description:
    Shikha is trying to solve a hard math problem in which she is required to take the mod of a number x with y quite frequently. Given two numbers x and y write a program that helps Shikha do this easily. Assume that the value of y is always greater than 0.

    Input Format:
    Two lined inputs. The first line denotes the x value and the second one the y value.

    Output Format:
    Single number which is the mod of x with y.

    Input:
    100
    11
    Output:
    1

6.Four average
    Problem Description:
    Given four numbers as input print their average value as output.

    Input Format:
    Four lines denoting four numbers.

    Output Format:
    Single number denoting the average value.

    Input:
    1
    2
    3
    4
    Output:
    2.5

7.Odd/Even - without 'if' statements
    Problem Description
    Given an integer n as input, print True if it is odd and False if it is even. Solve this question with the concepts taught in the Lecture on Operators. DO NOT USE IF/ELSE.

    Input Format:
    A single line input containing the integer.

    Output Format:
    A single-line boolean value.

    Input:
    2
    Output:
    False

    Example Explanation
    The output is False because 2 is even.

8.Are the weights balanced?
    Problem Description:
    A weighing machine has two arms, a left arm, and a right arm. On both sides of the weighing machine we can put in weights and if both of those weights are equal, the arms of the machine will hang equally in the air, with none of them hanging below the other. This is hard to observe visually hence you are asked to write a program that takes in two weight values as input and outputs True if they will leave the machine balanced and False if they will leave the machine unbalanced.

    Input Format:
    The input will contain two lines denoting the weight values on the left and right arms of the machine

    Output Format:
    True if the machine is balanced. False if the machine is unbalanced.

    Input:
    64.0
    63.0
    Output:
    False

9.Raised to the power
    What do you think would be the output when we run the piece of code given below?
    print(3 ** 2 ** 0)

    a.	Error
    b.	0
    c.	3
    d.	1

10.	What would be the output of the following piece of code?
    print("abcd" < "abce")

    a.	Error
    b.	True
    c.	False
"""
# n = int(input())    # 100
# print(n % 2 == 0)

# print(3 ** 2 ** 0)

