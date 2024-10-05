import numpy as np
import matplotlib.pyplot as plt

def f(n, r, primary):
 return primary * (1+r/100)**n

r = 5
primary = 100
x = np.linspace(1, 99)
y = f(x, r, primary)
plt.plot(x, y)
plt.show()