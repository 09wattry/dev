def digitss():	
	digits = '0123456789'
	result = ''

	for digit in digits:
		result = result + digit * 2

	print(result)
	
def thirty():
	message = 'Happy 29th!'
	new_message = ''

	for char in message:
		new_message = new_message + str((int(char) + 1) % 10)

	print(new_message)


def common_chars(s1, s2):
	'''(str, str) -> str

	Return a new string containing all characters from s1 that     appear at leastonce in s2. The characters in the result        will appear in the same order asthey appear in s1.

	>>> common_chars('abc', 'ad')
	'a'
	>>> common_chars('a', 'a')
	'a' 
	>>> common_chars('abb', 'ab')
	'abb' 
	>>> common_chars('abracadabra', 'ra')
	'araaara'
	'''


	res = ''

	for ch in s1:
		if ch in s2:
			res = res + ch

	return res

print(common_chars('abracadabra', 'ra'))