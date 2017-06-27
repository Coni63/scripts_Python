import sys
import math
import numpy as np

O1 = []
Ologn = []
On = []
Onlogn = []
On2 = []
On2logn = []
On3 = []
O2n = []
list_y = []
list_y2 = []
group = [On,Ologn,Onlogn,On2,On2logn,On3, O2n]

n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    #if x > 0 :
    list_y.append(y)
    Ologn.append(math.log(x))
    On.append(x)
    Onlogn.append(x*math.log(x))
    On2.append(math.pow(x, 2))
    On2logn.append(math.pow(x, 2)*math.log(x))
    On3.append(math.pow(x, 3))
    if x <= 30:
        O2n.append(math.pow(2,x))
            
res = []
res2 = []

for each in group:
    
    if len(each) == len(list_y):
        A = np.vstack([each, np.ones(len(each))]).T
        #print(A , file=sys.stderr)
        a,b = np.linalg.lstsq(A, list_y)[0]
        m = np.linalg.lstsq(A, list_y)[1]
        res.append(math.pow(m,0.5)/len(each))
      
print(res , file=sys.stderr)

index = res.index(min(res))

a = 2
b = 1/a

if max(res) < a*sum(res)/len(res) and min(res) > b*sum(res)/len(res):
    print("O(1)")
else:
    if index == 0:
        print("O(n)")
    elif index == 1:
        print("O(log n)")
    elif index == 2:
        print("O(n log n)")
    elif index == 3:
        print("O(n^2)")
    elif index == 4:
        print("O(n^2 log n)")
    elif index == 5:
        print("O(n^3)")
    elif index == 6:
        print("O(2^n)")
    
