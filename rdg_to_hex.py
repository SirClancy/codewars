#! /usr/bin/python
# def rgb(r, g, b):
#     def clamp(x):
#         return max(0, min(x, 255))

#     return ('%02x%02x%02x' % (clamp(r), clamp(g), clamp(b))).upper()

# Best Practise 
def rgb(r, g, b):
	round = lambda x: min(255, max(x, 0))
	return ("{:02X}" * 3).format(round(r), round(g), round(b))
	
print rgb(255, 255, 255) # returns FFFFFF
print rgb(255, 255, 300) # returns FFFFFF
print rgb(0,0,0) # returns 000000
print rgb(148, 0, 211) #retuns 9400D3