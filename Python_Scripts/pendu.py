mot = input("Entrez un mot : \n")
arr_mot = list(mot.lower())
current_mot = ['*']*len(arr_mot)
proposition = []
error = 0
while(error < 7 and arr_mot != current_mot):
    lettre = input("Donnez une lettre : \n")
    lettre = lettre.lower()
    if lettre in arr_mot and lettre not in proposition:
        proposition.append(lettre)
        for index, char in enumerate(arr_mot):
            if char == lettre:
                current_mot[index] = lettre
    else:
        error += 1
    print(''.join(current_mot))
    print("{} errors(s), {} vie(s) restante(s)".format(error, 7-error))

if error < 7:
    print("Gagné !")
else:
    print('PERDU :(')