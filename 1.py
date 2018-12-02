#!/usr/bin/env python3
#
# https://adventofcode.com/2018

print ("What's the frequency, Kenneth?")

# Read frequency changes from file into a changelist, as integers
changelist = []
with open('frequency-changes.txt') as f:
    changelist = list(map(int, f.readlines()))

# Loop through changelist over and over, until reaching a previously seen frequency
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

# We have a winner!
print("It's", current)
