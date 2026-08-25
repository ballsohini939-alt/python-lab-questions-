name = input("Enter your name: ")
age = int(input("Enter your age: "))
percentage = float(input("Enter your percentage: "))
student_input = input("Are you a student? (True/False): ")

if student_input == "True":
    is_student = True
else:
    is_student = False

print("\n--- Details and Data Types ---")

print("Name:", name)
print("Data Type:", type(name))

print("Age:", age)
print("Data Type:", type(age))

print("Percentage:", percentage)
print("Data Type:", type(percentage))

print("Is Student:", is_student)
print("Data Type:", type(is_student))