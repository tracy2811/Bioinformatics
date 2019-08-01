#! /usr/bin/python3

# Input: Pattern, Genome (separated by newline character)
# Output: List of matching position

def PatternMatching(Pattern, Genome):
    pos = []
    n = len(Genome)
    k = len(Pattern)

    for i in range(n-k+1):
        if Genome[i:i+k] == Pattern:
            pos.append(i)

    return pos

import sys

input = sys.stdin.read().splitlines()
v_cholerae = input[1]
pattern = input[0]

print(PatternMatching(pattern, v_cholerae))
