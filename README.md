# Стандарт оформления рисунков BMSTU Soft Matter Lab

Autor: [Dmitryuk N.A](https://github.com/NikitaDmitryuk), [Libet P.A]()

Laboratory: [Soft Matter Group, Bauman MSTU](http://teratech.ru/en)

Github repository: [FigureStyle_SMLab](https://github.com/NikitaDmitryuk/FigureStyle_SMLab)

---

## Правила оформления рисунков

---

#### Линии, символы и надписи

+ Линии – это теории, интерполяции и т.п. У линии есть формула, нет погрешности.

+ Точки, символы – это данные эксперимента или МД, где есть погрешность.

+ Надписей по минимуму, но все должно быть понятно без лишних объяснений. Рисунок должен "говорить" сам за себя.


#### Размеры поля рисунка

+ 1-колоночный рисунок – ширина 85 мм (предпочтительно), 85 мм.

+ 2-колоночный рисунок – ширина 160 мм (предпочтительно), 150 мм, 170 мм.


#### Размеры рисунков (рамка или оси)

+ 1-колоночный рисунок – 75 мм, 70 мм, 35 мм, 25 мм
+ 2-колоночный рисунок – 75 мм, 70 мм, 55 мм, 50 мм, 35 мм, 30 мм, 25 мм


#### Линии

+ Оси, рамки – 0.2 pt, 0.25pt
+ Линии графиков – 0.35 pt (предпочтительно); 0.2 pt; 0.25 pt; 0.5 pt; 0.7 pt; 1.0 pt –


#### Типы линий

+ Сплошные линии (предпочтительно), иногда – штриховые с длинным или умеренным штрихом (не мелким!).

+ По возможности не использовать штрих-пунктирные или пунктирные линии.

+ Эффективно заполнять рисунками и линиями пространство, не оставлять "пустоты".


#### Символы

Преимущественно – круги, треугольники, квадраты, ромбы, звездочки

Толщина линий – 0.2 pt (предпочтительно); 0,15 pt; 0.25 pt;

Заливка – белый, светло серый


#### Цвета

+ Использовать стандартные цвета. Не использовать оттенков, название которых не знаешь.

+ Следить за сочетаемостью (не допускать "красный-зеленый", "желтый-фиолетовый" и т.п.).

+ Цвет характеризует важность: Красные данные – самые важные, привлекают внимание.

+ Цветовое кодирование – данные, представленные на разных рисунках одним и тем же цветом, соответствуют одному и тому же (например, все данные МД показаны серым или синим, а все теоретические линии -- красным).

+ Цветовое кодирование схожих данных в разных работах.


#### Шрифты

Тип – без насечек, например, arial

Цвет – черный, белый (на темном фоне), красный, синий

Размеры шрифтов:

+ 9 pt, bold – обозначения панелей (а), (b) ...

+ 8 pt – для подписей на осях рисунков, надписях над рисунками

+ 7 pt – цифры на осях рисунков

+ 7 pt, 8 pt – надписи внутри рисунков

+ 7 pt, 6 pt – надписи в инсетах, на осях и внутри


[***Полная версия требований к оформлению тут.***](https://github.com/NikitaDmitryuk/FigureStyle_SMLab/blob/main/SMLab-Guide-Graphics-References.docx.pdf)

---

## Создание рисунков с использованием Matplotlib

---

[**Matplotlib**](https://matplotlib.org/stable/index.html#) -- Удобная библиотека для создания графики, в том числе научной.

Одним из самых удобных функционалов является создание *.mplstyle* файлов, в которых можно настроить единый стиль для всех сотрудников нашей лаборатории.

[**Файл 'figStyle_SMLab.mplstyle'**](https://github.com/NikitaDmitryuk/FigureStyle_SMLab/blob/main/figStyle_SMLab.mplstyle) задает все параметры, указанные выше в требованиях к рисункам. Это делает код более локаничным и простым, и позволяет создавать графики с одинавыми параметрами для рисунков к статье при работе в коллективе.

### Настройка среды

#### Установка необходимых пакетов

```shell
pip3 install numpy matplotlib scipy
```

#### Установка шрифта Arial и других шрифтов Windows (Manjaro linux)

Необходимо установить пакет *ttf-ms-fonts*.

```shell
sudo pacman -S ttf-ms-fonts
```

#### Если python не находит шрифт (Manjaro linux)

Необходимо удалить файл *~/.cache/matplotlib/fontlist.json*.

```shell
rm -i ~/.cache/matplotlib/fontlist*.json
```


### Использование готового стиля SMLab

Для использования [файла стиля](https://github.com/NikitaDmitryuk/FigureStyle_SMLab/blob/main/figStyle_SMLab.mplstyle) необходимо добавить следующую строку в программу:

```python
import matplotlib.pyplot as plt
plt.style.use('figStyle_SMLab.mplstyle')
```

Внутри файла сверху находятся использованные настройки с кратикими комментариями.
Ниже находятся неиспользованные настройки с более подробными комментариями, их можно использовать по необходимости.

---

## Основные используемые функции

---

#### Загрузка данных


```python
def load_data_from_folder(folder):
    def load(name):
        data = []
        with open(f'{folder}/{name}') as f:
            for line in f:
                data.append([float(x.replace(',', '.')) for x in line.split()])
        return np.array(data)
    return load
```

Указание папки с данными (частичное применение функции):

```python
load_data = load_data_from_folder('path/to/data')
```

Чтение данных из разных файлов:

```python
x1 = load_data('A.txt')[:, 0]    # Чтение первого столбца
y1 = load_data('B.txt')[:, 1]    # Чтение второго столбца
x2 = load_data('C.txt')[0, :]    # Чтение первой строки
y2 = load_data('D.txt')[1, :]    # Чтение второй строки
```

#### Построение графика

Cоздание рисунка:

```python
fig, ax = plt.subplots()        # Создание поля для рисунка (fig) и осей (ax)
```

Рисование двух линий:

```python
ax.plot(x1, y1, color='C0', marker='', linestyle='-', label=r'$\frac{a}{b}$')
ax.plot(x2, y2, color='C1', marker='o', linestyle='', label=r'Класс 2 (канал B)', zorder=2)
```

Где:

+ *color* -- цвет линий / точкек. Стандартные цвета *C0, C1, .. , C9*, также можно задать как *(0.5, 0.5, 0.5)* где от 0 до 1 указаны значения RGB. [Eсть и другие способы и цвета.](https://matplotlib.org/stable/users/dflt_style_changes.html)

+ marker -- Символы точек. Самые часто используемые: 'o' -- полые круги, '' -- сплошная линия без символов. [Все виды символов тут](https://matplotlib.org/stable/api/markers_api.html).

+ linestyle -- Тип соединяющих линий. Часто используемые: '' -- соединения точек нет, '\-' -- сплошная линия, '\-\-' -- штриховая линия. [Все виды линий и создание своих тут](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html).

+ label -- Метка для легенды. Форматирование строк c префиксом **r** например *r'$ T_{cp} / T_{tp} = 2.0 $'* указывает на необходимоть компилировать эту строку с использованием Latex.

***Информация по всем параметрам функции *pyplot.plot* в одном [месте](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html).***

+ zorder -- приоритет наложения графиков. Лини, у которой данный параметри больше, чем у другой, находится выше. Если параметры одинаковые (по умолчанию), то располагаются в порядке рисования.


**Создание подписей к осям**

```python
ax.set_xlabel(r'Wave vector, $kn^{-1/3}/\pi$')
ax.set_ylabel(r'Frequency, $\omega$')
```

**Пределы рисования**

```python
ax.set_ylim(bottom=0, top=1)
ax.set_xlim(left=0, right=1)
```

**Явное указание больших и маленьких штрихов на осях:**

```python
import matplotlib.ticker as ticker

ax.xaxis.set_major_locator(ticker.MultipleLocator(20)) # Шаг больших меток
ax.xaxis.set_minor_locator(ticker.MultipleLocator(4))  # Шаг маленьких меток
# Аналогично для другой оси
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
```

**Создание легенды**

```python
ax.legend(loc=2, labelcolor='markeredgecolor')
```

где *loc* -- позиция легенды на графике. Часто используется *loc='best'*; *labelcolor* -- цвет текста (в данном случае по цвету маркеров).

[**Полная информация по легендам.**](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)

**Сохранение графика**

```python
fig.savefig('filename.pdf')
```


---

## Редко используемые функции, но не менее важные

---

**Текст на графике**

```python
ax.text(pos_x, pos_y, 'Text',
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes)
```

Можно использовать для автоматического обозначения панелей (**(a)**, **(b)**, ... ).


**Стрелочки**

```python
style_arrow = mpatches.ArrowStyle('-|>', head_length=.2, head_width=.08)

ax.annotate('Text',
            xy=(x2[0], y2[0]), xycoords='data',
            xytext=(0, 20), textcoords='offset points',
            arrowprops=dict(arrowstyle=style_arrow, lw=0.8, fc="k", ec="k"),
            bbox=dict(pad=-0.5, facecolor="white", edgecolor="white"),
            ha='center', va='top')
```

**Горизонтальные и вертикальные линии**

```python
ax.hlines(y, x_min, x_max, linestyles='-', color='C7', zorder=1) # горизонтальная линия
ax.vlines(x, y_min, y_max)                                       # вертикальные линии
```

**Логарифмические оси**

```python
ax.set_xscale('log')
ax.set_yscale('log')
```

**Конкретные значения цифр на осях**

```python
ax.set_xticks([1, 10, 100])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

ax.set_yticks([0.01, 0.1, 1])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
```

**Error bar**

```python
ax.errorbar(x, y, err)
```

**Множители осей**

```python
plt.ticklabel_format(axis='y', style='sci', scilimits=(-2, 3))
```

**Color bar**

```python
cntr = ax.tricontourf([x, y], z, levels=levels, cmap='jet')
fig.colorbar(cntr, ticks=[1, 2, 3])
```
