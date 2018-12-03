#!/usr/bin/env python3
#
# https://adventofcode.com/2018

import string

# Read ids from file into list
def get_ids(filename):
    with open(filename) as f:
        ids = f.readlines()
    return ids

# Count how many letters that occur exactly "count" times in the id.
def count_letters_in_id(id, count):
    alphabet = string.ascii_lowercase
    occurences = 0
    for letter in alphabet:
        if id.count(letter) == count:
            occurences += 1
    if occurences == 1:
        print("\tMATCH: letter:", letter, ": count:", count, "occurences:", occurences)
        return 1
    else:
        print("\tNope: letter:", letter, ": count:", count, "occurences:", occurences)
        return 0

ids = get_ids("input.txt")
two = 0
three = 0
for id in ids:
    print("id:", id)
    two += count_letters_in_id(id, 2)
    three += count_letters_in_id(id, 3)
print("two:", two)
print("three:", three)
print(two * three)
