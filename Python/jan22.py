# Operators in Python
"""
1. Arithmetic Operators: +, -, *, /, %, ** (exponent), // (floor division/integer division)
2. Comparision/Conditional/Relational Operators/Conditions: <, >, <=, >=, ==, !=
    # these operators will always return either True or False
3. Logical Operators: and, or, not
4. Bitwise Operators: &, |, ~, ^ (xor- exclusive or), <<, >>

    3 : 0 0 1 1
        & & & &
    5 : 0 1 0 1
    -----------
        0 0 0 1 = 1

    3 : 0 0 1 1
        | | | |
    5 : 0 1 0 1
    -----------
        0 1 1 1 = 7

    3 : 0 0 1 1
        ^ ^ ^ ^
    5 : 0 1 0 1
    -----------
        0 1 1 0 = 6


    3 : 0 0 1 1
    ~3: 1 1 0 0 = -4

    23 : 0 0 0 1  0 1 1 1
    << : 0 0 1 0  1 1 1 0 : 46
    << : 0 1 0 1  1 1 0 0 : 92
    << : 1 0 1 1  1 0 0 0 : 184

    100 : 0 1 1 0  0 1 0 0
    >>  : 0 0 1 1  0 0 1 0 : 50
    >>  : 0 0 0 1  1 0 0 1 : 25
    >>  : 0 0 0 0  1 1 0 0 : 12

5. Assignment Operators: 
    =
    a = 5
    shorthand operators:

    a = a + b   : a += b
    a = a - b   : a -= b
    a = a * b   : a *= b
    a = a / b   : a /= b
    a = a % b   : a %= b
    a = a ** b  : a **= b
    a = a // b  : a //= b
    a = a & b   : a &= b
    a = a | b   : a |= b
    a = a ^ b   : a ^= b
    a = a << 3  : a <<= b
    a = a >> 3  : a >>= b

    There is no such thing as i++ or i-- in Python, so we have to write i += 1 or i -= 1.

6. Membership Operators: in, not in

7. Identity Operators: is, is not
"""

# print(10 ** 3)      # 10^3
# print(64 ** (1/2))
# print(64 ** 0.5)
# print(11/4)     # 2.75
# print(11//4)    # 2

# print(10 > 20)
# print(10 <= 20)

# a = 3
# b = 5
# c = 10
# d = 15
# print(a > b or c > b)
# print(a > b and c > b)

# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~a)

# print(23 << 3)
# print(100 >> 2)

# print("toh" in "Python")
# print("th" in "Python")

# d <<= 3
# print(d)

# print(a is b)
# print(b is not c)

# print(a == b)
# print(b != c)

# myList = [1,2,3,4]
# yourList = myList
# ourList = myList.copy()

# print(myList is yourList)
# print(myList == yourList)

# print(myList == ourList)
# print(myList is ourList)

# if-else / Decision Making

"""
if (condition){
    code 1
    code 2
    code 3
}
code 4

if condition :
    code 1
    code 2
code 3
code 4
"""
"""
a = int(input("a: "))
count = 0
if a % 2 == 0:
    print("Even")
    count += 1
else:
    print("Odd")

print("End of the program.")
"""
"""
a = float(input("a: "))

if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")

print("End of the world.")
"""
# shorthand if can only be used if code inside each if/else block is only of one line.
# shorthand if:
"""
age = int(input("Your age: "))
if age >= 18: print("Please vote.")
print("Have a nice day, good bye!")
"""
# shorthand if-else:
"""
a = int(input("a: "))

print("Even") if a % 2 == 0 else print("Odd")

print("End of the program.")
"""
# shorthand for if-elif-else does not exist.

# There is no switch case in Python.
"""
Ask two numbers from user. Also ask for operation (+,-,* or /). Print answer accordingly.

a = float(input("a: "))
b = float(input("b: "))
operation = input("Operation (+, -, * or /): ")
"""

# Printing the score of golf game:
"""
PAR: 10

Strokes         Score
10              PAR
9 (PAR - 1)     BIRDIE
8 (PAR - 2)     EAGLE
7 (PAR - 3)     DOUBLE EAGLE
2 TO 6          TRIPLE EAGLE
(2 to PAR - 4)
1               HOLE IN ONE

11 (PAR + 1)    BOGEY
12 or 13        DOUBLE BOGEY
(PAR + 2 OR PAR + 3)
14 OR MORE      GO HOME
(PAR + 4 OR MORE)

Write a Python program that takes PAR & Strokes from user & prints the score accordingly.
"""

# HW Examples:
"""
1. A school has following grading system. Write a Python code that takes percentage of a student and display his/her grade.
below 35%       :   F
from 35 to 44   :   E
from 45 to 54   :   D
from 55 to 64   :   C
from 65 to 74   :   B
75 or more      :   A

2. Write a Python program to find whether a given year is a leap year or not. 
Test Data : 2016
Expected Output :
2016 is a leap year.

3. Write a Python program to find the largest of three numbers. 
Test Data : 12 25 52
Expected Execution:
1st Number = 12
2nd Number = 25
3rd Number = 52

52 is the largest number.

4. Write a Python program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies. 
Test Data : 
x-coordinate: 7
y-coordinate: 9
Expected Output :
The coordinate point (7,9) lies in the First quadrant.

5. Write a Python program to find the eligibility of admission for a professional course based on the following criteria: 
Eligibility Criteria : 
Marks in Maths must be atleast 65,
Marks in Phy must be atleast 55,
Marks in Chem must be atleast 50 and 
Total marks all three subject must be atleast 190 or Total in Maths and Physics >=140
Input the marks obtained in Mathematics :72 
Input the marks obtained in Physics :65 
Input the marks obtained in Chemistry :51 
Total marks of Maths, Physics and Chemistry : 188 
Total marks of Maths and Physics : 137 
The candidate is not eligible.


6. Take values of length and breadth of a rectangle from user and check if it is square or not.

7. A shop gives discount of 10% if the cost of purchased quantity is more than Rs.1000.
Ask user for quantity
Assume each item costs 100.
Calculate and print total amount to be paid by user.

8. In above program, ask user for his/her name, mobile number, quantity and price of each item, then decide whether he/she is eligible for discount and based on that print the invoice in the following format:
case 1- when customer is not eligible for discount:

------------------------Retail Invoice---------------------
Customer Name: xxxxxx
Contact Number: xxxxxx
Date of Invoice: 09-01-2022
-----------------------------------------------------------
Items               Price       Quantity        Total
item-1              50          3               150
item-2              100         4               400
item-3              40          5               200
                                                ---------
                                Final Amount:   750
----------------Thanks for shopping with us!---------------

case 2- when customer is eligible for discount:

------------------------Retail Invoice---------------------
Customer Name: xxxxxx
Contact Number: xxxxxx
Date of Invoice: 09-01-2022
-----------------------------------------------------------
Items               Price       Quantity        Total
item-1              90          3               270
item-2              100         4               400
item-3              40          10              400
                                                ---------
                                Grand Total:    1070
                                Discount:        107
                                                ---------
                                Final Amount:    963
----------------Thanks for shopping with us!---------------

9. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and years of service and print the final salary.
"""