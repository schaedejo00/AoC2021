import numpy as np
import re

with open('input01_1.txt', 'r') as f:
    arr = np.genfromtxt(f, dtype=int, delimiter='\n')
previous = arr[0]

diff = np.zeros(len(arr))
count = 0

for i in range(3, len(arr)):
    sum1 = np.sum(arr[i-3:i])
    sum2 = np.sum(arr[i-2:i+1])

    if (sum2 > sum1):
        count+=1
    print(arr[i-3:i], sum1, arr[i-2:i+1], sum2, count)

print (count)


