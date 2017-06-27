import random

#Entree

choice = ['X', 'O']
W = 85
H = 85

grid = []
for y in range(H):
    line = []
    for x in range(W):
        line.append(random.choice(choice))
    grid.append(line)

for line in grid:
    print(''.join(line))

start = (28, 40) #line - col
stop = (28, 41)

print('')

for i in range(start[0], stop[0]):
    width = stop[1] - start[1]
    grid[i] = grid[i][:start[1]] + ['O'] * width + grid[i][stop[1]:]

print(H, W)
for line in grid:
    print(''.join(line))

# Solution

def rectangle_from_histogram(H):
    best = (float('-inf'), 0,0,0)
    S = []
    H2 = H + [float('-inf')]
    for right in range(len(H2)):
        x=H2[right]
        left = right
        while len(S) > 0 and S[-1][1] >= x:
            left, height = S.pop()
            rect = (height * (right-left), left, height, right)
            if rect > best :
                best = rect
        S.append((left, x))
    return best


def rectangle_from_grid(P):
    rows = len(P)
    cols = len(P[0])
    t = [0] * cols
    best = None
    for i in range(rows):
        for j in range(cols):
            if P[i][j] == 'O':
                t[j] += 1
            else:
                t[j] = 0
        (area, left, height, right) = rectangle_from_histogram(t)
        alt = (area, left, i, right-1, i-height+1)
        if best is None or best < alt:
            best = alt
    return best

result = rectangle_from_grid(grid)

print(result[0])
print("{}-{}".format(result[1], result[4]))
print("{}-{}".format(result[3], result[2]))