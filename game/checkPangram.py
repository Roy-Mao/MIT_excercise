import string
# astring = 'my nam&%$#$e is roy'
# astring = astring.replace(' ', '')
# astring = ''.join(x for x in astring if x not in string.punctuation)
# print astring


def checkPangram(astring):
	adict = {}
	astring = astring.lower()
	astring = astring.replace(' ', '')
	astring = ''.join(x for x in astring if x not in string.punctuation)
	for a in astring:
		getVal = adict.get(a, 0)
		if getVal == 0:
			adict[a] = 1
		else:
			adict[a] = getVal + 1
	print adict
	print adict.keys()
	keyNum = len(adict.keys())
	if keyNum == 26:
		return True
	else:
		return False
print checkPangram('The quick brown fox jumps over the lazy dog.')


