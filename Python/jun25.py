# 4 Pillars of OOP: Inheritance, Polymorphism, Abstraction, Encapsulation
# inheritance

# Single/single level/simple inheritance
"""
class Father():
    vehicle = "car"

    def showProperties(self):
        print(f"Vehicle of {self.name}:", self.vehicle)

class Child(Father):
    pass


f1 = Father()
f1.name = "Anuj"
# print(f1.vehicle)
f1.showProperties()

c1 = Child()
c1.name = "Moksh"
# print(c1.vehicle)
c1.showProperties()
"""

# Multi-level inheritance
"""
class Father():
    vehicle = "Honda City"
    profession = "Lawyer"
    home = "5 BHK"

    def showProperties(self):
        print(f"Vehicle of {self.name}:", self.vehicle)
        print(f"Profession of {self.name}:", self.profession)
        print(f"Home of {self.name}:", self.home)

class Child(Father):
    profession = "Scrum Master"
    vehicle = "Fortuner"

class GrandChild(Child):
    profession = "Student"

f1 = Father()
f1.name = "Harshad"

c1 = Child()
c1.name = "Anuj"
# c1.showProperties()

gc1 = GrandChild()
gc1.name = "Moksh"

gc1.showProperties()
"""
# MRO: Method Resolution Order

# Hierachical Inheritance
"""
class Father():
    vehicle = "Honda City"
    profession = "Lawyer"
    home = "5 BHK"

    def showProperties(self):
        print(f"Vehicle of {self.name}:", self.vehicle)
        print(f"Profession of {self.name}:", self.profession)
        print(f"Home of {self.name}:", self.home)

class Child1(Father):
    profession = "Scrum Master"
    vehicle = "Fortuner"

class Child2(Father):
    vehicle = "XUV700"

f1 = Father()
f1.name = "Harshad"

c1 = Child1()
c1.name = "Anuj"
# c1.showProperties()

c2 = Child2()
c2.name = "Neepa"
"""

# Hybrid Inheritance
"""
class Father():
    vehicle = "Honda City"
    profession = "Lawyer"
    home = "5 BHK"

    def showProperties(self):
        print(f"Vehicle of {self.name}:", self.vehicle)
        print(f"Profession of {self.name}:", self.profession)
        print(f"Home of {self.name}:", self.home)

class Child1(Father):
    profession = "Scrum Master"
    vehicle = "Fortuner"

class Child2(Father):
    vehicle = "XUV700"

class GrandChild1(Child1):
    profession = "Student"

class GrandChild2(Child2):
    profession = "Data Scientist"

f1 = Father()
f1.name = "Harshad"

c1 = Child1()
c1.name = "Anuj"
# c1.showProperties()

c2 = Child2()
c2.name = "Neepa"
"""

# Multiple Inheritance
"""
class Father():
    vehicle = "Honda City"
    profession = "Lawyer"
    home = "5 BHK"

    def showProperties(self):
        print(f"Vehicle of {self.name}:", self.vehicle)
        print(f"Profession of {self.name}:", self.profession)
        print(f"Home of {self.name}:", self.home)
        print(f"Hobby of {self.name}:", self.hobby)

class Mother():
    hobby = "Trekking"
    profession = "Teacher"

class Child1(Father, Mother):
    pass

class Child2(Mother, Father):
    pass

# Diamond Problem
# class GrandChild(Child1, Child2):
#     pass

c1 = Child1()
c1.name = "Anuj"
# c1.showProperties()

c2 = Child2()
c2.name = "Neepa"
# c2.showProperties()

# gc1 = GrandChild()
# gc1.showProperties()
"""