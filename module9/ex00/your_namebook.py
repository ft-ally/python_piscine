#!/usr/bin/env python3

class Array():
	def array_of_names(self, dict):
		result=[]
		for first, last in dict.items():
			full_name = first.capitalize() + " " + last.capitalize()
			result.append(full_name)
		return result

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brinacier"
}
a = Array()
print(a.array_of_names(persons))