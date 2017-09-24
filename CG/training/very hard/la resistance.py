import sys
import math
import re
import time

def check_iter(sentence = "", pos = 0):
    for code, word in dico.items():
        if l[pos:pos + len(code)] == code:
            sentence += word
            #print(sentence, file=sys.stderr)
            if pos + len(code) == len(l):
                global a
                a += 1
                return True
            else:
                next_pos = pos + len(code)
                check_iter(sentence = sentence, pos = next_pos)


def str_to_morse(word):
    conv = ""
    for each in word:
        conv += morseAlphabet[each]
    return conv


morseAlphabet = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
         "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
         "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.."}

inverseMorseAlphabet=dict((v,k) for (k,v) in morseAlphabet.items())

dico = {}

l = input()
print(l, file=sys.stderr)

s = time.time()
a = 0
n = int(input())
for i in range(n):
    w = input()
    w = w.upper()
    morse_code = str_to_morse(w)
    dico[morse_code] = w

# list_words = [input().upper() for x in range(n)]
# print(list_words, file=sys.stderr)

#print(l[4:4+7])

print(time.time() - s, file=sys.stderr)

check_iter()

print(a)

# To debug: print("Debug messages...", file=sys.stderr)