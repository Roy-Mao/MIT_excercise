
import re
def alternade_game(file):
	with open(file, 'r') as f:
		file_str = f.read()
	file_str = re.sub('\s+', ' ', file_str)
	file_list = file_str.split()
	for f in file_list:
		odd_index_char = f[::2]
		even_index_char = f[1::2]
		if all(x in f for x in [odd_index_char, even_index_char]):
			print '"' + f  + '": makes "' + odd_index_char + '" and "' + even_index_char + '".'


	
