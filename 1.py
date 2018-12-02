#!/usr/bin/env python3
#
# https://adventofcode.com/2018

print ("What's the frequency, Kenneth?")

# Read frequency changes from file into a changelist
changelist = []
with open('frequency-changes.txt') as file_:
    for line in file_:
        changelist.append(int(line))

# Loop through changelist over and over, until reaching a previously seen frequency
current = 0
seen = {}
found = False
while not found:
    for change in changelist:
        current += change
        if current in seen.keys():
            found = True
            break
        else:
            seen[current] = True

# We have a winner!
print("It's", current)
