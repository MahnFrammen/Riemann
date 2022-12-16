# Zach Pedersen Rylan Casanova
# This is our work
# Prof. Citro
# CST-305

import numpy as np
import matplotlib.pyplot as plt
import math

# get variables for Riemann Sum
start = 0
end = 30
subintervals = 30
interval = (end - start) / subintervals

# start conditions
domain = np.linspace(0, 30, 31)

# gets y values for the graph
y = [15.9, 21.5, 23.5, 23.6, 23.6, 22.9,
     23.7, 23.8, 23.6, 23.7, 23.6,
     23.6, 23.2, 23.7, 23.8, 23.7,
     23.9, 23.6, 23.7, 23.7, 23.6,
     23.6, 23.6, 23.6, 23.3, 18.0,
     18.0, 17.9, 17.8, 17.9, 18.0]

for i in range(0, len(y)):
    y[i] *= 60

# finds y range
low = min(y)
high = max(y)

# Display plots (center)
fig, ax1 = plt.subplots()
ax1.plot(domain, y)
ax1.set_ylabel('MB/min')
ax1.set_xlabel('minute')
ax1.set_ylim(0, high)

# set bar graph
y.pop()
domain = np.linspace(0, 29, 30)

ax2 = ax1.twinx()
ax2.bar(domain, y, width=interval, align='edge', alpha=0.5, color='red')
ax2.grid(False)
ax2.set_ylim(0, high)

plt.show()

# calculates sum
sumc = 0
for i in y:
    sumc += i * interval

print("Left Riemann Sum: ", sumc)
print("Granularity: ", subintervals)
