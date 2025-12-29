def is_palindrome(value):
    value=str(value)
    return value==value[::-1]

data=input("Enter a number or word: ")

if is_palindrome(data):
    print("Palindrome")
else:
    print("Not a Palindrome")
