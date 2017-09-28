import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

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

wordlist = load_words()

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

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.

# TO DO: your code begins here!
def end_game(word, wordlist):
    word = word.lower()
    wordLength = len(word)
    for i in wordlist:
        compare_slice = i[ : wordLength]
        if compare_slice == word:
            break
        else:
            if (i == wordlist[-1]) and (compare_slice != word):
                return True
            else:
                continue

    for item in wordlist:
        if (item == word) and (wordLength > 3):
            return True

    return False


def check_valid(enter_letter):
    Letterlength = len(enter_letter)
    if (enter_letter in string.ascii_letters) and (Letterlength == 1):
        return True
    else:
        return False

def ask_input():
    user_input = raw_input('Please give a letter: ').upper()
    is_valid = check_valid(user_input)
    while not is_valid:
        user_input = raw_input('Invalid character, try again.')
        is_valid = check_valid(user_input)
    user_input = user_input.upper()
    return user_input




def play_the_game():
    word = ''
    if_end = False
    while not if_end:
        wordLength = len(word)
        word = word.upper()
        if wordLength == 0:
            n = '1'
            print 'Welcome to Ghost.'
            print 'Player 1 goes first.'
            print 'Current word fragment: ' + word
            entered_letter = ask_input()
            print 'Player 1' + ' says letter: ' +  entered_letter
        else:
            if wordLength % 2 != 0:
                n = '2'
                m = '1'
            else:
                n = '1'
                m = '2'
            print 'Current word fragment: ' + word
            print 'Player ' + n + "'s turn."
            entered_letter = ask_input()
            print 'Player ' + n + ' says letter: ' +  entered_letter
        word = word + entered_letter
        if_end = end_game(word, wordlist)
    print 'Current word fragment: ' + word
    print 'Player ' + n + ' loses because "' + word + '" is a word!'
    print 'Player ' + m + ' wins!'
play_the_game()