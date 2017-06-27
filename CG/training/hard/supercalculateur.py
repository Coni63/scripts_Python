import sys
import math

n = int(raw_input())

calc_arr = []
lastdate = 0
calcul = 0

for i in xrange(n):
    j, d = [int(j) for j in raw_input().split()]
    calc_arr.append([j, j+d])
    lastdate = max(lastdate, j+d)

# tri par date de debut puis duree
calc_arr.sort(key=lambda elem: elem[1])
print >> sys.stderr, calc_arr

# array representant chaque jour free [0]
list_date = [0] * lastdate 

for each in calc_arr:
    #si la duree n'est pas attribue, on attribut un le calcul le plus court
    if not 1 in list_date[each[0]:each[1]]:
        #on replis par des 1 le calendrier
        calcul += 1
        list_date[each[0]:each[1]] = [1] * (each[1]-each[0])
 
print(calcul)