#! /usr/bin/python
# plusminus_value = {'+': 1, '-': -1}
# lessmore_value = {'<': -1, '>': 1}
# brc_value = {'[': 1, ']': -1}
# brc_pair = {'[': ']', ']': '['}


# def brain_luck(code, inputs):
# 	inputl = list(inputs)
# 	code_ptr = data_ptr = 0
# 	data = [0]
# 	output = ''

# 	while code_ptr != len(code):
# 		inst = code[code_ptr]

# 		if inst == '.':
# 			output += chr(data[data_ptr])

# 		if inst == ',':
# 			data[data_ptr] = ord(inputl.pop(0))

# 		if inst in lessmore_value:
# 			data_ptr += lessmore_value[inst]
# 			if data_ptr == len(data):
# 				data.append(0)

# 		if inst in plusminus_value:
# 			data[data_ptr] += plusminus_value[inst]
# 			data[data_ptr] %= 256

# 		if (inst == '[' and data[data_ptr] == 0) or (inst == ']' and data[data_ptr] != 0):
# 			direction = bracket_counter = brc_value[inst]
# 			while not (code[code_ptr] == brc_pair[inst] and bracket_counter == 0):
# 				code_ptr += direction
# 				if code[code_ptr] in brc_value:
# 					bracket_counter += brc_value[code[code_ptr]]

# 		code_ptr += 1

# 	return output


# Best Practise
from collections import defaultdict

def brain_luck(code, input):
	p, i = 0, 0
	output = []
	input = iter(input)
	data = defaultdict(int)
	while i < len(code):
		c = code[i]
		if c == '+': data[p] = (data[p] + 1) % 256
		elif c == '-': data[p] = (data[p] - 1) % 256
		elif c == '>': p += 1
		elif c == '<': p -= 1
		elif c == '.': output.append(chr(data[p]))
		elif c == ',': data[p] = ord(next(input))
		elif c == '[':
			if not data[p]:
				depth = 1
				while depth > 0:
					i += 1
					c = code[i]
					if c == '[': depth += 1
					elif c== ']': depth -= 1
		elif c == ']':
			if data[p]:
				depth = 1
				while depth > 0:
					i -= 1
					c = code[i]
					if c == ']': depth += 1
					elif c == '[': depth -= 1
		i += 1
	return ''.join(output)





# Two numbers multiplier
print brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)),chr(72)

# Echo until byte(255) encountered
print brain_luck(',+[-.,+]', 'Codewars' + chr(255)),'Codewars';

# Echo until byte(0) encountered
print brain_luck(',[.[-],]', 'Codewars' + chr(0)),'Codewars';
