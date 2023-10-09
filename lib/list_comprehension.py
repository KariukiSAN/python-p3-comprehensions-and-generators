#!/usr/bin/env python3

def return_evens(num_list):
    # Use list comprehension to filter even numbers from num_list
    evens = [num for num in num_list if num % 2 == 0]
    return evens

def make_exclamation(sentence_list):
    # Use list comprehension to add exclamation marks to sentences
    exclamation_sentences = [sentence + '!' for sentence in sentence_list]
    return exclamation_sentences
