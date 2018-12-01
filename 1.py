#!/usr/bin/env python3

i = 0
with open('frequency-changes.txt') as file_:
    for line in file_:
        i += int(line)
print(i)
