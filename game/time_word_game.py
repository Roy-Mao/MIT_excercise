
import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
points_dict = {}

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist


def get_words_to_points(word_list):
    for word in word_list:
        totVal = 0
        for letter in word:
            letterVal = SCRABBLE_LETTER_VALUES[letter]
            totVal += letterVal
        points_dict[word] = totVal


def count_letter(word,letter):#count how many letters appear in the word
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return count


def pick_best_word(hand, points_dict):
    """
    Return the highest scoring word from points_dict that can be made 
    with the given hand.Return '.' if no words can be made with the 
    given hand. 
    """
    max_points = 0
    test_list = []
    final_list = []
    my_list = points_dict.keys()[:]
    another_list = points_dict.keys()[:]
    for i in my_list:     #get the key-word item in the dict
        for letter in i:           #iterate through the letters in the word
            if not letter in hand.keys():
                another_list.remove(i)
                break     #I will get a new dic must contain keys in hand
    if len(another_list) == 0:
        return '.'
    for j in hand.keys():          # loop the key-word in hand dict
        for i in another_list:       # loop the word-key item in scruded new dict
            count = count_letter(i, j)
            if count > hand[j]:
                if not i in test_list:
                    test_list.append(i)
                else:
                    continue
    for m in another_list:
        if not m in test_list:
            final_list.append(m)
    if len(final_list) == 0:
        return '.'
    for n in final_list:
        points = points_dict.get(n)
        if points >= max_points:
            max_points = points
            print n
    return max_points






def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
    sumScore = 0
    word.lower()
    wordLength = len(word)
    for letter in word:
        singleScore = SCRABBLE_LETTER_VALUES[letter]
        sumScore += singleScore
    if wordLength == n:
        sumScore += 50
    return sumScore

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    word.lower()
    new_hand = {}
    for element in hand.keys():
        for letter in word:
            if element == letter:
                val = hand[element] - 1
                hand[element] = val
                if hand[element] > 0:
                    continue
                else:
                    break
            else:
                continue
        if hand[element] > 0:
            new_hand[element] = hand[element]
        else:
            continue
    return new_hand
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, points_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    word.lower()
    word_to_dic = get_frequency_dict(word)
    for letter in word_to_dic.keys():
        if not letter in hand.keys():
            return False
    for letter in word_to_dic.keys():
        if word_to_dic[letter] > hand[letter]:
            return False
    if word in points_dict.keys():
        return True
    else:
        return False




#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    condition = True
    done = False
    tot = 0.0
    remain_time = 15.00
    while condition:
        print 'Current Hand: ', display_hand(hand)
        start_time = time.time() #once appear above sentence, start counting
        user_input = raw_input('Enter word, or a "." to indicate that you are finished: ')
        if user_input == ".":
            break
        is_valid = is_valid_word(user_input, hand, word_list)
        while not is_valid: 
            user_input = raw_input('Invalid input, choose another word or ".": ')
            if user_input == '.':
                done = True
                break
            else:
                is_valid = is_valid_word(user_input, hand, word_list)
        if done:
            break
        end_time = time.time()
        if end_time - start_time <= 1:
            total_time = 1.00
        else:
            total_time = end_time - start_time
        score = get_word_score(user_input, HAND_SIZE)
        tscore = float(score) / total_time
        tscore = round(tscore, 2)
        prior_tot = tot
        tot += tscore
        tot = round(tot, 2)
        hand = update_hand(hand, user_input)
        remain_time -= total_time
        if remain_time > 0:
            print 'It took %0.2f seconds to provide an answer.' % total_time
            print 'You have %0.2f seconds remaining.' % remain_time
            print user_input + ' earned ' + str(tscore) + ' points. Total: ' + str(tot) + ' points.' 
        else:
            print 'It took %0.2f seconds to provide an answer.' % total_time
            one_result = 'Total time exceeds 15 seconds. Your final score: %s' % prior_tot  
            condition = False
    two_result = 'Your final score: ' + str(tot) + ' points.'  # replace this with your code...
    if remain_time >= 0:
        print two_result
    else:
        print one_result
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
    
    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    get_words_to_points(word_list)
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

