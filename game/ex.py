
freq = {}
def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    for x in sequence:
        freq[x] = 12
    return freq
get_frequency_dict(['a', 'b', 'c', 'd'])
print freq