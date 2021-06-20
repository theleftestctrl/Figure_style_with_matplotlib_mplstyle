import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib

plt.style.use('../figStyle.mplstyle') # Загрузка стиля

def load_data_from_folder(folder):
    def load(name):
        data = []
        with open(f'{folder}/{name}') as f:
            for line in f:
                data.append([float(x.replace(',', '.')) for x in line.split()])
        return np.array(data)
    return load


load_data = load_data_from_folder('/home/nikita/Yandex.Disk/SoftMatter/Python scripts/Matplotlib_style_for_articles/Example/data')

time = load_data('time.txt')[:, 0] # Чтение данных из файла
class_a = load_data('A.txt')[:, 0] # Чтение данных из файла
class_b = load_data('B.txt')[:, 0] # Чтение данных из файла
class_с = load_data('С.txt')[:, 0]

fig = plt.figure() # Создание графика и осей
fig, ax = plt.subplots()
# рисуем графики


ax.plot(time, class_a, color='C0', marker='o', linestyle='', label=r'Класс 1 (канал A)')
ax.plot(time, class_b, color='C1', marker='o', linestyle='', label=r'Класс 2 (канал B)')
ax.plot(time, class_с, color='C2', marker='o', linestyle='', label=r'Класс 3 (канал С)')

ax.set_xlabel(r'Время, с')
ax.set_ylabel(r'Концентрация общего гемоглобина, мкМ/л')


# Метки ось X
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))  # шаг больших меток
ax.xaxis.set_minor_locator(ticker.MultipleLocator(4))  # шаг маленьких меток

ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

# пределы рисования
#ax.set_xlim(left=0.85, right=160)
#ax.set_ylim(bottom=-0.1, top=0.51)

ax.legend(labelcolor='markeredgecolor') # рисование легенды. loc отвечаеет за расположение

fig.savefig('example.pdf')
