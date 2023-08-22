from products import Products

class Furniture(Products):
    category = "Furniture"
    category_code = "F"

    def __init__(self, name, cost_price, mrp, quantity, material):
        super().__init__(name, cost_price, mrp, quantity)
        self.material = material

    def show_details(self):
        super().show_details()
        print("Material:", self.material)
        
        print("-"*55)
        print()
 
    @classmethod
    def addNewItem(cls):
        name, cost_price, mrp, quantity = super().addNewItem()
        material = input("Material: ")
        return cls(name, cost_price, mrp, quantity, material)
