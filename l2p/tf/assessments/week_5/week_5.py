def mystery(s):
	i = 0
	result = ''

	while not s[i].isdigit():
		  result = result + s[i]
		  i = i + 1

	return result
	
def secret(s):
    i = 0
    result = ''

    while s[i].isdigit():
        result = result + s[i]
        i = i + 1
   
    return result
	
#print("A" + secret('123')) error
#print("B" + secret('abc123'))
#print("C" + secret('123abc'))
#print("D" + secret('abc'))
	

def compress_list(L):
	""" (list of str) -> list of str

	Return a new list with adjacent pairs of string elements       from Lconcatenated together, starting with indices 0 and 1,    2 and 3,and so on.

	Precondition: len(L) >= 2 and len(L) % 2 == 0

	>>> compress_list(['a', 'b', 'c', 'd'])
	['ab', 'cd']
	""" 
	compressed_list = []
	i = 0

	while i < len(L):
		compressed_list.append(L[i] + L[i + 1])
		i = i + 2

	return compressed_list
	 

def sumit():
	totalwhile = 0
	i = 524
	
	while i <= 10508:
		if i % 2 == 0:
			totalwhile = totalwhile + i
		
		i = i + 1
		
	totalfor = 0
	
	for i in range(524, 10509, 2):
		totalfor = totalfor + i
		
	print("While: " + str(totalwhile) + " For: " + str(totalfor))
	
#sumit()


def cap_song_repetition(playlist, song):
	'''(list of str, str) -> NoneType

	Make sure there are no more than 3 occurrences of song in playlist.

	'''
	
	while playlist.count(song) > 3:
		playlist.remove(song)
		
		
def q10():
	a = [1, 2, 3]
	b = [1, 2, 3]
	a = [1, 'A', 3]
	b = [1, 'A', 3]
	print(a, b)
	#[1, 'A', 3] [1, 'A', 3]
	
def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1


#values = [1, 2, 3]
#print(increment_items(values, 2))
#print(values)		
		
def while_version(L):
	""" (list of number) -> number
	"""
	i = 0
	total = 0

	while i < len(L) and L[i] % 2 != 0:
		total = total + L[i]
		i = i + 1

	return total
	 
	 
def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total
	
	
	