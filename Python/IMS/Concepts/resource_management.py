"""
f = open("ourBatch.csv", "r+")

data = f.readlines()
# print(data)
# f.write("\nTest")
print(f.closed)

f.close()
print(f.closed)
"""
"""
with open("ourBatch.csv", "r+") as f:        # this is same as writing: f = open("ourBatch.csv", "r+")
    data = f.readlines()
    data.pop(0)
    print(data)
    print(f.closed)

print(f.closed)
"""

class ContextManager():
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print("Enter method called")
        self.fp = open(self.name, self.mode)
        return self.fp

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit method called")
        self.fp.close()
        # print(exc_type)
        # print(exc_value)
        # print(traceback)

name = input("File name with full path: ")
mode = input("Mode: ")

# f = ContextManager(name, mode)
with ContextManager(name, mode) as f:
    print(f.read())
print("End of the program")

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    pass