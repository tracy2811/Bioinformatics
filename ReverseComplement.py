#! /usr/bin/python3

# Input: A DNA string Pattern
# Output: The reverse complement of Pattern

def ReverseComplement(Pattern):
    return Complement(Pattern[::-1])

def Complement(Pattern):
    comp = ''
    for a in Pattern:
        if a == 'A':
            comp = comp + 'T'
        elif a == 'T':
            comp = comp + 'A'
        elif a == 'C':
            comp = comp + 'G'
        elif a == 'G':
            comp = comp + 'C'
        else:
            raise ValueError('Invalid character %c' %(a))
    return comp

Pattern = input()
print(ReverseComplement(Pattern))
