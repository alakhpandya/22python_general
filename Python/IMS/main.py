""" 
generate bill
"""
# DRY: Do not Repeat Yourself
from products import Products
from electronics import Electronics
from grocery import Grocery
from furniture import Furniture
from toys import Toys
from cloths import Cloths

def loadFromCSV():
    with open('database.csv', 'r') as f:
        data = f.readlines()
    for raw_obj in data:
        raw_obj = raw_obj[1 : -2].split(",")
        temp = {}
        for item in raw_obj:
            key, value = item.split(":")
            temp[key] = value[1:]
        # print(temp)
        name = temp["'name'"]
        cost_price = float(temp[" '_Products__cost_price'"])
        mrp = float(temp[" '_mrp'"])
        quantity = int(temp[" 'quantity'"])
        category_code = temp[" 'category_code'"]
        if category_code == "'E'":
            power_option = temp[" 'power_option'"]
            Electronics.createItem(name, cost_price, mrp, quantity, power_option)
        elif category_code == "'G'":
            exp_date = temp[" 'exp_date'"]
            Grocery.createItem(name, cost_price, mrp, quantity, exp_date)


# e1 = Electronics("Asus TUF F15", 56000.0, 86000, 10, "Rechargable Battery")
# e1.show_details()

# g1 = Grocery("Kissan Ketchup", 90.0, 135, 50, "12/24")
# g1.show_details()
loadFromCSV()
while True:
    print("Enter:\n1 to add new product to inventory")
    print("2 to delete a product")
    print("3 to view a product details")
    print("4 to edit a product details")
    print("5 to view the entire inventory")

    print("9 to exit\n")
    op = int(input())
    if op == 1:
        print("Enter:\n\t1 to add an Electronics item")
        print("\t2 to add a Furniture")
        print("\t3 to add Grocery")
        print("\t4 to add Cloth")
        print("\t5 to add Toy")
        item_type = int(input())    # 3
        lookup = {
            1 : Electronics.addNewItem,
            2 : Furniture.addNewItem,
            3 : Grocery.addNewItem,
            4 : Cloths.addNewItem,
            5 : Toys.addNewItem
        }
        lookup[item_type]()

    elif op == 2:
        index = Products.showInventory()
        if not index:
            print("Please add a product first!")
        else:
            removed_product = Products.all_products[index]
            Products.all_products[index] = None
            print(f"{removed_product.name} has been successfully removed!\n")

    elif op == 3:
        index = Products.showInventory()
        if not index:
            print("Please add a product first!")
        else:
            Products.all_products[index].show_details()

    elif op == 4:
        print(Products.all_products)
        index = Products.showInventory() + 1
        if not index:
            print("Please add a product first!")
        else:
            Products.all_products[index - 1].editDetails()

    elif op == 5:
        Products.showInventory()

    elif op == 9:
        Products.writeToCSV()
        break

    else:
        print("Invalid operation, please try again...")