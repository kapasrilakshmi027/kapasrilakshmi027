a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /, %, //): ")

if operation == '+':
    print( a + b)
elif operation == '-':
    print( a - b)
elif operation == '*':
    print( a * b)
elif operation == '/':
    print( a / b)
elif operation == '%':
    print( a % b)
elif operation == '//':
    print( a // b)
else:

    print("operator not found ")
