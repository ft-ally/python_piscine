#!/usr/bin/env python3

num = (input("Enter a number\n"))
integer = int(num)
i = 0
while i <= 9 :
	result = integer * i
	print(f"{i} x {integer} = {result}")
	i += 1
