#! /usr/bin/python
# def divisors(integer):
# 	arr = []
# 	for x in range(2,integer - 1): #if integer is 12
# 		if integer % x == 0:
# 			arr.append(x)

# 	if len(arr) == 0:
# 		return str(integer) + ' is prime'
# 	else:    
# 		return arr
	

# print divisors(25)
# best practise

def divisors(num):
	l = [a for a in range(2,num) if num%a == 0]
	if len(l) == 0:
		return str(num) + " is prime"
	return l

print divisors(100)