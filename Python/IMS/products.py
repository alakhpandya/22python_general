import datetime

class Products():
    all_products = []
    country = "India"

    def __init__(self, name:str, cost_price, mrp, quantity:int):
        assert isinstance(name, str), "Name should be a string..."
        self.name = name

        assert isinstance(cost_price, float), "Cost Price should be a Float..."
        self.cost_price = cost_price
        assert isinstance(mrp, float) or isinstance(mrp, int), "MRP should be a Float..."
        self.mrp = mrp
        
        assert isinstance(quantity, int), "Qunatity should be integer."
        assert quantity > 0, "Quantity should be greater than 0!"
        self.quantity = quantity
        Products.all_products.append(self)
        self.generateBarcode()

    def generateBarcode(self):
        # Format: YYYYMMCXXXX
        """
        YYYY: Year of purchase in 4 digits (to be fetched from the system date using datetime module)
        MM: Month of purchase in 2 digits (to be fetched from the system date using datetime module)
        C: category_code (E/G/F/T/C)
        XXXX: Index number in the list + 100
        """
        purchase_year = datetime.datetime.today().year
        purchase_month = datetime.datetime.today().month
        index = str(len(Products.all_products) + 100)
        self.barcode = str(purchase_year)+str(purchase_month)+ self.category_code + index
        # barcode: 202307E102

    def show_details(self):
        print(f"------------- Details of {self.name} -------------")
        print("Category:", self.category)
        print("Cost price:", self.cost_price)
        print("MRP:", self.mrp)
        print("Stock:", self.quantity)
        print("Barcode:", self.barcode)

    @staticmethod
    def addNewItem():
        print("Enter the following details:")
        name = input("Name: ")
        cost_price = float(input("Cost Price: "))
        mrp = float(input("MRP: "))
        quantity = int(input("Quantity: "))
        return name, cost_price, mrp, quantity
    
    @staticmethod
    def showInventory():
        print("SrNo\t\tItem Name")
        for item in Products.all_products:
            print(f"{item.barcode}\t{item.name}")
        barcode = input("Enter barcode no: ")
        index = int(barcode[-3:]) - 101
        return index

    def editDetails(self):
        print("Enter new details (Press 'Enter' to keep old detail):")
        self.name = input("Item name:")
        self.category = input("Category:")
        self.cost_price = float(input("Cost price:"))
        self.mrp = float(input("MRP:"))
        self.quantity = int(input("Stock:"))
        self.barcode = input("Barcode:")

if __name__ == '__main__' :
    # p1 = Products("1234", 35.5, 50.5, 10)
    # p1.show_details()
    # p2 = Products("Sample product 1", 35.5, 50.5, 10)
    # p2.show_details()
    # s1 = 123
    # print(isinstance(s1, str))
    pass