"""
File: anagram.py
Name: Sharon
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# Global Variable
dic_list = []       # a list of words in dictionary

dictionary = [set()for i in range(26)]

# def main():
#     print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
#     while True:
#         start = time.time()
#         read_dictionary()
#         anagrams = input('Find anagrams for: ')
#         if anagrams == EXIT:
#             break
#         else:
#             s = []
#             for item in s:
#                 s.append(item)
#             find_anagrams(anagrams)
#             end = time.time()
#             print(end - start)
#
#
# def read_dictionary():
#     with open(FILE, 'r') as f:
#         for line in f:
#             # global dict_list
#             dictionary[ALPHABET.find(line[0])].add(line.lower().strip())
#
#
# def find_anagrams(s):
#     """
#     :param s: list, the word import by user
#     :return: str: the number of total anagrams and the word list
#     """
#     word_lst = []
#     helper(s, [], word_lst)
#     print(str(len(word_lst)) + " anagrams: " + str(word_lst))
#
#
# def helper(lst, word, word_lst):
#     """
#     :param lst: list, the word import by user
#     :param word: list, put the index of anagram
#     :param word_lst: list, put the anagrams that is found in dictionary
#     """
#     # Base case
#     if len(lst) == len(word):
#         word_str = ""
#         for order in word:
#             word_str += lst[int(order)]
#         # if has_prefix(word_str):
#             if len(word_str) == len(lst):
#                 if word_str in dictionary[ALPHABET.find(word_str[0])] and word_str not in word_lst:
#                     word_lst.append(word_str)
#                     print("Searching...")
#                     print("Found: " + word_str)
#     else:
#         for i in range(len(lst)):
#             if i not in word:
#                 # Choose
#                 word.append(i)
#                 # Explore
#                 # if has_prefix(word):
#                 helper(lst, word, word_lst)
#                 # Un-choose
#                 word.pop()


def main():
    """
    input a word, and find anagrams of the word
    """

    ####################
    print(f'Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    s = str(input(f'Find anagrams for: '))
    start = time.time()
    read_dictionary()
    if s == EXIT:
        pass
    else:
        while True:
            if s != EXIT:
                find_anagrams(s)
                end = time.time()
                print('----------------------------------')
                print(f'The speed of your anagram algorithm: {end - start} seconds.')
            else:
                break
            s = str(input(f'Find anagrams for: '))
            start = time.time()
    ####################


def read_dictionary():
    global dic_list
    with open(FILE, 'r') as f:
        for line in f:
            dic_list += line.split()
    return dic_list


def find_anagrams(s):
    """
    :param s: str, input word
    :return:
    """
    find = []
    s_list = list(s)
    for i in range(len(dic_list)):
        if s_list[0] in dic_list[i] and len(s) == len(dic_list[i]):
            find.append(dic_list[i])
    s_list.pop(0)       # remove the first letter in input word
    find_anagrams_helper(s, s_list, find, [])


def find_anagrams_helper(s, s_list, find, new_find):
    """
    :param s: str, input word
    :param s_list: list, remaining letter in the input word
    :param find: list, words that are found
    :param new_find: list
    """
    # if len(s_list) == 0:                            # when removed all letters in input word
    #     for i in range(len(find)):
    #         print('Searching...')
    #         print(f'Found:  {find[i]}')
    #     print(f'{len(find)} anagrams:  {find}')
    # else:
    #     for i in range(len(find)):
    #         if s_list[0] in find[i]:                # check if the letter in input word is also in each word
    #             if sorted(list(find[i])[0:]) == sorted(list(s)[0:]):
    #                 new_find.append(find[i])
    #     s_list.pop(0)                               # remove the first letter
    #     find = new_find
    #     new_find = []
    #     find_anagrams_helper(s, s_list, find, new_find)

    for i in range(len(find)):
        if s_list[0] in find[i]:  # check if the letter in input word is also in each word
            if sorted(list(find[i])[0:]) == sorted(list(s)[0:]):
                new_find.append(find[i])
    for i in new_find:
        for j in range(len(new_find)):
            print('Searching...')
            print(f'Found:  {new_find[j]}')
        print(f'{len(new_find)} anagrams:  {new_find}')
#
#
# def has_prefix(sub_s):
#     """
#     :param sub_s:
#     :return:
#     """
#     if sub_s not in dic_list:
#         return False
#     return True


if __name__ == '__main__':
    main()
