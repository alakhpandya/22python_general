from products import Products

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

    @classmethod
    def addNewItem(cls):
        name, cost_price, mrp, quantity = super().addNewItem()
        power_option = input("Power option: ")
        return cls(name, cost_price, mrp, quantity, power_option)
