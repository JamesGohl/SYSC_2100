# SYSC 2100 Winter 2023 Lab 11/Asst 2

# Put import statements here.

__author__ = 'Mutakabbir'
__student_number__ = '10101010'


from random import randint, choice

LIST_LENGTH = 9999


def generate_reverse_sorted_list(len_: int = LIST_LENGTH) -> list:
    """
    :param len_ (int) the size of the list to generate:
    :return (list) unsorted list:
    """
    list_ = list(range(len_, 0, -1))
    return list_


def generate_random_list(len_: int = LIST_LENGTH) -> list:
    """
    :param len_ (int) the size of the list to generate:
    :return (list) unsorted list:
    """
    list_ = [randint(1, len_ * 10) for _ in range(len_)]
    return list_


def generate_few_unique_list(len_: int = LIST_LENGTH, options_: list = [1, 2, 3, 4, 5]) -> list:
    """
    :param len_ (int) the size of the list to generate:
    :param options_ (list) The elements that can be present in the list:
    :return (list) unsorted list:
    """
    list_ = [choice(options_) for _ in range(len_)]
    return list_


def generate_nearly_sorted_list(len_: int = LIST_LENGTH) -> list:
    """
    :param len_ (int) the size of the list to generate:
    :return (list) unsorted list:
    """
    list_ = list(range(len_))
    temp = list_[0]
    list_[0] = list_[1]
    list_[1] = temp
    return list_
