print("Vlad Panasiuk, IT31")

first_number = float(input("Enter the first number (float): "))
operation = input("Enter the operation (+, -, *, /, //, %, **): ").strip()
second_number = float(input("Enter the second number (float): "))

if operation == "+":
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result:.4f}")
elif operation == "-":
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result:.4f}")
elif operation == "*":
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result:.4f}")
elif operation == "/":
    if second_number == 0:
        print("Error: division by zero is not allowed")
    else:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.4f}")
elif operation == "//":
    if second_number == 0:
        print("Error: division by zero is not allowed")
    else:
        result = first_number // second_number
        print(f"{first_number} // {second_number} = {result:.4f}")
elif operation == "%":
    if second_number == 0:
        print("Error: division by zero is not allowed")
    else:
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result:.4f}")
elif operation == "**":
    result = first_number ** second_number
    print(f"{first_number} ** {operation} = {result:.4f}")
else:
    print(f"Unknown operation: {operation}")