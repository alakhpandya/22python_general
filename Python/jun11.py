# OOP: Object Oriented Programming
# Why OOP over POP
"""
1. Easy
"""
"""
Car management system:
For every car:
stock 
model name
sale price
length
width
height
weight
ground clearance
engine
color
average
airbags
cost price
seating capacity
fuel type
"""
"""
Options:
1. Show details of any car
2. Add new car
3. Edit a car
4. Delete a car
"""
# [
#     {"model" : "s1", "stock" : 50, "price" : 600000},
# ]
# model_names = ["city s", "city sx", "c3", "c4"]
# stock = [50, 23, 21, 46]

# Python is purely an OOP language
"""
x = 5
print(type(x))
# x.upper()
y = int(5.6)
# print(x + y)
print(x.__add__(y))
a = "Hello"
b = "World"
# print(a + b)
print(a.__add__(b))
"""

# Creating a class
# class Car():
class Car:
    seating_capacity = 5        # class variable

    # creating a method
    def displayDetails(self):
        print("---------- Details of c1 ----------")
        print("Model Name:", self.name)
        print("Price:", self.price)
        print("Fuel:", self.fuel)
        print("Seating Capacity:", self.seating_capacity)
        print()


c1 = Car()
# Creating object variables
c1.name = "Elantra"
c1.price = 2000000
c1.fuel = "Diesel"
# print("---------- Details of c1 ----------")
# print("Model Name:", c1.name)
# print("Price:", c1.price)
# print("Fuel:", c1.fuel)
# print("Seating Capacity:", c1.seating_capacity)
# print()
c1.displayDetails()


c2 = Car()
c2.name = "Verna"
c2.price = 1200000
c2.fuel = "Petrol"
# print("---------- Details of c2 ----------")
# print("Model Name:", c2.name)
# print("Price:", c2.price)
# print("Fuel:", c2.fuel)
# print("Seating Capacity:", c2.seating_capacity)
# print()
c2.displayDetails()

# Deleting an object/object variable
# del c1.name
# del c1
# print("Model Name:", c1.price)
# print("Model Name:", c2.name)

# Modifying class variable
Car.seating_capacity = 9

c3 = Car()
c3.name = "Fortuner"
c3.price = 3500000
c3.fuel = "Diesel"
c3.seating_capacity = 7

# print("---------- Details of c3 ----------")
# print("Model Name:", c3.name)
# print("Price:", c3.price)
# print("Fuel:", c3.fuel)
# print("Seating Capacity:", c3.seating_capacity)
# print()
c3.displayDetails()

# print("Seating Capacity of c2:", c2.seating_capacity)
# print(c1.__dict__)
# print(c3.__dict__)

# print(c2.airbags)