
import matplotlib.pyplot as plt
import numpy as np

#******************************

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)        # 2 row, 3 col, 1st position
plt.plot(x, y)

#******************************

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 20, 40])

plt.subplot(2, 3, 2)        # 2 row, 3 col, 2nd position
plt.plot(x, y)

#******************************

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)        # 2 row, 3 col, 3rd position
plt.plot(x, y)

#******************************

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 20, 40])

plt.subplot(2, 3, 4)        # 2 row, 3 col, 4th position
plt.plot(x, y)

#******************************

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 20, 40])

plt.subplot(2, 3, 5)        # 2 row, 3 col, 5th position
plt.plot(x, y)



plt.show()