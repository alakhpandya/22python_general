from products import Products

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

    @classmethod
    def addNewItem(cls):
        name, cost_price, mrp, quantity = super().addNewItem()
        age_group = input("Age group: ")
        return cls(name, cost_price, mrp, quantity, age_group)
