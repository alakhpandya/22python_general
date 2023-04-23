# Scope of a variable, local variables, global variables & global keyword
"""
var1 = 10                           # global variable

def func1():
    global var1
    var1 += 1
    print("var1 from func1 =", var1)
    # print("var2 from func1 =", var2)
    var3 = 30                       # local variable: variable with local scope
    print("var3 from func1 =", var3)
    def subFunc():                  # local function: function with local scope
        print("var3 from subFunc =", var3)
    subFunc()
    return var1

def func2():
    global var1, var2
    print("var2 from func2 =", var2)
    # print("var3 from func2 =", var3)

print("var1 from main =", var1)
var1 += 1
a = func1()
var2 = 20                           # global variable for all the functions CALLED AFTER THIS POINT
func2()
# subFunc()
print("var1 from main =", var1)

# print("var3 from main =", var3)
"""

# A typical programming sequence:
"""
import statements

global constants & variables

functions

main
"""

# lambda functions 
# def cube(x):
#     return x ** 3
"""
cube = lambda x : x ** 3
print(cube(3))

def sqrt(n):
    return n ** 0.5

sqrt = lambda n : n ** 0.5

def avg(a, b):
    return (a + b)/2

avg = lambda a, b : (a + b)/2

def root():
    return float(input("number: ")) ** 0.5

root = lambda : float(input("number: ")) ** 0.5
print(root())
"""

# lambda a, b : (a + b)/2
# lambda : float(input("number: ")) ** 0.5

# some useful built in functions

n = [10, 32, 34, 50, 62, 73, 89, 93, 10]
# n = [1, 2, 34, 5, 6, 7, 8, 9, 10, "Vivek"]
# print(sum(n))
# name = ["Vivek", "Prajapati"]
# print(sum(name, " "))

# print(sum(n, 1000))

x1 = 3
y1 = 4

x2 = -2
y2 = -4

distance = abs(x1 - x2) + abs(y1 - y2)
print(distance)

print("Absolute of 5:", abs(5))
print("Absolute of -5:", abs(-5))

# Next Class: Some more Built-in useful functions, Recursive functions

# HW:
"""
1. Remaining Bake Time
    Problem Description:
    You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook. According to your cookbook, the Lasagna should be in the oven for 40 minutes. Given the time (in minutes), the lasagna has been in the oven, find how many more minutes the lasagna still needs to bake for.

    Problem Constraints
    0 <= N <= 40

    Input Format:
    The only first line contains the integer N, denoting the actual time (in minutes) the lasagna has been in the oven for.

    Output Format:
    Print in a single line how many minutes the lasagna needs to bake.

    Examples
    Input: 
    30
    Output: 
    10

    Example Explanation
    Note: The problem constraints mean that when we test your code, the test cases used in the backend can have input values only within those constraints.You need not implement them in your code.You need to make sure your code will work for all such input values!

2. Preparation Time
    Problem Description:
    You'll write some code to help you cook a gorgeous lasagna from your favorite cookbook. Now, you also want to add a few layers to the lasagna. Assume **each layer takes 2 minutes** to prepare. Given the number of layers you want to add to the lasagna, find how many minutes you would spend making them.

    Input Format:
    The only first line contains the integer N denoting the number of layers.

    Output Format:
    Print in a single line how many minutes are required to prepare N layers.

    Examples 
    Input:
    2
    Output:
    4

3. Total Elapsed Cooking Time
    Problem Description:
    You wrote some code to help you cook a gorgeous lasagna from your favorite cookbook. Now, you want to find the total number of minutes you've been cooking for the sum of your preparation time and the time the lasagna has already spent baking in the oven. The preparation time of one layer is 2 minutes. Given the number of layers added to the lasagna and the number of minutes the lasagna has been baking in the oven, find the total elapsed cooking time (prep + bake) in minutes.

    Problem Constraints:
    1 <= N <= 20
    0 <= M <= 40

    Input Format:
    There are 2 lines in the input.
    The first line contains the integer N denoting the number of layers.
    The second line contains the integer M denoting the time the lasagna has already spent baking in the oven.

    Output Format:
    Print in a single line the total elapsed cooking time.

    Examples 
    Input 1:
    3
    20
    Output 1:
    26

    Input 2:
    1
    29
    Output 2:
    31

4. Total Bills Value
    Problem Description:
    Given the value of a single bill and the number of bills you received, print the total value of the bills.

    Note: The value of all the bills are same

    Problem Constraints
    1 <= N <= 100
    1 <= M <= 100

    Input Format:
    The first line of the input is an integer N denoting the value of a single bill.
    The second line of the input is an integer M denoting the number of bills.

    Output Format:
    Print in a single line denoting the total value of bills.

    Examples 
    Input:
    12
    10
    Output:
    120

5. Nilay only likes Integers
    Problem Description:
    Nilay is continuously receiving a stream of numbers that are rounded off to three decimal places. The program that Nilay wrote is giving the output in form of a float, but he needs this output in form of an integer. This integer here will be the largest integer less than or equal to the given number. Write a program that helps Nilay solve this problem.

    Input Format:
    The input will contain three lines that contain three float numbers respectively.

    Output Format:
    The output should be three lines denoting the largest integer less than or equal to the given number.

    Input:
    0.001
    16.203
    20.999
    Output:
    0
    16
    20

6. The floor slope
    Problem Description:
    Given the (x, y) co-ordinates of two points on a 2D plane, calculate the slope of the line they make and print the greatest integer less than of equal to the value of the slope acoording to the output format specified.

    Input Format:
    The input will contain four lines. All integers.
    The first line contains the x_1 coordinate.
    The second line contains the y_1 coordinate.
    The third line contains the x_2 coordinate.
    The fourth line contains the y_2 coordinate.

    Output Format:
    The output should be a single line saying:
    The value of the floor slope is [the slope value]

    Input:
    1
    2
    3
    4
    Output:
    The value of the floor slope is 1

7. Getting Started - 2
    Problem Description:
    Your friend Rahul plans to visit exotic countries all around the world. Sadly, Rahul's math skills aren't good enough. Given the amount of money Rahul has before the currency exchange and the amount of money that is spent from his savings, print the amount of money that remains in his savings.

    Input Format:
    The first line contains an integer N denoting the total savings, the amount of money before exchange.
    The second line contains an integer M denoting the exchanging amount, denoting the amount of money that is spent from the savings.

    Output Format:
    Print a single line denoting the amount of money that is left in his savings.

    Problem Constraints:
    1 <= N <= 1000
    1 <= M <= N

    Examples
    Input:
    116
    12
    Output:
    104

8. What is the date?
    Problem Description:
    Rahul is working on solving a problem that needs him to have his date in Day/Month/Year format. Unfortunately, he just has the Day, Month, and Year as an integer value. Write a piece of code that helps Rahul get out of this situation.

    Input Format:
    The input will contain three lines
    1. Day
    2. Month
    3. Year

    Output Format:
    Print a single line in "Day/Month/Year" format.
    Note: The output should not contain "" or ''.

    Input:
    1
    12
    2017

    Output:
    1/12/2017

9. Do all probabilities add to 1?
    Problem Description:
    One of the most fundamental axioms of probability theory is that the total probability of a set of related events always adds up to 1. Given three probability values, your task is to check if they all add up to 1.

    Input Format:
    The input will contain three lines. The first, second, and third probability value respectively.

    Output Format:
    The output will be a single line boolean variable which is True if all three probabilites add upto 1 else False.

    Input:
    0.70
    0.20
    0.10
    Output:
    True

10. Valid Variable Names
    Which of the following is a valid way of initializing a variable in python?

    a. %variable = 2
    b. 2variable = 2
    c. _variable = 2
    d. \\vari able = 2

"""