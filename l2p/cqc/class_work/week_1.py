''' This file script is used to better understand the methods for writing a palindrome
	there are serveral algorythms that we will test.
	
'''
def reverse(s):
	rev = ''
	i = 0
	for char in s:
		rev = char + rev
		i = i + 1
	
	print("n = " + str(i))
	return rev

def method1(s):
	''' (str) -> bool
	
	Reverses s and compares it to the original string.
	
	Return True if s is a palindrome or False if it is not.
	
	>>> method1('racecar')
	True
	>>> method1('tame')
	False
	'''
	if reverse(s) == s:
		return True
	
	return False
	
print(method1('racecar'))

def method2(s):
	''' (str) -> bool
	
	Reverse half of the string and compare it to the other half.
	
	Return True if s is a palindrome or False if it is not.
	
	>>> method1('racecar')
	True
	>>> method1('tame')
	False
	'''
	mid = len(s) // 2
	if s[:mid] == reverse(s[len(s) - mid:]):
		return True
	
	return False
	
print(method2('racecar'))

def method3(s):
	''' (str) -> bool
	
	Compare every second letter, if they all match then the word is a palindrome 
	
	Return True if s is a palindrome or False if it is not.
	
	>>> method1('racecar')
	True
	>>> method1('tame')
	False
	'''
	i = 0
	j = len(s) - 1
	
	while i < j and s[i] == s[j]:
		j = j - 1
		i = i + 1
		
	print("n = " + str(i))
	
	
	if s[i] == s[j] or j <= i:
		return True
		
		
	return False
		
print(method3('racecar'))