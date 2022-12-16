# Zach Pedersen Rylan Casanova
# This is our work!
# Prof. Citro
# CST-305

import numpy as np
import matplotlib.pyplot as plt
import math

# f(x) = ln x
def func(x):
    return math.log(x)

# get variables for Riemann Sum
start = 1
end = math.e
subintervals = 4000
interval = (end - start) / subintervals

# number of points
r = 100
# start conditions
domain = np.linspace(start, end, r)

# gets y values for the graph
y = []
for i in range(0, len(domain)):
    y.append(func(domain[i]))

# finds y range
low = min(y)
high = max(y)

# gets rectangles for Riemann Sum
centerx = []
centery = []
index = start + interval / 2
for i in range(0, subintervals):
    centerx.append(index)
    centery.append(func(index))
    index += interval

# Display plots (center)
fig, ax1 = plt.subplots()
ax1.plot(domain, y)
ax1.set_ylabel('y')
ax1.set_ylim(low, high)

ax2 = ax1.twinx()
ax2.bar(centerx, centery, width=interval, align='center', alpha=0.5, color='red')
ax2.grid(False)
ax2.set_ylim(low, high)

plt.show()

# calculates sum
sumc = 0
for i in centery:
    sumc += i * interval

print("Center Riemann Sum: ", sumc)
print("Granularity: ", subintervals)
