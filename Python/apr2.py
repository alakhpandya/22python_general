# Misc topics around functions

'''
Multi
Line
Comments 1
'''

"""
Multi
Line
Comments 2
"""

# a = 10
# b = 15.56
# c = "my string"

# d = """He said "I don't mind giving you my car"."""
'''
e = """An Android app is a software application that is built for mobile applications which are run mainly on Android platforms. As Android OS dominates most of the mobile app development market, to leverage the benefits of Android application development has become a necessity for all business ends. Android apps offers tremendous strategic and operational benefits as it addresses a higher range of audience and gain immense popularity.

iSyncEvolution is a trusted name as a mobile app development company that provides robust, out-of-the-box Android app development services. We provide you with custom Android app designs and streamlined development solutions for all your business needs. With the aid of our certified team of developers, you can be assured of a full range of innovative solutions to enhance your market strategy and user-friendly app design. Our Android app designers deliver brilliant apps with a smooth user experience. We build interactive and top-end apps that guarantee high functionality.

Our company provides top-notch services, irrespective of the size of your enterprise. Our Android app developers offer a robust roadmap for personalized app development for enterprises with smart performance and technical scalability. iSyncEvolution presents powerful app features for a successful integrated user experience while conceptualizing, designing, building and maintaining the tailor-made android apps. Our successful operations in Australia, Canada, India, UAE, UK, and the USA are testimony to our quality apps on the Android platform.

Make your Android app enticing and inventive with our Android app development services!

The niche that we have created for ourselves in the market is due to our comprehensive Android app development sol"""
'''
# Docstring

# def myFunc(a,b,c,d,e):
#     # print("Hello")
#     '''This function is finding average of five integers'''
#     """Another Way to write Docstring"""
#     "This is also a docstring"
#     'This too.'
#     return (a + b + c + d + e)/5

# from random import normalvariate, uniform

# print(normalvariate.__doc__)

# uniform()
# myFunc()


# Rules for function:
"""
We put () after a function if and only if we want to call it.
"""
"""
def average(a, b):
    print((a + b)/2)
    return (a + b)/2
"""
# average(5,6)

# deleting a function
# del average(10,15)

# Copying a function:
# average_of_two = average
# print(average_of_two)



# Passing a collection to a function

# def sum_of_squares(x):
#     sum = 0
#     for number in x:
#         sum = sum + (number**2)
#     return sum

# myList = [2,5,6,8,10,14]
# print(sum_of_squares(myList))
# # sum_of_squares(9)
# myTuple = (3,4,5,6,7)
# print(sum_of_squares(myTuple))
# mySet = {3,4,5,6,7}
# print(sum_of_squares(mySet))

"""
def calculatePercentage(result):
    total_marks = 0
    for marks in result.values():
        total_marks += marks
    percentage = total_marks/len(result)
    return percentage


marks_sheet = {"C" : 80, "C++" : 75, "Java" : 85}
print(calculatePercentage(marks_sheet))
"""

# Upcoming sessions: positional, default, variable & keyword arguments, nesting of functions, scope of a function, local variable, global variable, global keyword, lambda functions, some useful built in functions, Recursive functions