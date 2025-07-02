#!/usr/bin/env python3

first = (input("Give me the first number: "))
second = (input("Give me the second number: "))
print("Thank you!")
sum = int(first) + int(second)
min = int(first) - int(second)
quo = int(first) // int(second)
prod = int(first) * int(second)
print(f"{first} + {second} = {sum}")
print(f"{first} - {second} = {min}")
print(f"{first} / {second} = {quo}")
print(f"{first} * {second} = {prod}")

