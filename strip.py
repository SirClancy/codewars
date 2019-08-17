#! /usr/bin/python

# def solution(string, markers):
# 	lines = string.split('\n')
# 	for i, line in enumerate(lines):
# 		for marker in markers:
# 			index = line.find(marker)
# 			if index != -1:
# 				line = line[:index]
# 		lines[i] = line.rstrip(' ')
# 	return '\n'.join(lines)

# Best Practise
def solution(string,markers):
	parts = string.split('\n')
	for s in markers:
		parts = [v.split(s)[0].rstrip() for v in parts]
	return '\n'.join(parts)

print solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])