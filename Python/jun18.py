
class Car:
    seating_capacity = 5        # class variable
    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel

    # creating a method
    def displayDetails(self):
        print("---------- Details of c1 ----------")
        print("Model Name:", self.name)
        print("Price:", self.price)
        print("Fuel:", self.fuel)
        print("Seating Capacity:", self.seating_capacity)
        print()

    def changeDetails(self):
        print("Enter new details:")
        self.name = input("Name: ")
        self.price = int(input("Price: "))
        self.fuel = input("Fuel: ")

    # def displayDetails(self, something):
    #     print("Something is -", something)

c1 = Car("Elantra", 2500000, "Petrol")
# c1.displayDetails("Nothing")

c2 = Car("Verna", 1200000, "Petrol")
# c1.changeDetails()
# c1.displayDetails()
c3 = Car("Fortuner", 3500000, "Diesel")
"""
Press 1 - to add a new car
2 - display details of an existing car
3 - change details of an existing car
4 - delete a car
5 - exit
"""
# Your code goes here