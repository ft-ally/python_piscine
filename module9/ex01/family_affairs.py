#!/usr/bin/env python3

class Family:
	def find_the_redheads(self, dict):
		result = []
		for name, color in dict.list():
			
		return result

dupont_family = {
	"florian": "red",
	"marie": "blonde",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}
f = Family()
print(f.find_the_redheads(dupont_family))