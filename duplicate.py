#! /usr/bin/python
# def duplicate_count(text):
# 	# Your code goes here
# 	text_set = set(list(text.lower()))
# 	count = 0
# 	for i in text_set:
# 		if text.lower().count(i) > 1:
# 			count += 1
# 	return count

# Test Cases
# Best Practise
def duplicate_count(s):
	return len([c for c in set(s.lower()) if s.lower().count(c)>1])

print duplicate_count("abcde")
print duplicate_count("abcdea")
print duplicate_count("indivisibility")