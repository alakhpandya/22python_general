from products import Products

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

    @classmethod
    def addNewItem(cls):
        name, cost_price, mrp, quantity = super().addNewItem()
        size = input("Size: ")
        return cls(name, cost_price, mrp, quantity, size)
