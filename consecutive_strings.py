#! /usr/bin/python
# def longest_consec(strarr, k):
#     n = len(strarr)
#     if n == 0 or k > n or k <= 0:
#         return ''

#     longest = index = 0
#     for i in range(n - k + 1):
#         length = sum([len(s) for s in strarr[i: i + k]])
#         if length > longest:
#             longest = length
#             index = i

#     return ''.join(strarr[index: index + k])
# Best Practise
def longest_consec(strarr, k):
	result = ""
	
	if k > 0 and len(strarr) >= k:
		for index in range(len(strarr) - k + 1):
			s = ''.join(strarr[index:index+k])
			if len(s) > len(result):
				result = s
			
	return result
print longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta"