#! /usr/bin/python
# def first_non_repeating_letter(string):
# 	#your code here
# 	print string
# 	list = [i.lower() for i in string]
# 	print list
# 	for i in range(len(list)):
# 		if list.count(list[i]) == 1:
# 			return string[i]
# 	return ""

# Best Practise

def first_non_repeating_letter(string):
	string_lower = string.lower()
	for i, letter in enumerate(string_lower):
		if string_lower.count(letter) == 1:
			return string[i]
			
	return ""

print first_non_repeating_letter('Basic Tests')
