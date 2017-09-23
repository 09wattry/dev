def test(s1, s2):
	digits = '0123456789'	
	result = 0

	for digit in digits:
		result = result + int(digit)
	
	print(result)


if __name__ == "__main__":
	print(test('abracadabra', 'ra'))