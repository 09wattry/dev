
file_path =  "read.txt"

file = open(file_path, 'r')
line =  file.readline()

'''while line != '':
	print(line, end='\n')
	line = file.readline()
'''

for line in file:
	print(line - '\n')
	
file.close()
	