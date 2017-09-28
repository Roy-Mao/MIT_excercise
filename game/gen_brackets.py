import random
def gen_brackets(num):
	amounts = num * 2
	bra_list = ['[', ']']
	nstring = ''
	for n in range(amounts):
		rchoice = random.choice(bra_list)
		nstring += rchoice
	return nstring

def check_nest(num):
	count = 0
	astring = gen_brackets(num)
	print astring
	for a in astring:
		if a == '[':
			count += 1
		else:
			count -= 1
		if count < 0:
			return 'Not OK'
	if count != 0:
		return 'Not OK'
	return 'OK'
print check_nest(5)

