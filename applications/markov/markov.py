import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

# Looks through entire list and returns the string
# with all punctuation removed


def remove_punctuation(_str):
    # temp string variable to return once un-punctuated
    _ = ""

    # string list of all punctuations
    p_list = '''"\n:;,.-+=/\\|[]!{}()*^?&'''
    # looking at each character..
    for char in _str:
        # if the current char we ar looking at is NOT in the p_list..
        if char not in p_list:
            # then its okay to move on to the next step
            _ += char
    
    # return  non punctuated string
    return _


def random_sentence(length, choices):
    # removes punctuation..
    choices = remove_punctuation(choices)

    # split the words from string to list
    _all_words = choices.lower().split(" ")

    _table = {}

    # create a lookup table to store all of the 
    # word choices we get
    # word  | next_choices
    # a piece of pizza, a hamburger, and a salad 
    # --------------------
    # a             | [piece, hamburger, salad]
    # piece         | [of ]
    # of            | [pizza, a]
    # pizza         | [a ]
    # hamburger     | [and ]
    # and           | [a ]
    # salad         | None
    for _choice in range(0, len(_all_words)-1):
        current_word = _all_words[_choice]  # current word

        # if the next character is at the end of the list...
        if _choice + 1 >= len(_all_words):
            _table[current_word].append(None)
        else:
            next_word = _all_words[_choice + 1]
            # if current_word not in _table:]
            if current_word not in _table:
                _table[current_word] = []
                _table[current_word].append(next_word)

            else: 
                _table[current_word].append(next_word)
            

    ## so with this in mind... on the left we have an index of choices... 
    ## and for each of those choices there are x other words to choose from to create a sentence

    __final = ""


    # choose somewhere to start...
    random_choice = random.randint(1, len(_table))
    start = _table[_all_words[random_choice]]
    # look through the entire list..
    for i in range(length):
        cur = start 
        for k, v in cur.items():
            _choice  = random.choice(v)
            

    # return the new words in string form
    return __final

# TODO: construct 5 random sentences
# Your code here



# print(random_sentence(10, words))
print(random_sentence(5, words))
# print(random_sentence(7, words))
# print(random_sentence(8, words))
# print(random_sentence(16, words))
