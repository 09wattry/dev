def get_negative_nonnegative_lists(L):
	'''(list of list of int) -> tuple of (list of int, list of int)

	Return a tuple where the first item is a list of the negative ints in the
	inner lists of L and the second item is a list of the non-negative ints
	in those inner lists.

	Precondition: the number of rows in L is the same as the number of
	columns.

	>>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
	([-1, -4], [3, 5, 2, 5, 4, 0, 8])
	'''
	
	nonneg = []
	neg = []
	for row in range(len(L)):
		for col in range(len(L)):
			if L[row][col] < 0:
					neg.append(L[row][col])

			nonneg.append(L[row][col])


	return (neg, nonneg)
	
def count_chars(s):
	'''(str) -> dict of {str: int}

	Return a dictionary where the keys are the characters in s and the values
	are how many times those characters appear in s.

	>>> count_chars('abracadabra')
	{'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
	'''
	d = {}

	for c in s:
		if not (c in d):
			d[c] =  1
		else:
			d[c] = d[c] + 1

	return d
	

def get_keys(L, d):
	'''(list, dict) -> list

	Return a new list containing all the items in L that are keys in d.

	>>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
	['a', 1]
	'''

	result = []
	for k in d:
		if k in L:
			result.append(k)

	return result


def are_lengths_of_strs(L1, L2):
	'''(list of int, list of str) -> bool

	Return True if and only if all the ints in L1 are the lengths of the strings
	in L2 at the corresponding positions.

	Precondition: len(L1) == len(L2)

	>>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
	True
	'''

	result = True
	for i in range(len(L1)):
		if L1[i] != len(L2[i]):
			result = False

	return result
	
	

def get_diagonal_and_non_diagonal(L):
	'''(list of list of int) -> tuple of (list of int, list of int)

	Return a tuple where the first item is a list of the values on the
	diagonal of square nested list L and the second item is a list of the rest
	of the values in L.

	>>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
	([1, 4, 8], [3, 5, 2, 5, 4, 0])
	'''

	diagonal = []
	non_diagonal = []
	for row in range(len(L)):
		for col in range(len(L)):
			if row == col:
				diagonal.append(L[row][col])
			elif row != col:
				non_diagonal.append(L[row][col])

	return (diagonal, non_diagonal)
	
	
	
def reverse(s):
	result = ''
	i = len(s) - 1
	while i >= 0:
		result = result + s[i]
		i = i - 1

	return result
	
def double_last_value(L):
	'''(list of int) -> NoneType

	Double the value at L[-1]. For example, if L[-1] is 3,
	replace it with 6.

	Precondition: len(L) >= 1.
	'''
	return L[-1] * 2
	

def count_values_that_are_keys(d):
	'''(dict) -> int

	Return the number of values in d that are also keys in d.

	>>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
	3
	>>> count_values_that_are_keys({1: 1})
	1
	>>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
	2
	>>> count_values_that_are_keys({1: 2})
	0
	'''

	result = 0
	for k in d:
		if d[k] in d:
			 result = result + 1

	return result
	
print(count_values_that_are_keys({1: 2, 2: 3, 3: 3}))