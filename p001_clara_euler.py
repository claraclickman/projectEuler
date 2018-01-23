#!/usr/bin/env python
# -*- coding: utf-8 -*-
# CLARA CLICKMAN
# SRC: Jesse Rubin + project euler

prob_prompt = """
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

link: https://projecteuler.net/problem=1
"""


# def sum_multiples_below(below_n, multiples_list):
#     """
#     >>> sum_multiples_below(10, [3, 5])
#     23
#     """
#     # CLARA IMPLEMENT THIS FUNCTION
#     pass

#     mults_list = []
#     for i in range(below_n):


# write tests below

'''
this is the working model for adding fixed multiple 3 and 5
'''


def multiples_below(n):

    sum_shit = 0
    # print(sum_shit)
    # sum_shit = sum_shit + 1
    # print(sum_shit)
    # sum_shit += 1
    # print(sum_shit)
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum_shit += i

    return sum_shit


print(multiples_below(1000))


# def sum_multiples_below(below_n, multiples_list):
