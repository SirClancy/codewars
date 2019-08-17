#! /usr/bin/python

from datetime import datetime
startTime = datetime.now()
# def solution(lst):
# 	res = []
# 	if lst:
# 		tmp, i, ln = lst[0], 0, len(lst)
# 		while i < ln:
# 			tmp, j = lst[i], i
# 			while j < ln - 1 and lst[j+1] == lst[j]+1:
# 				j += 1
# 			if j - i > 1:
# 				tmp = str(lst[i]) + "-" + str(lst[j])
# 				i = j+1
# 			else:
# 				i = (j if j > i else i+1)
# 			res.append(tmp)
# 	return ",".join(str(x) for x in res)

# Best Practise
def solution(args):
	out = []
	beg = end = args[0]
	
	for n in args[1:] + [""]:        
		if n != end + 1:
			if end == beg:
				out.append( str(beg) )
			elif end == beg + 1:
				out.extend( [str(beg), str(end)] )
			else:
				out.append( str(beg) + "-" + str(end) )
			beg = n
		end = n
	
	return ",".join(out)

print solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
print(datetime.now() - startTime)