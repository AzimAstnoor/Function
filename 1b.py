from newt import main
print(" Select the Operation:\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division")
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
   print(num1, "+", num2, "=", main.addition(num1, num2))
elif choice == '2':
   print(num1, "-", num2, "=", main.subtraction(num1, num2))
elif choice == '3':
   print(num1, "*", num2, "=", main.multiplication(num1, num2))
elif choice == '4':
   print(num1, "/", num2, "=", main.division(num1, num2))
else:
   print("Invalid input")