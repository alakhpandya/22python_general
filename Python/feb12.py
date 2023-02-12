# for-else
"""
n = int(input("n: "))
for i in range(2, n):
    if n % i == 0:
        print("Not Prime.")
        break
else:
    print("Prime.")
"""
"""
1. Update the above program so that it asks two numbers from user & prints all the prime numbers between them(including both).
"""
"""
a = int(input("Enter two integers:\n"))
b = int(input())
print(f"Prime numbers between {a} & {b}:")
for n in range(a, b+1):
    if n <= 1:
        continue
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            break
    else:
        print(n)
"""
# Programming Excercises:
"""
1. Ask user for an integer & print whether it's a perfect number or not.
    eg, 56
    factors of 56: 1 + 2 + 4 + 7 + 8 + 14 + 28 = 64 != 56
    eg, 28
    factors of 28: 1 + 2 + 4 + 7 + 14 = 28
2. Ask two integers from user and print all the perfect numbers between those two numbers
3. Ask user for a 3-digit integer & print whether it's an Armstrong number or not. A 3-digit integer is an Armstrong number if sum of cubes of all of its digits equals to the number itself.
    eg, 153:
    (1^3) + (5^3) + (3^3) = 153
"""
"""
a = int(input("Enter two integers:\n"))
b = int(input())
for n in range(a, b+1):
    # n = int(input("n : "))
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    if sum(factors) == n:
        # print("Perfect.")
        print(n)
    # else:
    #     print("Not Perfect.")
"""
# HW:
"""
4. Ask user for a an integer & print whether it's an Armstrong number or not. An x-digit integer is an Armstrong number if sum of x-powers of all of its digits equals to the number itself.
    eg, 1634:
    (1^4) + (6^4) + (3^4) + (4^4)
    = 1 + 1296 + 81 + 256
    = 1634
5. Ask two integers from user and print all the Armstrong numbers between those two numbers
6. Given an array of integers A, find and return the minimum elements to be removed such that in the resulting array the sum of any two adjacent values is even.

Input Format:
The only argument given is the integer array A.
Output Format:
Return the minimum number of elements to be removed.

Program Constraints:
1 <= length of the array <= 100000
-10^9 <= A[i] <= 10^9 

Examples:
Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    2

Input 2:
    A = [5, 17, 100, 11]
Output 2:
    1
"""


# Next Class: List Comprehension