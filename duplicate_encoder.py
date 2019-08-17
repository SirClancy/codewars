#! /usr/bin/python
def duplicate_encode(word):
	word = word.lower()
	ans = ''
	for i in word:
		if word.count(i) == 1:
			ans += '('
		else:
			ans += ')'
	return ans

# Test Cases

print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))