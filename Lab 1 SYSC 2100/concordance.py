"""
SYSC 2100 Winter 2024
Lab 1, Part 3, Exercise 4, Extra-Practice Exercise 5
"""

__author__ = 'James Gohl'
__student_number__ = '101299043'

import string

# For information about the string module, type help(string) at the shell
# prompt, or browse "The Python Standard Library", Section "Built-in Types",
# Subsection "Text Sequence Type - str" in the documentation
# (available @ python.org).


def build_concordance(filename: str) -> dict[str, list[int]]:
    """Return a concordance of words in the text file
    with the specified filename.

    The concordance is stored in a dictionary. The keys are the words in the
    text file. The value associated with each key is a list containing the line
    numbers of all the lines in the file in which the word occurs.)

    >>> concordance = build_concordance('sons_of_martha.txt')
    """
    infile = open(filename, "r")
    hist = {}

    line_num = 0
    for line in infile:
        line_num += 1
        word_list = line.split()
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            if word != '' and word not in hist:
                hist[word] = [line_num]
            elif word != '' and line_num not in hist[word]:
                hist[word].append(line_num)
    return hist


# Extra-Practice: Exercise 5 Solution


if __name__ == '__main__':
    file_name = input("enter file name: ")
    concordance = build_concordance(file_name)
    concordance = dict(sorted(concordance.items()))
    for key, value in concordance.items():
        print(key, ":", value)
