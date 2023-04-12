# Upcoming sessions: passing collections in functions, positional, default, variable & keyword arguments, passing a function as argument to other function, nesting of functions, scope of a function, local variable, global variable, global keyword, lambda functions, some useful built in functions, Recursive functions

# passing collections in functions
"""
def avg(a):
    return sum(a)/len(a)

numberList=[1,2,3,4]
numTuple = (1,2,3,4,5)
nSet = {10, 9, 8, 7}
print(avg(numberList))
print(avg(numTuple))
print(avg(nSet))
myDictionary = {
   20 : "Sub-1",
   30 : "Sub-2",
   40 : "Sub-3"
}
print(avg(myDictionary))
yourDictionary = {
   "Maths" : 30,
   "Science" : 40,
   "Languages" : 50
}
print(avg(yourDictionary.values()))
"""

# positional & default arguments
"""
def func1(a, b, c = 10):
    print(a)
    print(b)
    print(c)

func1(5, 7, 9)
"""
"""
def avg(a):
    return sum(list1)/len(list1)

list1=[]
n=int(input("enter a number of loop"))
for i in range(n):
    num=int(input('enter a number:'))
    list1.append(num)
print(list1)
print(avg(list1))
"""

# Variable length arguments
"""
def func1(a, b, c = 10, *args):
    print(args)
    print(type(args))
    print(a)
    print(b)
    print(c)

func1(1,2,3,4,5,6,7,8,9,10)
func1(1,2)
"""

# keyword arguments
"""
def func2(a = 10, b = 20, *args):
    pass

func2(Physics = 25, Maths = 30, Sanskrit = 40)


def func3(**kwargs):
    print(kwargs)

func3(Physics = 25, Maths = 30, Sanskrit = 40)


def func(a,b):
    print("a =", a)
    print("b =", b)

func(b=10,a=29)
"""
# Rule:
# First comes ALL POSITIONAL ARGUMENTS, then comes ALL DEFAULT ARGUMENTS, then comes *args, finally comes **kwargs

# Passing a function as argument to other function
"""
def fact(n):
    # Write a code that returns factorial of n here
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def avg(a, b, c, d, e):
    # Write code that returns average of a, b, c, d & e here
    return (a + b + c + d + e)/5
"""
# Main program:
# Ask 5 integers from user & print average of their factorials using above two functions.
# p = int(input())
# q = int(input())
# r = int(input())
# s = int(input())
# t = int(input())
"""
f1 = fact(p)
f2 = fact(q)
f3 = fact(r)
f4 = fact(s)
f5 = fact(t)
print(avg(f1, f2, f3, f4, f5))
"""
# print(avg(fact(p), fact(q), fact(r), fact(s), fact(t)))
# print(avg(fact(int(input())), fact(int(input())), fact(int(input())), fact(int(input())), fact(int(input()))))


# nesting of functions
"""
def avg(a, b, c, d, e):
    def fact(n):
        f = 1
        for i in range(1, n+1):
            f *= i
        return f
    return (fact(a) + fact(b) + fact(c) + fact(d) + fact(e))/5

p = int(input())
q = int(input())
r = int(input())
s = int(input())
t = int(input())

print(avg(p, q, r, s, t))
"""

# Scope of a variable, local variables, global variables & global keyword, lambda functions, some useful built in functions, Recursive functions

# HW:
"""
1. Problem Description: Given a name A as input. Print "Hello A", where A is the name in input.

    Problem Constraints:
    1 <= len(A) <= 15
    Characters in A are in lowercase English Alphabets.

    Input Format:
    There is a single input line, which is the string A.

    Output Format:
    Print in a single line "Hello A" without quotes.

    Examples 
    Input 1:
    Ram
    Output 1:
    Hello Ram

    Input 2:
    Shyam
    Output 2:
    Hello Shyam

2. Problem Description: Print the first five letters of the English alphabet i.e. A, B, C, D and E.

    Output Format
    Print the characters in separate lines.

    Example Output
    A
    B
    C
    D
    E

3. Problem Description: Given two numbers A and B. Concatenate the two numbers and print it.

    Problem Constraints
    1 <= A, B <= 104

    Input Format:
    There are two input lines
    The first line has a single integer A.
    The second line has a single integer B.

    Output Format
    Print in a single line the concatenated number.

    Examples 
    Input 1:
    4
    5
    Output 1:-
    45

    Input 2:
    16
    2
    Output 2:-
    162

4. Problem Description: Given two names A and B as input, print "A says Hi to B", where A and B are the names in input.

    Problem Constraints
    1 <= len(A), len(B) <= 15
    Characters in A and B are in lowercase English Alphabets.

    Input Format:
    There are two input lines
    The first line has a string A.
    The second line has a string B.

    Output Format:
    Print in a single line A says Hi to B.

    Examples 
    Input:
    Ram
    Shyam

    Output:
    Ram says Hi to Shyam

5. What will be the output of the following snippet of python code?

    print(type(1)) 
    print(type(str(True) + '1')) 
    print(type(float(int(0.1)))) 
    print(type(True)) 
    print(type(Float(1))) 

    a.
    int
    str
    float
    bool
    Error

    b.
    str
    str
    float
    int
    float

    c.
    int
    int
    float
    int
    float

    d.
    The code will produce an error and nothing will be printed.
"""