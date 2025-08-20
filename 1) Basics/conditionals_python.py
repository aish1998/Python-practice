"""This is Program Tells whether a number is odd or even"""

num = int(input("Enter the value of num"))
if num > 0:
    print("The number is positive")
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative")
