import numpy as np
import matplotlib.pyplot as plt
import script

N = 5
T1 = 50
T2 = 14
sample_per_step = 100

timer_throw_Methode1 = []
timer_count_Methode1 = []
timer_total_Methode1 = []
timer_throw_Methode2 = []
timer_count_Methode2 = []
timer_total_Methode2 = []
timer_throw_Methode3 = []
timer_count_Methode3 = []
timer_total_Methode3 = []

for i in range(1, N+1):
    timer = script.main(i * sample_per_step, T1, T2)
    timer_throw_Methode1.append(timer[0][0])
    timer_count_Methode1.append(timer[0][1])
    timer_total_Methode1.append(timer[0][2])
    timer_throw_Methode2.append(timer[1][0])
    timer_count_Methode2.append(timer[1][1])
    timer_total_Methode2.append(timer[1][2])
    timer_throw_Methode3.append(timer[2][0])
    timer_count_Methode3.append(timer[2][1])
    timer_total_Methode3.append(timer[2][2])

ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars
space = 0.05

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width - space, timer_throw_Methode1, width, color='r')
rects2 = ax.bar(ind - width - space, timer_count_Methode1, width, color='b', bottom=timer_throw_Methode1)
rects3 = ax.bar(ind, timer_throw_Methode2, width, color='r')
rects4 = ax.bar(ind, timer_count_Methode2, width, color='b', bottom=timer_throw_Methode2)
#rects5 = ax.bar(ind + width + space, timer_throw_Methode3, width, color='r')
#rects6 = ax.bar(ind + width + space, timer_count_Methode3, width, color='b', bottom=timer_throw_Methode3)
rects7 = ax.bar(ind + width + space, timer_total_Methode3, width, color='y')

ax.set_ylabel('Time (s)')
ax.set_title('time per Methode and per size of samples')
ax.set_xticks(ind + width / 2 - 2 * space)
ax.set_xticklabels([sample_per_step * T1 * x for x in range(1, N+1)])

ax.legend((rects1[0], rects2[0], rects7[0]), ('Throwing time (Meth 1 & 2)', 'Counting time (Meth 1 & 2)', 'total time (Meth 3)'))

plt.show()
