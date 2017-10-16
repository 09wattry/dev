def is_palindrome_v3(s):
	""" (str) -> bool

	Return True if and only if s is a palindrome.

	>>> is_palindrome_v3('noon')
	True
	>>> is_palindrome_v3('racecar')
	True
	>>> is_palindrome_v3('dented')
	False
	"""
	count = 0
	j = len(s) - 1
	for i in range(len(s) // 2):
		if s[i] != s[j - i]:
			return False
			
	'''for i in range(len(s) // 2):
		if s[i] != s[len(s) - i - 1]:
			return False'''

	return True
	
#print(is_palindrome_v3("noon"))

def is_anagram(s1, s2):
	""" (str, str) -> bool

	Return True if and only if s1 is an anagram of s2.

	>>> is_anagram("silent", "listen")
	True
	>>> is_anagram("bear", "breach")
	False
	"""
	'''L1 = list(s1)
	L2 = list(s2)
	
	L1.sort()
	L2.sort()
	
	if L1 == L2:
		return True

	return False'''
	
	'''D1 = {}
	D2 = {}
	
	for letter in s1:
		if letter in D1:
			D1[letter] = D1[letter] + 1
		else:
			D1[letter] =  1
	
	for letter in s2:
		if letter in D2:
			D2[letter] = D2[letter] + 1
		else:
			D2[letter] =  1
			
	
	if D1 == D2:
		return True
		
	return False'''

#print(is_anagram("silent", "listen"))

def count_startswith(L, ch):
	""" (list of str, str) -> int

	Precondition: the length of each item in L is >= 1, and len(ch) == 1

	Return the number of strings in L that begin with ch.

	>>> count_startswith(['rumba', 'salsa', 'samba'], 's')
	2
	"""
	startswith = L[:]

	'''for item in L:
		if not item.startswith(ch):
			startswith.remove(item)

	return len(startswith)'''
	
	'''for item in L:
		if item.startswith(ch):
			startswith.remove(item)

	return len(L) - len(startswith)'''
	
	count = 0

	for item in L:
		if item.startswith(ch):
		  count = count + 1

	return count
	
print(count_startswith(['rumba', 'salsa', 'samba','simba'], 's'))

def check_digit(s):
	digits = ''

	'''for ch in s:
		if ch in '0123456789':
			digits = digits + ch'''
			
	digits = ''

	'''for i in range(len(s)):
		if s[i].isdigit():
			digits = digits + s[i]'''
			
	indices = []

	for i in range(len(s)):
		if s[i].isdigit():
			indices.append(i)

	for index in indices:
		digits = digits + s[index]

	print(digits)
	
#check_digit("abc123")

def is_one_to_one(d):
	""" (dict) -> bool

	Return True if and only if no two of d's keys map to the same value.

	>>> is_one_to_one({'a': 1, 'b': 2, 'c': 3})
	True
	>>> is_one_to_one({'a': 1, 'b': 2, 'c': 1})
	False
	>>> is_one_to_one({})
	True
	"""
	l = []
	l2 = []
	
	'''for k in d:
		l.append(d[k])

	for i in range(0,len(l)):
		for j in range(i + 1,len(l)):
			if l[i] == l[j]:
				return False'''

	

	
	
	return True
	
#print(is_one_to_one({'a': 1, 'b': 1, 'c': 3}))