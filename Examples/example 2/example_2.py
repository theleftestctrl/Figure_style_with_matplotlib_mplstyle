import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib

plt.style.use('../../figStyle.mplstyle')

def load_data_from_folder(folder):
    def load(name):
        data = []
        with open(f'{folder}/{name}') as f:
            for line in f:
                data.append([float(x.replace(',', '.')) for x in line.split()])
        return np.array(data)
    return load


load_data = load_data_from_folder('data')

x1 = load_data('A.txt')[:, 0]
y1 = load_data('OX2.txt')[:, 0]
x2 = load_data('B.txt')[:, 0]
y2 = load_data('OX1.txt')[:, 0]

fig, ax = plt.subplots()

ax.plot(x1, y1, color='C2', marker='*', linestyle='', label=r'Концентрация 1-ого вещества')
ax.plot(x2, y2, color='C3', marker='<', linestyle='', label=r'Концентрация 2-ого вещества')

ax.set_xlabel(r'Время, с')
ax.set_ylabel(r'Концентрация')

ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(2))

ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

ax.legend(labelcolor='markeredgecolor')

fig.savefig('example_2.pdf')
