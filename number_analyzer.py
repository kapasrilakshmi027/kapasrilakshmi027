num=int(input("Enter a number: "))

print("\n-----NNUMBER ANALYZER-----")

if num>=0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("Zero")
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")
if -9<=num<=9:
    print("It is a single-digit number")
else:
    print("It is munlti-digit number")
    
