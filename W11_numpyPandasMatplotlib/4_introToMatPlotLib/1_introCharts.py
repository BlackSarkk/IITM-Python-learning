
# Matplotlib provides useful package for data Visualization

# do:  pip3 install matplotlib
# do:  sudo apt install python3-tk      #This is to view graph 

import matplotlib.pyplot as plt
import numpy as np


#*********************************************
#! Scatter plot:
#*********************************************
#*********************************************

'''
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x, y)   #? plot1

x = np.array([5, 8, 8, 2, 2, 13, 2, 9, 4, 31, 12, 4, 6])
y = np.array([98, 36, 87, 88, 118, 86, 106, 87, 95, 78, 77, 84, 89])
plt.scatter(x, y)   #? plot2

plt.show()
'''



#*********************************************
#! Bar chart:
#*********************************************
#*********************************************

'''
x = np.array([5, 8, 8, 2, 2, 13, 2, 9, 4, 31, 12, 4, 6])
y = np.array([98, 36, 87, 88, 118, 86, 106, 87, 95, 78, 77, 84, 89])
# plt.bar(x, y)       # Vertical Bar Chart
plt.barh(x, y)       # Horizontal Bar Chart

plt.show()
'''


#*********************************************
#! Histogram:
#*********************************************
#*********************************************

'''
# x = np.array([5, 8, 8, 2, 2, 13, 2, 9, 4, 31, 12, 4, 6])
x = np.random.normal(170, 10, 250)
plt.hist(x)       

plt.show()
'''


#*********************************************
#! PieChart:
#*********************************************
#*********************************************

'''
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherry", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.hist(y)       

plt.show()
'''

