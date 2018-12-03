#!/usr/bin/env python3
#
# https://adventofcode.com/2018

# Read ids from file into list
def get_ids(filename):
    with open(filename) as f:
        ids = f.readlines()
    return ids

# Check if id has at least one letter that occurs exactly "count" times
def check_letters_in_id(id, count):
    for letter in list("abcdefghijklmnopqrstuvxyz"):
        if id.count(letter) == count:
            return 1
    return 0

# Business time
ids = get_ids("input.txt")
two = 0
three = 0
for id in ids:
    two += check_letters_in_id(id, 2)
    three += check_letters_in_id(id, 3)

print("two:", two)
print("three:", three)
print("checksum:", two * three)
