num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Modulus")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Addition =", num1 + num2)

elif choice == 2:
    print("Subtraction =", num1 - num2)

elif choice == 3:
    print("Multiplication =", num1 * num2)

elif choice == 4:
    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Cannot divide by zero.")

elif choice == 5:
    if num2 != 0:
        print("Floor Division =", num1 // num2)
    else:
        print("Cannot divide by zero.")

elif choice == 6:
    if num2 != 0:
        print("Modulus =", num1 % num2)
    else:
        print("Cannot perform modulus by zero.")

else:
    print("Invalid choice.")