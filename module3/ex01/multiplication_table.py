#!/usr/bin/env python3

num = (input("Enter a number\n"))
integer = int(num)
i = 0
while i <= 10 :
	result = integer * i
	print(f"{integer} x {i} = {result}")
	i += 1