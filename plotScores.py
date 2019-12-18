import matplotlib.pyplot as plt
import numpy as np

#Description
#x axis trial #
#y axis similarity score 0-1
#index corresponds to certain pairing of audio files so match records 1 if was supposed to be a match & 0 if not


#from model1

#TEST X
x = [1, 2, 3, 4, 5]
#y made by output redirecting (appending) output of model1 to a new file, vim search and replacing to get rid of extra output/ add commas
y = [0.9034163951873779, 0.6532658934593201, .5, .5, .5]

#not a match
xNot = [1, 2]
yNot = [.6, .5]

#from model2 with male and female voices; from print of model
#match = [1, 0, 0, 1, 0, 0, 0]
#x = [1, 1, 1, 1, 1, 1, 1]
#y = [0.8891976475715637, 0.8869891166687012, 0.8723126649856567, 0.910430371761322, 0.8662552237510681, 0.9034217596054077, 0.8281809091567993]

plt.figure() 
plt.plot(x, y, 'g')
plt.plot(xNot, yNot, 'r')
#plot line for the threshold determined by similarity score key1 vs key2
#args y, xmin, xmax for the line overall xmin and xmax is 0 and 1
#plt.axhline(y[0], 0, .5, linestyle='--') 
#plt.axhline(y[5], .5, 1, linestyle='--') 
plt.xticks(np.arange(min(x), max(x)+1))
plt.title('Model 1')
plt.xlabel('Trial Number')
plt.ylabel('Similarity Score (0-1)')
plt.show()

