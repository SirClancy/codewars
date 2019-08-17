#! /usr/bin/python
# def valid_parentheses(string):
#     brac = 0
#     for i in string:
#         if i == '(':
#             brac += 1
#         elif i == ')':
#             brac -= 1
#         if brac < 0:
#             return False
#     if brac != 0:
#         return False
#     else:
#         return True
#2nd ans
# def valid_parentheses(string):
# 	# your code here

# 	stack = []
# 	for s in string:
# 		if(s == '('):
# 			stack.append(s)
# 		elif(s == ')'):
# 			try:
# 				stack.pop()
# 			except:
# 				return False

# 	if(len(stack) == 0):
# 		return True
# 	else:
# 		return False

# Best practise
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

# Test Cases

print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))