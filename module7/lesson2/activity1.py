name = "Penguin"
age = 15
is_student = True
weight = 38.5


print("Name:", name)
print("Data type of Name is", type(name))
print("Age:", age)
print("Data type of age is", type(age))
print("is_student :", is_student)
print("Data Type of is_student is", type(is_student))
print("Weight:", weight)
print("Data Type of weight is", type(weight))

print("/n After Type casting....")
age = str(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of Weight is", type(weight))