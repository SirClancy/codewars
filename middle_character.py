#! /usr/bin/python
# def get_middle(s):
#   if len(s) <= 2:
#       return s
#   if len(s) % 2 == 0:
#       return s[len(s)//2 - 1:len(s)//2 + 1]
#   else:
#       return s[len(s)//2]

# best practise
def get_middle(s):
	return s[(len(s)-1)/2:len(s)/2+1]
print get_middle("clancy")