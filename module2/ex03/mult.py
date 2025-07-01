#!/usr/bin/env python3
first = (input("Enter the first number: \n"))
second = (input("Enter the second number: \n"))
product = int(first) * int(second)
print(first + " x " + second + " = " + str(product))
if int(product) == 0 :
    print("The result is positive and negative.")
elif int(product) > 0 :
    print("The result is positive.")
else :
    print("The result is negative.")
