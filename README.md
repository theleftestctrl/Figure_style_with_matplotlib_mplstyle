# Matplotlib_style_for_articles
Matplotlib style for articles
## Use

```shell
import matplotlib.pyplot as plt
plt.style.use('./article_style.mplstyle')
```
## Настройка шрифтов

### Установка шрифта Arial и других шрифтов Windows

Необходимо установить пакет *ttf-ms-fonts*.

```shell
sudo pacman -S ttf-ms-fonts
```

### Если python не находит шрифт

Необходимо удалить файл *~/.cache/matplotlib/fontlist.json*.

```shell
rm -i ~/.cache/matplotlib/fontlist*.json
```

## Установка необходимых пакетов

```shell
pip3 install numpy matplotlib scipy
```

