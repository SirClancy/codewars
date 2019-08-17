#! /usr/bin/python
from collections import OrderedDict

# def format_duration(inp_num):
#     if inp_num == 0: return 'now'
#     result = ""
#     d = OrderedDict([
#                      ('year', inp_num / (60*60*24*365)), 
#                      ('day', inp_num % (60*60*24*365) / (60*60*24)),
#                      ('hour', inp_num % (60*60*24*365) % (60*60*24) / (60*60)),
#                      ('minute', inp_num % (60*60*24*365) % (60*60*24) % (60*60) / 60),
#                      ('second', inp_num % (60*60*24*365) % (60*60*24) % (60*60) % 60)
#                    ])

#     for k,v in d.items():
#         if v == 0: continue
#         elif v == 1: result += "1 " + k + ", "
#         else: result += str(v) + " " + k + "s, "
#     result = result[:len(result)-2]
#     result_reversed = result[::-1]
#     if result_reversed.find(',') != -1:
#         result = result_reversed[:result_reversed.find(',')] + "dna " + result_reversed[result_reversed.find(',')+1:]
#         return result[::-1]
#     else: return result
# BEST PRACTISE
times = [("year", 365 * 24 * 60 * 60), 
		 ("day", 24 * 60 * 60),
		 ("hour", 60 * 60),
		 ("minute", 60),
		 ("second", 1)]

def format_duration(seconds):

	if not seconds:
		return "now"

	chunks = []
	for name, secs in times:
		qty = seconds // secs
		if qty:
			if qty > 1:
				name += "s"
			chunks.append(str(qty) + " " + name)

		seconds = seconds % secs

	return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]

print format_duration(1)