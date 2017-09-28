from string import *
#iteration approach
def countSubStringMatch(target,key):
	Lst = []
	i = 0
	while i <= len(target):
		retVal = find(target, key, i)
		if retVal < 0:
			return len(Lst)
		Lst.append(retVal)
		i = retVal + 1

recursive approach
def countSubStringMatchRecursive(target, key):
	retVal = find(target, key)
	if retVal < 0:
		return 0
	else:
		return 1 + countSubStringMatchRecursive(target[retVal + len(key):], key)

#the iteration approach
def subStringMatchExact(target,key):
	Lst = []
	i = 0
	while i <= len(target):
		retVal = find(target, key, i)
		if retVal < 0:
			break
		Lst.append(retVal)
		i = retVal + 1
	return tuple(Lst)

def constrainedMatchPair(firstMatch,secondMatch,length):
	Lst = []
	for i in firstMatch:
		for j in secondMatch:
			if i + length + 1 == j:
				Lst.append(i)
	return tuple(Lst)

def subStringMatchExactlyOneSub(target,key):
	firstResult = subStringMatchExact(target, key)
	firstMatch = subStringMatchExact(target, "")
	secondMatch = subStringMatchExact(target, "tgc")
	secondResult = constrainedMatchPair(firstMatch, secondMatch, 0)
	for i in secondResult:
		if not i in firstResult:
			return i


print subStringMatchExactlyOneSub("ttgcatgcatggatgtaatgcag", "atgc")








