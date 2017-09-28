import string
adict = {}
sletters = string.letters[:26]
sletters = sletters.upper()
for s in sletters:
	s_index = sletters.index(s)
	v_index = s_index + 13
	if v_index <= 25:
		adict[s] = sletters[v_index]
	else:
		v_index = v_index - 26
		adict[s] = sletters[v_index]

def rot13_translate(astring):
	nstring = ''
	for a in astring:
		a = a.upper()
		if a in adict:
			for keys, vals in adict.iteritems():
				if vals == a:
					getKeys = keys
					nstring += getKeys
		else:
			nstring += a
	return nstring
print rot13_translate('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')
		


