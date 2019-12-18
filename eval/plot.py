import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

with open('result.txt') as f:
    lines = f.readlines()
    l1 = lines[0]
    match= [float(x) for x in l1.strip().split(',')]
    l2 = lines[1]
    nomatch = [float(x) for x in l2.strip().split(',')]


axes = plt.gca()
axes.set_ylim([0.3, 1.0])
plt.xlabel('User Sets')
plt.ylabel('Score')

plt.plot([2, 4], match, 'go-', label='line 1')
plt.plot([1, 3, 5, 6], nomatch, 'ro-',  label='line 2')

red = mpatches.Patch(color='red', label='Non-matching Audio Sets')
green = mpatches.Patch(color='green', label='Matching Audio Sets')

plt.legend(handles=[red, green], loc='lower left')

plt.show()
