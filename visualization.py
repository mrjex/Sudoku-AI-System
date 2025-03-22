#####     VISUALIZATION.PY     #####
#
#   - Responsible for the frontend visualization using matplotlib
#   - This module creates plots to graphically demonstrate the algorithmic performances


import matplotlib.pyplot as plt
import numpy as np


###   SECTION 1 - BACKTRACKING & CONSTRAINT PROPAGATION VISUALIZATION   ###


def initFigure():
    plt.figure()


# Append a Backtracking-and-Constraint-Propagation graph on the same plot.
# Used for displaying multiple backtracking performances for multiple puzzles in one plot.
def appendFigure(run_sp, difficulty):
    # plot the time taken to solve the board using constraint propagation
    plt.semilogy(np.arange(1, len(run_sp) + 1), run_sp, label=f'sp_{difficulty} time per epoch')
    plt.title('Time taken to solve the board')
    plt.xlabel('epoch iteration')
    plt.ylabel('time (seconds)')
    plt.legend()


def showFigure():
    plt.show()



###   SECTION 2 - SIMULATED ANNEALING VISUALIZATION   ###


# Visualize energy required to solve board with Simulated Annealing
def plotEnergyAnnealing(energies_easy, energies_hard):
    initFigure()

    plt.plot(energies_easy, label='energy_easy per epoch')
    plt.plot(energies_hard, label='energy_hard per epoch')
    plt.ylim(bottom=0)
    plt.title('Energy of the board')
    plt.xlabel('epoch iteration')
    plt.ylabel('energy value')
    plt.legend()


# Visualize time required to solve board with Simulated Annealing
def plotTimeAnnealing(run_sa_easy, run_sa_hard):
    initFigure()

    plt.semilogy(np.arange(1, len(run_sa_easy) + 1), run_sa_easy, label='SA_easy time per epoch')
    plt.semilogy(np.arange(1, len(run_sa_hard) + 1), run_sa_hard, label='SA_hard time per epoch')
    plt.title('Time taken to solve the board')
    plt.xlabel('epoch iteration')
    plt.ylabel('time (seconds)')
    plt.legend()


# The entrypoint invoked from main.py that triggers its sub-functions to visualize all aspects of the Simulated Annealing performances
def plotAnnealing(energies_easy, energies_hard, run_sa_easy, run_sa_hard):
    plotEnergyAnnealing(energies_easy, energies_hard)
    plotTimeAnnealing(run_sa_easy, run_sa_hard)
    showFigure()