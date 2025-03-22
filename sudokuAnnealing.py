from math import exp
import random
import time
import numpy as np
from itertools import repeat
import utils


class SudokuAnnealing:

    # Initialize Simulated Annealing object along with its decreasing energies
    def __init__(self, board, puzzleFile):
        self.exec_time = [0.] # Initialize timer
        self.board = np.array(list(board.replace('.', '0'))).reshape(9, 9).astype(int)
        self.max_temperature = 10
    
        utils.displayUnsolvedBoardUI(self, puzzleFile, "annealing", None)

        mask = (self.board == 0)
        self._guesses = np.argwhere(mask)
        self.board[mask] = np.random.randint(1, self.max_temperature, size=np.count_nonzero(mask))

        # Initialize variables simulating the physical annealing process
        self._cooling_rate = 0.021
        self._temperature = 0.502

        self._energy = self.getGlobalBoardEnergy()

    def solve(self):
        energies = []

        # Iterate while the current temperature of the object is less than the max temperature
        while self._temperature < self.max_temperature:
            start_time = time.perf_counter()

            for _ in repeat(None, 5000):
                self._metropolisAlgorithm()

            self.exec_time.append((time.perf_counter() + self.exec_time[-1] - start_time)) # Update required time to solve board

            self._energy = self._global_energy()  # Access global energy of board
            energies.append(self._energy)

            # Exit if no energy left
            if self._energy <= 0:
                break

            self._temperature *= (1.0 + self._cooling_rate)  # Simulate the temperature adjustment rate
        return energies  # Return energies

    # Returns a cell's local energy
    def _local_energy(self, row, col):
        energy = 0

        # Identify the column, row and subgrid of a cell
        for i in [self.board[row, :],
                  self.board[:, col],
                  self.board[(row // 3) * 3:(row // 3 + 1) * 3,
                  (col // 3) * 3:(col // 3 + 1) * 3].flatten()]:
            occ = np.bincount(i)
            energy += np.sum(occ[occ > 1])

        return energy

    # Returns the total energy of the entire board (also known as the global energy)
    def _global_energy(self):
        energy = 0 
        cols = [0, 3, 6, 1, 4, 7, 2, 5, 8]  # List of equally distributed columns
        numRows = 9

        for i in range(numRows):
            energy += self._local_energy(i, cols[i]) # Sum up each cell's local energy
        return energy

    def _metropolisAlgorithm(self):
        row, col = random.choice(self._guesses)  # get a random cell (since simulated annealing is a random searching technique)

        # Read previous values and energies
        old_energy = self._local_energy(row, col)
        old_value = self.board[row, col]

        # Assign a randomized value to a cell and read the change in terms of energy
        self.board[row, col] = np.random.randint(1, self.max_temperature)
        delta_energy = self._local_energy(row, col) - old_energy

        # If the change of energy is negative or the estimated probability is below the defined threshold, then return
        if delta_energy < 0 or random.uniform(0.0, 1.0) < exp(-self._temperature * delta_energy):
            return
        else:
            self.board[row, col] = old_value # Revert the cell's value to the old value

    # Print the board visually on the developer's terminal output
    def display(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")
        print('\n')
    
    def getGlobalBoardEnergy(self):
        return self._global_energy()