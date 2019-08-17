#! /usr/bin/python
# def narcissistic(value):
#     return sum(int(i)**len(str(value)) for i in str(value)) == value

# best practise
def narcissistic(value):
	return value == sum(int(x) ** len(str(value)) for x in str(value))

print narcissistic(122)