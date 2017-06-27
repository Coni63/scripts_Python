import sys
import math

def decomposer(mot):
    dictionnaire = {}
    for each_letter in mot:
        if each_letter not in dictionnaire.keys():
            dictionnaire[each_letter]=1
        else:
            dictionnaire[each_letter]+=1
    return dictionnaire

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
score = {"a":1, "b":3, "c":3, "d":2, "e":1, "f":4, "g":2, "h":4, "i":1, "j":8, "k":5, "l":1, "m":3, "n":1, "o":1, "p":3, "q":10, "r":1, "s":1, "t":1, "u":1, "v":4, "w":4, "x":8, "y":4, "z":10}
freq_word = {}
dico = []
possible_word = []
best_score = 0

n = int(input())
for i in range(n):
    w = input()
    dico.append(w)
    
letters = input()
freq_word[letters] = decomposer(letters)
        
for each_word in dico: #pour chaque mot du dico
    flag = True
    freq_word[each_word] = decomposer(each_word) #on le decompose en dico de caractere
    for each in freq_word[each_word]: #pour chaque letter du mot du dico
        if each not in freq_word[letters].keys() or freq_word[each_word][each] > freq_word[letters][each]:  #si on a pas assez de fois cette lettre ou qu'on ne l'a pas du tout
            flag = False
            
    if flag == True:
        possible_word.append(each_word)

print(dico, file=sys.stderr)     
print(possible_word, file=sys.stderr)

for each in possible_word:
    val = 0
    for letter in each:
        val += score[letter]
    print(val, file=sys.stderr)
    if val > best_score:
        best_score = val
        mot = each
        
print(mot)    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


