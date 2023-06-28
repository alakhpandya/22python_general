"""
generate bill
"""
# DRY: Do not Repeat Yourself

class Products():
    all_products = []
    country = "India"

    def __init__(self, name, cost_price, mrp, quantity):
        self.name = name
        self.cost_price = cost_price
        self.mrp = mrp
        self.quantity = quantity
        Products.all_products.append(self)

    def show_details(self):
        print(f"------------- Details of {self.name} -------------")
        print("Category:", self.category)
        print("Cost price:", self.cost_price)
        print("MRP:", self.mrp)
        print("Stock:", self.quantity)

class Electronics(Products):
    category = "Electronics"

    def __init__(self, name, cost_price, mrp, quantity, power_option):
        super().__init__(name, cost_price, mrp, quantity)
        self.power_option = power_option

    def show_details(self):
        super().show_details()
        print("Power:", self.power_option)
        
        print("-"*55)
        print()

class Furniture(Products):
    category = "Furniture"

    def __init__(self, name, cost_price, mrp, quantity, material):
        super().__init__(name, cost_price, mrp, quantity)
        self.material = material

    def show_details(self):
        super().show_details()
        print("Material:", self.material)
        
        print("-"*55)
        print()

class Grocery(Products):
    category = "Grocery"

    def __init__(self, name, cost_price, mrp, quantity, exp_date):
        super().__init__(name, cost_price, mrp, quantity)
        self.exp_date = exp_date

    def show_details(self):
        super().show_details()
        print("Expiry Date:", self.exp_date)
        
        print("-"*55)
        print()

class Cloths(Products):
    category = "Cloths"

    def __init__(self, name, cost_price, mrp, quantity, size):
        super().__init__(name, cost_price, mrp, quantity)
        self.size = size

    def show_details(self):
        super().show_details()
        print("Size:", self.size)
        
        print("-"*55)
        print()

class Toys(Products):
    category = "Toy"

    def __init__(self, name, cost_price, mrp, quantity, age_group):
        super().__init__(name, cost_price, mrp, quantity)
        self.age_group = age_group

    def show_details(self):
        super().show_details()
        print("Age group:", self.age_group)
        
        print("-"*55)
        print()

e1 = Electronics("Asus TUF F15", 56000, 86000, 10, "Rechargable Battery")
e1.show_details()

g1 = Grocery("Kissan Ketchup", 90, 135, 50)
g1.show_details()

# Next Class: How to keep this code organized, validations, menu driven, static methods, class methods etc