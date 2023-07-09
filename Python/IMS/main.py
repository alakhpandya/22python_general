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

e1 = Electronics("Asus TUF F15", 56000.0, 86000, 10, "Rechargable Battery")
# e1.show_details()

g1 = Grocery("Kissan Ketchup", 90.0, 135, 50, "12/24")
# g1.show_details()

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
        pass

    elif op == 3:
        index = Products.showInventory()
        Products.all_products[index].show_details()

    elif op == 4:
        index = Products.showInventory()
        Products.all_products[index].editDetails()

    elif op == 5:
        pass

    elif op == 9:
        break

    else:
        print("Invalid operation, please try again...")

# Next Class: Abstraction, Encapsulation, Polymorphism & remaining menu options