
import math
import scipy
import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from scipy import interpolate
import matplotlib
import sys
import os
import subprocess
from matplotlib import rc

plt.style.use('../../figStyle_SMLab.mplstyle')

def load_data_from_folder(folder):
    def load(name):
        data = []
        with open(f'{folder}/{name}') as f:
            for line in f:
                data.append([float(x.replace(',', '.')) for x in line.split()])
        return np.array(data)
    return load


load_data = load_data_from_folder('data')

x1 = load_data('fig11a_1.txt')[:, 0] # Чтение данных из файла
y1 = load_data('fig11a_1.txt')[:, 1]

x2 = load_data('fig11a_2.txt')[:, 0] # Чтение данных из файла
y2 = load_data('fig11a_2.txt')[:, 1]

x3 = load_data('fig11a_3.txt')[:, 0] # Чтение данных из файла
y3 = load_data('fig11a_3.txt')[:, 1]

x4 = load_data('fig11a_4.txt')[:, 0] # Чтение данных из файла
y4 = load_data('fig11a_4.txt')[:, 1]


fig, ax = plt.subplots()

ax.plot(x1[::1], y1[::1], marker='o', color='C0', linestyle='', label=r'$T = 0.6$')
ax.plot(x1, y1, marker='', color='C7', linestyle=':', zorder=1)

ax.plot(x2[::1], y2[::1], marker='o', color='C3', linestyle='')

ax.plot(x3[::1], y3[::1], marker='o', color='C1', linestyle='', label=r'$T = 0.57$')
ax.plot(x3, y3, marker='', color='C7', linestyle=':', zorder=1)

ax.plot(x4[::1], y4[::1], marker='o', color='C3', linestyle='')

style_arrow = mpatches.ArrowStyle('-|>', head_length=.2, head_width=.08)

ax.annotate(r'$G_6$',
            xy=(x2[0], y2[0]), xycoords='data',
            xytext=(0, 20), textcoords='offset points',
            arrowprops=dict(arrowstyle=style_arrow, lw=0.8, fc="k", ec="k"),
            bbox=dict(pad=-0.5, facecolor="white", edgecolor="white"),
            ha='center', va='top')

ax.annotate(r'$G_t$',
            xy=(x2[-1], y2[-1]), xycoords='data',
            xytext=(0, 20), textcoords='offset points',
            arrowprops=dict(arrowstyle=style_arrow, lw=0.8, fc="k", ec="k"),
            bbox=dict(pad=-0.5, facecolor="white", edgecolor="white"),
            ha='center', va='top')

ax.annotate(r'$G_6$',
            xy=(x4[0], y4[0]), xycoords='data',
            xytext=(0, -20), textcoords='offset points',
            arrowprops=dict(arrowstyle=style_arrow, lw=0.8, fc="k", ec="k"),
            bbox=dict(pad=0.5, facecolor="white", edgecolor="white"),
            ha='center', va='bottom')

ax.annotate(r'$G_t$',
            xy=(x4[-1], y4[-1]), xycoords='data',
            xytext=(0, -20), textcoords='offset points',
            arrowprops=dict(arrowstyle=style_arrow, lw=0.8, fc="k", ec="k"),
            bbox=dict(pad=0.5, facecolor="white", edgecolor="white"),
            ha='center', va='bottom')


ax.set_xlabel(r'Density, $\rho$') # r для компиляции формул с latex
ax.set_ylabel(r'Pressure, $P$')

ax.hlines(0, 0.5, 1.3, linestyles='-', color='C7', zorder=1)

# Метки ось X
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))  # шаг больших меток
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.02))  # шаг маленьких меток

ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

# пределы рисования
ax.set_xlim(left=0.95, right=1.23)
ax.set_ylim(bottom=-1.25, top=1.75) # 1.75

ax.legend(loc='best', labelcolor='markeredgecolor')

fig.savefig('example_2.pdf')
