import sys
import math

count = 0
l = int(input())
n = int(input())
previous_plaque = None
for i in range(n):
    plaque, distance, timestamp = input().split()
    distance, timestamp = int(distance), int(timestamp)
    if previous_plaque == plaque:
        v = 3600 * (distance - previous_distance)/(timestamp - previous_timestamp)
        if v > l:
            print(plaque, distance)
            count += 1
    previous_plaque = plaque
    previous_distance = distance
    previous_timestamp = timestamp

if count == 0:
    print("OK")