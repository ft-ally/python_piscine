#!/usr/bin/env python3
i = 0
while i <= 10 :
	print(f"Table of {i}:", end=" ")
	j = 0
	while j <= 10 :
		product = i * j
		print(f"{product}", end=" ")
		j +=1
	print("")
	i += 1
