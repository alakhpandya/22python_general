# f = open('newAdmissions.csv', 'w')
# f.write('\n12,Devanshi,Student')
# f.write('\n13,Harsh,Mentor')
# f.close()

# f = open('latestAdmissions.csv', 'r')

# f.close()
"""
f = open('ourBatch.csv', 'r')
data = f.readlines()
f.close()

# print(data)
data.append('\n12,Devanshi,Student')
data.append('\n13,Harsh,Mentor')

f = open('ourBatch.csv', 'w')
f.writelines(data)
f.close()
"""
"""
f = open('ourBatch.csv', 'r')
data = f.readlines()
f.close()

roll = int(input("Roll no: "))
student_info = data[roll].strip().split(',')
roll_no, name, role = student_info
print(f"------------ Details of Roll no: {roll_no} ------------")
print("Name:", name)
print("Role:", role)
"""

# f = open('ourBatch.csv', 'a')
# f.write('\nNew student')
# f.close()

# f = open('ourBatch.csv', 'x')
# f.close()

# f = open('ourBatch.csv', 'r+')
# f.seek()
# f.read()
# print(f.tell())
# f.write('New student')
# f.close()
