#!/usr/bin/env python3

numbers = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
for i in numbers:
	if int(i) >= 5:
		new.append(int(i) + 2)
set =(set(new))
print(numbers)
print(set)
