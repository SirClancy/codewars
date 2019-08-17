#! /usr/bin/python
# def unique_in_order(iterable):
# 	newList = []
# 	for item in iterable:
# 		if len(newList) < 1 or not item == newList[len(newList) - 1]:
# 			newList.append(item)
# 	return newList


# best practise
def unique_in_order(iterable):
	result = []
	prev = None
	for char in iterable[0:]:
		if char != prev:
			result.append(char)
			prev = char
	return result

print unique_in_order('AAAABBBCCDAABBB')
print unique_in_order('ABBCcAD')
