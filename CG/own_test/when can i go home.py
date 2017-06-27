import sys
import time
import math
import matplotlib.pyplot as plt

def to_step(hour):
    a = hour.split(":")
    return int(a[0])*6 + int(a[1])/10

def to_hour(step):
    return "%.2d:%.2d" % ((step//6)%24, 10*(step%6))


K= {"m": 0.7, "f": 0.6}

weight = 65
gender = 'f' #or 'f'
inp = [
    {"v": "75", "t": "40", "s": "23:30"}
]

n = len(inp)
start_time = None

volume = []
percent = []
step_list = []

timelapse = [0]*144
current_level = 0
i_can_drive = True
step_limit_to_drive = None

for i in range(n):
    V = int(inp[i]["v"])
    T = int(inp[i]["t"])
    step = to_step(inp[i]["s"])

    if i == 0:
        start_time = step
    else:
        if step < step_list[-1]:
            step += 24 * 6

    step_list.append(step)
    step -= start_time

    alcool = 0.8 * V * T / 10
    level = alcool / (weight * K[gender])

    for j in range(144):
        if j >= step + 3:
            timelapse[j] += level

consummed_alcohol = 0
for k in range(144):
    if timelapse[k] > 0:
        consummed_alcohol = min(consummed_alcohol, timelapse[k])
        remaining_alcohol = timelapse[k] - consummed_alcohol
        if remaining_alcohol <= 0:
            timelapse[k] = 0
        else:
            timelapse[k] = remaining_alcohol
            consummed_alcohol += (0.1 / 6)

print(timelapse)
plt.plot(timelapse)
plt.show()

if max(timelapse) > 3:
    print("Alcohold Poisonning")
elif max(timelapse) <= 0.5:
    print("Always")
else:
    for l in range(144):
        if timelapse[l] > 0.5:
            i_can_drive = False
        if not i_can_drive and timelapse[l] < 0.5:
            step_limit_to_drive = l
            i_can_drive = True
    print(to_hour(step_limit_to_drive + start_time))
