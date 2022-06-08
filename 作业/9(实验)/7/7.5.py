from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 30)
P = [1, 3, 1, 4, 0]

plt.subplot(2, 2, 1)
plt.plot(x, np.polyval(P, x), 'r-')

plt.subplot(2, 2, 2)
Q = np.polyder(P)
plt.plot(x, np.polyval(Q, x), 'b--')

plt.subplot(2, 2, 3)
R = np.polyder(Q)
plt.plot(x, np.polyval(R, x), 'g.')

plt.subplot(2, 2, 4)
S = np.polyder(R)
plt.plot(x, np.polyval(S, x), 'y^')
plt.show()
