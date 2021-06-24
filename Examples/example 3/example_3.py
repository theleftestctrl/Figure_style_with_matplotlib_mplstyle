 
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib

plt.style.use('../../figStyle_SMLab.mplstyle')

def load_data_from_folder(folder):
    def load(name):
        data = []
        with open(f'{folder}/{name}') as f:
            for line in f:
                data.append([float(x.replace(',', '.')) for x in line.split()])
        return np.array(data)
    return load


def plot_phase_diagram(fig, ax, path_data, step, label, markersize, color, max_tmp_plot):
    
    load_data = load_data_from_folder(path_data)
    
    data = load_data('phase.txt')
    
    tmp = data[:, 0]
    
    tmp_new = data[:, 0][tmp <= max_tmp_plot][::step]
    
    condens_dens = data[:, 1][tmp <= max_tmp_plot][::step]
    condens_dens_err = data[:, 2][tmp <= max_tmp_plot][::step]
    
    gas_dens = data[:, 3][tmp <= max_tmp_plot][::step]
    gas_dens_err = data[:, 4][tmp <= max_tmp_plot][::step]

    board_dens = data[:, 5][tmp <= max_tmp_plot][::step]
    board_dens_err = data[:, 6][tmp <= max_tmp_plot][::step]


    ax.errorbar(condens_dens, tmp_new, xerr=condens_dens_err, marker='o', linestyle='', markersize=markersize, color=color, label=label)
    ax.errorbar(gas_dens, tmp_new, xerr=gas_dens_err, marker='o', linestyle='', markersize=markersize, color=color)
    ax.errorbar(board_dens, tmp_new, xerr=board_dens_err, marker='o', linestyle='', markersize=markersize, color=color)
    
    
    data_fit = load_data('phase_fit.txt')
    
    fit_tmp_condens = data_fit[:, 0][::step]
    fit_dens_condens = data_fit[:, 1][::step]
    extr_tmp_condens = data_fit[:, 2][::step]
    extr_dens_condens = data_fit[:, 3][::step]
    
    fit_tmp_gas = data_fit[:, 4][::step]
    fit_dens_gas = data_fit[:, 5][::step]
    extr_tmp_gas = data_fit[:, 6][::step]
    extr_dens_gas = data_fit[:, 7][::step]
    
    fit_tmp_board = data_fit[:, 8][::step]
    fit_dens_board = data_fit[:, 9][::step]
    extr_tmp_board = data_fit[:, 10][::step]
    extr_dens_board = data_fit[:, 11][::step]
    
    
    ax.plot(fit_dens_condens, fit_tmp_condens, marker='', linestyle='-', color=color)
    ax.plot(extr_dens_condens, extr_tmp_condens, marker='', linestyle='--', color=color)
    
    ax.plot(fit_dens_gas, fit_tmp_gas, marker='', linestyle='-', color=color)
    ax.plot(extr_dens_gas, extr_tmp_gas, marker='', linestyle='--', color=color)
    
    ax.plot(fit_dens_board, fit_tmp_board, marker='', linestyle='-', color=color)
    ax.plot(extr_dens_board, extr_tmp_board, marker='', linestyle='--', color=color)
    
    
    data_cp = load_data('phase_point_cp_tp.txt')
    
    tmp_cp = data_cp[:, 0]
    dens_cp = data_cp[:, 2]
    
    ax.plot(dens_cp, tmp_cp, marker='*', linestyle='', color=color, markeredgecolor='k', markerfacecolor=color, zorder=3)


if __name__ == '__main__':
    
    fig, ax = plt.subplots()
    
    plot_phase_diagram(fig=fig, ax=ax, path_data='data/flat_layer', step=2, label='Flat layer', markersize=2, color='C0', max_tmp_plot=1.28)
    plot_phase_diagram(fig=fig, ax=ax, path_data='data/dbscan', step=2, label='DBSCAN', markersize=2, color='C1', max_tmp_plot=1.28)
    
    ax.set_xlabel(r'Density, $\rho$')
    ax.set_ylabel(r'Temperature, $T$')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.04))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.04))
    ax.set_xlim(left=0, right=1.04)
    ax.set_ylim(bottom=0.5, top=1.35)
    ax.legend(loc='best', labelcolor=['C0', 'C1'])
    
    fig.savefig('example_3.pdf')
