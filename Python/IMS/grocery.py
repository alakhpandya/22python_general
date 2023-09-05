from products import Products

class Grocery(Products):
    category = "Grocery"
    category_code = "G"

    def __init__(self, name, cost_price, mrp, quantity, exp_date):
        super().__init__(name, cost_price, mrp, quantity)
        self.exp_date = exp_date

    def show_details(self):
        super().show_details()
        print("Expiry Date:", self.exp_date)
        
        print("-"*55)
        print()
    
    @classmethod
    def addNewItem(cls):
        name, cost_price, mrp, quantity = super().addNewItem()
        exp_date = input("Expiry date: ")
        return cls(name, cost_price, mrp, quantity, exp_date)

    @classmethod
    def createItem(cls, name, cost_price, mrp, quantity, exp_date):
        return cls(name, cost_price, mrp, quantity, exp_date)