# f = open("C:\\Users\\Alakh Pandya\\Desktop\\Batches\\22python_general\\Python\\IMS\\Concepts\\ourBatch.txt")
# data = f.read()
# print(type(data))
# print(data)

# data = f.read(30)
# print(data)

# line1 = f.readline()
# print(line1)

# print(f.read(25))
# print(f.read(2))
# print(f.read())

# print(f.tell())
# f.seek(50)
# print(f.tell())
# print(f.read())

# l = f.readline()
# m = f.readline()
# print(l)
# print(m)

# n = f.readlines()
# print(n)
# f.close()

"""
f = open("D:\\ourBatch.txt")
data = f.readlines()
# print(data)
f.close()

roll = int(input("Roll no: "))
stu_info = data[roll]


f = open("C:\\Users\\Alakh Pandya\\Desktop\\Batches\\22python_general\\Python\\IMS\\Concepts\\ourBatch.txt")

# d1 = f.readlines()
# print(f.read())
# f.write("\n12")
# print(f.writable())
# print(f.readable())

f.close()
"""

# File opening syntax:
"""
f = open('entire file path including its name with extension', 'Mode1Mode2')
f.close()

Mode 1  Name            Description                                             Mode 2  Name
r       Read            Opens the file for reading only                         t       Text            Default Mode
                        Cursor is placed at the begining of the file.
                        Does not erase the content of the file
                        Raises FileNotFoundError if file does not exist

w       Write           Opens the file for writing only                         b       Binary
                        Erases entire content of the file at the time of opening
                        Creates file if it does not exist
                        Cursor is placed at the begining of the file.

a       Append          Opens the file for writing only
                        Does not erase the content of the file
                        Creates file if it does not exist
                        Cursor is placed at the end of the file.

x       Exclusively     Creates the file and opens it for writing if it does not exist
        Create          Raises FileExistsError if the file already exists
                        Cursor is placed at the end of the file.

r+      Read+           Opens the file for reading and writing both
                        Cursor is placed at the begining of the file.
                        Does not erase the content of the file
                        Raises FileNotFoundError if file does not exist

w+      Write+          Opens the file for reading and writing both
                        Erases entire content of the file at the time of opening
                        Creates file if it does not exist
                        Cursor is placed at the begining of the file.

a+      Append+         Opens the file for reading and writing both
                        Does not erase the content of the file
                        Creates file if it does not exist
                        Cursor is placed at the end of the file.
"""

# f = open("D:\\ourBatch.txt")        OR
f = open("D:\\ourBatch.txt", "rt")

# f = open("D:\\ourBatch.txt", "w")   OR
# f = open("D:\\ourBatch.txt", "wt")

# f = open("D:\\ourBatch.txt", "at")      OR
# f = open("D:\\ourBatch.txt", "a")

# f = open("D:\\ourBatch.txt", "a+b")
# f = open("D:\\ourBatch.txt", "a+")    # as good as "a + t"
f.close()

# Next Class: Remaining concepts of file handling, Resolving '\t' problem, back to project

# Comma Seperated Values: csv