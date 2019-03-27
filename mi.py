import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

x = np.arange(0, 100, 10)


y1 = [11 for i in x]
plt.plot(x, y1, linewidth=2, label='我')

y2 = [17 for j in x]
plt.plot(x, y2, linewidth=2, label='李嘉诚，马云，马化腾')

plt.legend(loc='right')
plt.show()
