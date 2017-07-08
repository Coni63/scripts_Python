import re

retour = "*#18*51*511#3#6##"
retour += "*#18*51*511#3#6*1*115##"
retour += "*#18*51*511#3#6*2*108##"
retour += "*#18*51*511#3#6*3*110##"
retour += "*#18*51*511#3#6*4*112##*#18*51*511#3#6*5*110##"
retour += "*#18*51*511#3#6*6*105##"
retour += "*#18*51*511#3#6*7*140##"
retour += "*#18*51*511#3#6*8*220##"
retour += "*#18*51*511#3#6*9*340##*#18*51*511#3#6*10*342##"
retour += "*#18*51*511#3#6*11*648##*#18*51*511#3#6*12*103##*#18*51*511#3#6*13*103##*#18*51*511#3#6*14*103##"
retour += "*#18*51*511#3#6*15*100##*#18*51*511#3#6*16*101##*#18*51*511#3#6*17*101##*#18*51*511#3#6*18*103##*#18*51*511#3#6*19*104##*#18*51*511#3#6*20*104##"
retour += "*#18*51*511#3#6*21*199##*#18*51*511#3#6*22*511##*#18*51*511#3#6*23*107##*#18*51*511#3#6*24*107##*#18*51*511#3#6*25*4196##*#*1##"

part1 = []
part2 = []
part3 = []

pattern = "(\*\#\d+\*\d+\*\d+#\d\#\d+\*\d+\*\d+\#{2})"
# for result in re.findall(pattern, retour):
#     parts = result[2:-2].split("#")
#     part1.append([int(x) for x in parts[0].split("*")])
#     part2.append(int(parts[1]))
#     part3.append([int(x) for x in parts[2].split("*")])
#
# print(part1)
# print(part2)
# print(part3)
#
# print(list(zip(*part3)))
data = {}
for result in re.findall(pattern, retour):
    result = result[2:-2].split("#")[2].split("*")
    heure = int(result[1])
    conso = int(result[2])
    data[heure] = conso

del(data[25])
print(data)