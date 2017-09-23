"""A board is a list of list of str. For example, the board
ANTT
XSOB
is represented as the list
[['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
ANT
BOX
SOB
TO
is represented as the list
['ANT', 'BOX', 'SOB', 'TO']
"""

def is_valid_word(wordlist, word):
	""" (list of str, str) -> bool

	Return True if and only if word is an element of wordlist.

	>>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
	True
	>>> is_valid_word(['WORD', 'SUCK', 'MY ', 'DICK'], 'LOL')
	false
	"""
	if word in wordlist:
		return True
		
	return False


def make_str_from_row(board, row_index):
	""" (list of list of str, int) -> str

	Return the characters from the row of the board with index row_index
	as a single string.

	>>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
	'ANTT'
	>>> make_str_from_row([['B', 'E', 'A', 'K'], ['S', 'O', 'B', 'S']], 1)
	'SOBS'
	"""
	word = "".join(board[row_index])
	
	return word
	

def make_str_from_column(board, column_index):
	""" (list of list of str, int) -> str

	Return the characters from the column of the board with index column_index
	as a single string.

	>>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
	'NS'
	>>> make_str_from_column([['T', 'N', 'A', 'X'], ['Y', 'A', 'V', 'E']], 1)
	'NO'
	"""
	word = ""
	
	for i in range(len(board)):
		word = word + board[i][column_index]
			
	return word
	

def board_contains_word_in_row(board, word):
	""" (list of list of str, str) -> bool

	Return True if and only if one or more of the rows of the board contains
	word.

	Precondition: board has at least one row and one column, and word is a
	valid word.

	>>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
	True
	>>> board_contains_word_in_row([['P', 'U', 'S', 'S'], ['T', 'E', 'S', 'T']], 'PUSS')
	True
	"""

	for row_index in range(len(board)):
		if word in make_str_from_row(board, row_index):
			return True

	return False
				
				
def board_contains_word_in_column(board, word):
	""" (list of list of str, str) -> bool

	Return True if and only if one or more of the columns of the board
	contains word.

	Precondition: board has at least one row and one column, and word is a
	valid word.

	>>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
	False
	>>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'O', 'O', 'B'],['O',"O","O","O"],['O',"B","O","O"]], 'NO')
	True
	"""
	for column_index in range(len(board[0])):
		if word in make_str_from_column(board, column_index):
			return True
			
	return False
	

def board_contains_word(board, word):
	""" (list of list of str, str) -> bool

	Return True if and only if word appears in board.

	Precondition: board has at least one row and one column.

	>>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
	True
	board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANTS')
	FALSE
	"""

	if board_contains_word_in_row(board,word) or board_contains_word_in_column(board, word):
			return True
			
	return False
	
	
def word_score(word):
	""" (str) -> int

	Return the point value the word earns.

	Word length: < 3: 0 points
				 3-6: 1 point per character for all characters in word
				 7-9: 2 points per character for all characters in word
				 10+: 3 points per character for all characters in word

	>>> word_score('DRUDGERY')
	16
	>>> word_score('WORD')
	4
	"""
	length = len(word)
	
	if length < 3:
		return 0
	elif length >= 3 and length <= 6:
		return length * 1
	elif length >= 7 and length <= 9:
		return length * 2
	elif length >= 10:
		return length * 3
			
			
def update_score(player_info, word):
	""" ([str, int] list, str) -> NoneType

	player_info is a list with the player's name and score. Update player_info
	by adding the point value word earns to the player's score.

	>>> update_score(['Jonathan', 4], 'ANT')
	
	>>> update_score(['Jonathan', 4], 'TAPE')
	
	"""
	
	player_info[1] = player_info[1] +  word_score(word)
	
	
def num_words_on_board(board, words):
	""" (list of list of str, list of str) -> int

	Return how many words appear on board.

	>>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
	3
	num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
	"""
	matches = 0
	
	for word in words:
		if board_contains_word(board, word):
				matches = matches + 1

	return matches
	

def read_words(words_file):
	""" (file open for reading) -> list of str

	Return a list of all words (with newlines removed) from open file
	words_file.

	Precondition: Each line of the file contains a word in uppercase characters
	from the standard English alphabet.
	"""
	words = []
	
	for word in words_file:
		words.append(word.strip('\n'))
		
	return words


def read_board(board_file):
	""" (file open for reading) -> list of list of str

	Return a board read from open file board_file. The board file will contain
	one row of the board per line. Newlines are not included in the board.
	"""
	board = []
	
	for line in board_file:
		board.append(list(line.strip()))
		
	return board

	