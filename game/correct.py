import string
def correct(astring):
	Length = len(astring)
	nstring = ''
	this_index = 0
	while this_index <= Length - 1:
		if astring[this_index] == ' ':
			nstring += astring[this_index]
			next_index = this_index + 1
			next_item = astring[next_index]
			while next_item == ' ':
				next_index += 1
				next_item = astring[next_index]
			nstring += next_item
			this_index = next_index + 1
		if astring[this_index] in string.punctuation:
			nstring += astring[this_index]
			next_index = this_index + 1
			if next_index <= Length - 1:
				next_item = astring[next_index]
				if next_item != ' ':
					nstring += ' '
			this_index += 1
		else:
			nstring += astring[this_index]
			this_index += 1
	return nstring
print correct('This   is  very funny  and     cool.   Indeed!')






