import os
import matplotlib.pyplot as plt

matchlst = []
nomatchlst = []

with open('result.txt') as f:
    lines = f.readlines()
    for l in lines:
        match, nomatch = [float(x) for x in l.strip().split(',')]
        matchlst.append(match)
        nomatchlst.append(nomatch)
    
axes = plt.gca()
axes.set_ylim([0.3, 1.0])
plt.xlabel('Trail')
plt.ylabel('Score')

plt.plot([1, 2, 3, 4, 5], matchlst, 'go-', label='line 1')
plt.plot([1, 2, 3, 4, 5], nomatchlst, 'ro-',  label='line 2')
plt.show()