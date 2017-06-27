from math import sin, cos, floor, radians, ceil

r = 1
arr = []
for i in range(r*2+1):
    arr.append(["0"]*(2*r+1))

if r % 2 == 0:
    arr[r][r] = "+"
else:
    arr[r][r] = "+"

for alpha in range(360):
    alpha = radians(alpha)
    y = round( r * (1 - cos(alpha)))
    x = round( r * (1 + sin(alpha)))
    arr[y][x] = "#"


for each in arr:
    print("".join(each))

