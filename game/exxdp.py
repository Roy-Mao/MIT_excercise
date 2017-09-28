import random
fair = [1,2,3,4,5,6]
def roll_dices(dice):
	diNum1 = random.choice(dice)
	diNum2 = random.choice(dice)
	return diNum1, diNum2
def craps_game(dice):
	diNum1, diNum2 = roll_dices(dice)
	sumNum = diNum1 + diNum2
	if sumNum in [7, 11]:
		return True
	if sumNum in [2, 3, 12]:
		return False
	point = sumNum
	while True:
		diNum1, diNum2 = roll_dices(dice)
		sumNum = diNum1 + diNum2
		if sumNum == 7:
			return False
		if sumNum == point:
			return True

def craps_trial(trialNum, dice):
	count_win = 0
	count_lose = 0
	for t in range(trialNum):
		if craps_game(dice):
			count_win += 1
		else:
			count_lose += 1
	winner_ratio = float(count_win)/trialNum
	casino_ratio = 1 - winner_ratio
	print count_win, count_lose, casino_ratio

craps_trial(100000, fair)



