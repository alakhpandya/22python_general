"""
while True:
    a = int(input("Enter two integers:\n"))
    b = int(input())
    try:
        print(a/b)
        break
    except ZeroDivisionError:
        print("b cannot be zero, please try again...")

print("Thanks for using our program!")
print("Feel free to reach out to us for any issues...")
"""
"""
while True:
    try:
        a = int(input("Enter two integers:\n"))
        b = int(input())
        print(a/b)
        break

    # except ZeroDivisionError:
    #     print("b cannot be zero, please try again...")
    # except ValueError:
    #     print("Please enter integers only. Try again...")

    # except Exception as Harsh:
    except Exception as e:
        # print("Something went wrong, please try again...")
        # print(Harsh)
        print(e)

print("Thanks for using our program!")
print("Feel free to reach out to us for any issues...")
"""
# KeyboartInterrupt
# i = 1
# while True:
#     print(i)
#     i += 1

"""
try:
    a = int(input("Enter two integers:\n"))
    b = int(input())
    c = a/b

except ZeroDivisionError:
    # This will be exectued only if ZeroDivisionError raises
    print("b cannot be zero, please try again...")

except Exception as e:
        print(e)

else:
    # This will be executed only if exception is not raised
    print("a + b =", c)
    print("Thanks for using our program!")

finally:
    # This will be executed no matter what
    print("Feel free to reach out to us for any issues...")
"""