#!/usr/bin/env python3

age = (input("Please tell me your age: "))
print(f"You are currently", age, "years old.")
i = 10
while i <= 30 :
	new_age = int(age) + int(i)
	print(f"In {i} years, you'll be {str(new_age)} years old.")
	i += 10