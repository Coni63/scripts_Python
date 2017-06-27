input()
t=[int(i) for i in input().split()]
if t:print(max([i for i in t if abs(i)==min(map(abs,t))]))
else:print(0)