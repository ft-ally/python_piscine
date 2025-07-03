#!/usr/bin/env python3

def check(name, members):
	return members[name] == 'red'

class Family:
	def find_the_redheads(self, members):
		redheads = filter(lambda name: check(name, members), members)
		return list(redheads)

dupont_family = {
	"florian": "red",
	"marie": "blonde",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}
f = Family()
print(f.find_the_redheads(dupont_family))