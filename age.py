import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xticks([])
    plt.yticks([])
    x = np.linspace(0, 2, 1000)
    plt.plot(x, x ** 2)
    plt.title("Ideal Life")
    plt.xlabel("Age")
    plt.ylabel("Money,Knowledge,Handsomeness")
    plt.annotate('ME', xy=(1, 1), xytext=(0.5, 2), arrowprops=dict(facecolor='red', shrink=0.08))
    plt.show()
