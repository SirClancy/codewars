#! /usr/bin/python
# def determinant(matrix):
# 	if len(matrix) < 2: return matrix[0][0]
# 	while len(matrix) >= 2:
# 		return sum([(1 if y%2 == 0 else -1)*(matrix[0][y])*determinant([[matrix[i][j] for j in range(0,len(matrix[i])) if j != y] for i in range(1,len(matrix))]) for y in range(0,len(matrix[0]))])
			
# print determinant([ [2,5,3], [1,-2,-1], [1, 3, 4]])

# Best Practise
from datetime import datetime
startTime = datetime.now()

def determinant(m):
	a = 0
	if len(m) == 1:
		a = m[0][0]
	else:
		for n in xrange(len(m)):
			if (n + 1) % 2 == 0:
				a -= m[0][n] * determinant([o[:n] + o[n+1:] for o in m[1:]])
			else:
				a += m[0][n] * determinant([o[:n] + o[n+1:] for o in m[1:]])
				
	return a
print determinant([ [2,5,3], [1,-2,-1], [1, 3, 4]])

print(datetime.now() - startTime)
