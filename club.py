#! /usr/bin/python
def openOrSenior(data):
    res = []
    for i in data:
      if i[0] >= 55 and i[1] > 7:
        res.append("Senior")
      else:
        res.append("Open")
    return res

print openOrSenior([[80, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]])
print openOrSenior([[56, 23],[56, 2],[56,  8],[54, 6]])