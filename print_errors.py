#! /usr/bin/python
# def printer_error(s):
# 	goodLetters='abcdefghijklm'

# 	errors=0
# 	totalLetters=len(s)

# 	for letter in s:
# 		if letter not in goodLetters:
# 			errors+=1

# 	return str(errors) + "/" + str(totalLetters)

# print printer_error("aaabbbbhaijjjm")
# print printer_error("aaaxbbbbyyhwawiwjjjwwm")

# best pactrise
from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

print printer_error("aaabbbbhaijjjm")
print printer_error("aaaxbbbbyyhwawiwjjjwwm")
