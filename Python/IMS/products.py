class Products():
    all_products = []
    country = "India"
    category = None

    def __init__(self, name:str, cost_price, mrp, quantity:int):
        assert isinstance(name, str), "Name should be a string..."
        self.name = name
        self.cost_price = cost_price
        self.mrp = mrp
        assert isinstance(quantity, int), "Qunatity should be integer."
        assert quantity > 0, "Quantity should be greater than 0!"
        self.quantity = quantity
        Products.all_products.append(self)

    def show_details(self):
        print(f"------------- Details of {self.name} -------------")
        print("Category:", self.category)
        print("Cost price:", self.cost_price)
        print("MRP:", self.mrp)
        print("Stock:", self.quantity)

    @staticmethod
    def addNewItem():
        print("Enter the following details:")
        name = input("Name: ")
        cost_price = float(input("Cost Price: "))
        mrp = float(input("MRP: "))
        quantity = int(input("Quantity: "))
        return name, cost_price, mrp, quantity

if __name__ == '__main__' :
    p1 = Products("1234", 35.5, 50, 10)
    p1.show_details()
    # s1 = 123
    # print(isinstance(s1, str))