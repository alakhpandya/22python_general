from grocery import Grocery

class Flour(Grocery):
    subcategory = 'Flour'

if __name__ == "__main__":
    f1 = Flour('Royal', 50.5, 75, 1, 12/2024)
    f1.show_details()