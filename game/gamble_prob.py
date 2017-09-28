resDict = {1: (float(2)/11), 2: ((float(6)/11) * (float(1)/11))}
def gamble_prob(numBets):
	if numBets in resDict:
		return resDict[numBets]
	else:
		resDict[numBets] = gamble_prob(numBets - 1) * (float(9)/11)
	return resDict[numBets]
gamble_prob()
print resDict
print sum(resDict.values())


