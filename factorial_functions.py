def factorial(num):
    if num<0:
        return"Factorial not defined for negative numbers"
    
    fact=1
    for i in range(1,num+1):
        fact*= i
    return fact

number=int(input("Enter a number: "))

print("Factorial:",factorial(number))
