#!/usr/bin/env python3
num = (input("Enter a number less than 25\n"))
inp = int(num)
if inp <= 25 :
	while inp <= 25 :
		print("Inside the loop, my variable is " + str(inp))
		inp += 1
else :
	print("Error")
