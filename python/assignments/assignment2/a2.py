def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1) > len(dna2):
        return True
    else:
        return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC','G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False

		
def is_valid_sequence(dna):
	""" (str) -> bool
	Return True if and only if the DNA sequence is valid 
	(that is, it contains no characters other than 'A', 'T', 'C' and 'G')
	
	>>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCTEA')
    False
	"""
	
	for char in dna:	
		if ((char != 'A') and (char != 'T') and (char != 'C') and (char != 'G')):
			return False	
	return True
	

def insert_sequence(dna1, dna2, i):
	""" (str, str, int) -> str
	Returns a string dna sequence after dna2 has been concatenated with dna2 at index id.	
		
	>>> insert_sequence("CCGG", "AT", 2)
	CCATGG
	>>> insert_sequence("CCGGATAG", "GC", 5)
	CCGGAGCTAG
	"""
	
	return dna1[:i] + dna2 + dna1[(i):]
	
	
def get_complement(nucleotide):
	""" (str) -> str
	Returns the complement nucleotide of the input parameter nucleotide.
	
	>>> get_complement("A")
	T
	>>> get_complement("G")
	C
	"""

	if nucleotide == 'A':
		return 'T'
	elif nucleotide == 'T':
		return 'A'
	elif nucleotide == 'G':
		return 'C'
	elif nucleotide == 'C':
		return 'G'
	else:
		return "Invalid input"
	
	
if __name__ == '__main__':
	print(get_complement("A"))
	
