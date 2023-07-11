l1 = []
l1.append("a")
l1.append(None)
l1.append("b")
l1.append("c")
l1.append(None)
l1.append("d")
new = input("New object: ")
if None in l1:
    index = l1.index(None)
    l1[index] = new
print(l1)
barcode = "202307C" + str(l1.index(new) + 101)
print(barcode)