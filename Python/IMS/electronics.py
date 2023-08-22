# Next Class: Polymorphism, File Handling, CSV Module, Exception Handling, Resource Management, Come back to this project

from products import Products

class Electronics(Products):
    category = "Electronics"
    category_code = "E"

    def __init__(self, name, cost_price, mrp, quantity, power_option):
        super().__init__(name, cost_price, mrp, quantity)
        self.power_option = power_option
        self.__offers = 5                # private


    def show_details(self):
        # print(f"------------- Details of {self.name} -------------")
        # print("Category:", self.category)
        # print("Cost price:", self.__cost_price)     # private variable
        # print("Cost price:", self._Products__cost_price)     # name mangling
        # print("MRP:", self._mrp)                    # protected variable
        # print("Stock:", self.quantity)
        # print("Barcode:", self.barcode)
        
        super().show_details()
        print("Power:", self.power_option)

        print("-"*55)
        print()

    # getter:
    @property
    def schemes(self):
        return self._Electronics__offers
    
    # setter:
    @schemes.setter
    def schemes(self, newValue):
        self._Electronics__offers = newValue

    @classmethod
    def addNewItem(cls):
        name, cost_price, mrp, quantity = super().addNewItem()
        power_option = input("Power option: ")
        return cls(name, cost_price, mrp, quantity, power_option)

    def editDetails(self):
        super().editDetails()
        power = input(f"Power\t{self.power_option}:\t")
        if power != "": self.power_option = power


if __name__ == "__main__":
    e1 = Electronics('USB Charger', 90.90, 300, 20, "N/A")
    # e1.show_details()
    print(e1.schemes)
    e1.schemes = 7
    print(e1.schemes)
