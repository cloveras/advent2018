#!/usr/bin/env python3
#
# https://adventofcode.com/2018

# Read frequency changes from file into a changelist, as integers
def get_changelist():
    with open('frequency-changes.txt') as f:
        changelist = list(map(int, f.readlines()))
    return changelist

# Loop through changelist over and over, until reaching a previously seen frequency
def find_seen_frequency(changelist):
    current = 0
    seen = {}
    found = False
    while not found:
        for change in changelist:
            current += change
            if current in seen:
                found = True
                break
            else:
                seen[current] = True
    return current

# Run the 💎💎
print ("What's the frequency, Kenneth?")
print("It's", find_seen_frequency(get_changelist()))
