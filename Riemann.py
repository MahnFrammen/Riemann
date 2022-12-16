# Zach Pedersen Rylan Casanova
# This is our work!
# Prof. Citro
# CST-305

import numpy as np
import matplotlib.pyplot as plt
import math

# f(x) = sinx + 1
def func(x):
    return math.sin(x) + 1

# number of points
r = 100
# start conditions
domain = np.linspace(-math.pi, math.pi, r)

# gets y values for the sine graph
y = []
for i in range(0, len(domain)):
    y.append(func(domain[i]))

# get variables for Riemann Sum
start = -math.pi
end = math.pi
subintervals = 4
interval = (end - start) / subintervals
low = min(y)
high = max(y)

# gets rectangles for Riemann Sum
leftx = []
lefty = []
index = start
for i in range(0, subintervals):
    leftx.append(index)
    lefty.append(func(index))
    index += interval

centerx = []
centery = []
index = start + interval / 2
for i in range(0, subintervals):
    centerx.append(index)
    centery.append(func(index))
    index += interval

rightx = []
righty = []
index = start + interval
for i in range(0, subintervals):
    rightx.append(index)
    righty.append(func(index))
    index += interval

# Display plots (left)
fig, ax1 = plt.subplots()
ax1.plot(domain, y)
ax1.set_ylabel('y')
ax1.set_ylim(low, high)

ax2 = ax1.twinx()
ax2.bar(leftx, lefty, width=interval, align='edge', alpha=0.5, color='red')
ax2.grid(False)
ax2.set_ylim(low, high)

plt.show()

# calculates sum
suml = 0
for i in lefty:
    suml += i * interval

print("Left Riemann Sum: ", suml)
print(lefty)

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
print(centery)

# Display plots (right)
fig, ax1 = plt.subplots()
ax1.plot(domain, y)
ax1.set_ylabel('y')
ax1.set_ylim(low, high)

ax2 = ax1.twinx()
ax2.bar(rightx, righty, width=-interval, align='edge', alpha=0.5, color='red')
ax2.grid(False)
ax2.set_ylim(low, high)

plt.show()

# calculates sum
sumr = 0
for i in righty:
    sumr += i * interval

print("Right Riemann Sum: ", sumr)
print(righty)
