"""
File: boggle.py
Name: Sharon
----------------------------------------
This program creates a boggle game that
recursively finds all the words from the 4*4 boggle board.
User will input letters into boggle board.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    input 4 rows of letters,
    and find all the words in boggle game
    """
    start = time.time()
    ####################
    dic_list = read_dictionary()
    letters = []
    counter = []        # count the numbers of words that have found
    for i in range(4):
        input_letter = input(f'{i+1} row of letters: ').lower().split()
        for ch in input_letter:
            if len(ch) != 1 or len(input_letter) != 4:
                print('Illegal input')
                return False
        letters.append(input_letter)
    find_word(letters, dic_list, counter)
    print(f'There are {len(counter)} words in total.')
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(letters, dic_list, counter):
    """
    :param letters: list, list of input letters
    :param dic_list: list, words in dictionary
    :param counter: list, count the numbers of words that have found
    """
    for i in range(4):
        for j in range(4):
            position = []
            word = ''
            word += letters[i][j]           # first letter in word
            position.append((i, j))
            find_word_helper(letters, dic_list, counter, word, position, (i, j), (i, j))


def find_word_helper(letters, dic_list, counter, word, position, last_position, current_position):
    """
    :param letters: list, list of input letters
    :param dic_list: list, words in dictionary
    :param counter: list, count the numbers of words that have found
    :param word: str, the word contains letters
    :param position: list
    :param last_position: position of last letter
    :param current_position: position of current letter
    """
    last_position = current_position
    if has_prefix(word, dic_list):
        # Base case
        if word in dic_list and len(word) >= 4:
            counter.append(1)                       # update numbers of words that have found
            print(f'Found "{str(word)}"')
            dic_list.remove(word)                   # remove the found word from dictionary
            find_word_helper(letters, dic_list, counter, word, position, last_position, current_position)
        else:
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    a = last_position[0] + i             # move up or down
                    b = last_position[1] + j             # move left or right
                    if 0 <= a < 4 and 0 <= b < 4:
                        if (a, b) not in position:      # choose the letter that is not used
                            position.append((a, b))
                            # choose
                            word += letters[a][b]
                            current_position = (a, b)
                            # explore
                            find_word_helper(letters, dic_list, counter, word, position, last_position, current_position)
                            # un-choose
                            position.pop()
                            word = word[:-1]


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    dic_list = []
    with open(FILE, 'r') as f:
        for line in f:
            dic_list += line.split()
    return dic_list


def has_prefix(sub_s, dic_list):
    """
    :param dic_list: list, dictionary
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for ch in dic_list:
        if ch.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
