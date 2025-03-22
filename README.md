# AI Project - Joel Mattsson's Sudoku System

This system was developed as an individual assignment in 2024 October during my exchange studies in Italy. It covers Sudoku with recursion as well as optimization. As the first introductory assignment of `Foundations of Artificial Intelligence` we had the opportunity to compare backtracking depth-first-search based approach to a local-search based one. The interesting topic of this assignment is the optimization that Simulated Annealing uses, as it simulates in one way or another artificial intelligence, considering the concept of trial and error and learning from past experiences as a normal human being.


## Table of Contents

- [AI Project - Joel Mattsson's Sudoku System](#ai-project---joel-mattssons-sudoku-system)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Configuration Demos](#configuration-demos)
      - [Backtracking \& Constraint Propagation](#backtracking--constraint-propagation)
      - [Simulated Annealing](#simulated-annealing)
  - [Adding your own puzzle](#adding-your-own-puzzle)
  - [System Overview](#system-overview)
    - [Python Modules](#python-modules)
    - [Directories](#directories)
      - [Puzzles Directory](#puzzles-directory)
      - [Performances Directory](#performances-directory)
      - [Graphs Directory](#graphs-directory)



## Getting Started

This is a brief introduction to getting started and setting up this project. In order to interact and run the project, there are two files you need to pay attentiont to:

- **main.py:** This is the only entrypoint of the system. All you need to do is to run this script. No modifications in this file is needed, as there are no configuration variables located in this file.

- **utils.py:** This is the only file with modifiable configuration variables. The system I constructed provides options for you as the developer. Essentially, there are 5 variables you need to be aware:

  - `runBacktrackConstraintAlgorithm` is a boolean and allows you to toggle between running the backtracking and simulated annealing algorithm.

  - `OPTION` is an integer with possible values ranging from 1-3. Note that Simulated Annealing does not provide an option for executing preferences and always defaults to running two puzzles in parallel. However, the backtracking algorithm has three different options for running puzzles based on what you initialize the variable to. Setting it to 1 indicates that only ONE selected puzzle will be executed when you run *main.py*. The second option runs two puzzles and compares them, and the third option runs a list of puzzles in the same go.

  - `SELECTED_PUZZLE` Represents the ONE puzzle you want to run if you set **OPTION=1** and **runBacktrackConstraintAlgorithm=True**. Once again, the first option is only applicable to the backtracking algorithm, and assigning the boolean to false would mean that the simulated annealing algorithm is executed on its one an only option, which is governed by the next variable.

  - `EASY_HARD_PUZZLES` is a dictionary of **two** key-value pairs, where the values are directories to the corresponding .txt puzzles. The puzzles contained in this variable will be executed if you set **OPTION=2** or if you set **runBacktrackConstraintAlgorithm=False** to run Simulated Annealing. In other words, this is an option for both backtracking and simulated annealing algorithms.

  - `SELECTED_PUZZLES_LIST` is a list of all the puzzles that will be solved when running the program. Set **OPTION=3** and **runBacktrackConstraintAlgorithm=True** to successfuly enable this option


### Configuration Demos

Considering the options available in *utils.py*, there are **4 different settings in total** that you as a developer can configure to run the system. Below, each and every possible configuration is demonstrated when executing the system:


#### Backtracking & Constraint Propagation

*Run **ONE** puzzle:*

![backtrack-option-1](readme-material/backtrack-option1.mp4)


*Run **TWO** puzzles:*

![backtrack-option-2](readme-material/backtrack-option2.mp4)


*Run **MULTIPLE** puzzles:*

![backtrack-option-3](readme-material/backtrack-option3.mp4)


#### Simulated Annealing

*Run **TWO** puzzles:*

![simulated-annealing](readme-material/simulated-annealing.mp4)


## Adding your own puzzle

To add your own puzzle and solve it with this program, you need to paste it into a .txt file in `/tests` directory, and then, based on your configured settings in `utils.py`, specify its path in the corresponding variable (*SELECTED_PUZZLE*, *EASY_HARD_PUZZLES* or *SELECTED_PUZZLES_LIST*). The format must also conform to those of which are supported by the system. In essence, the following cases are supported:

- Accepts **'.'** and **'0'** as empty cells

- Accepts **space separation** of all cells

- Accepts **'|'** as a boundary between subgrids


If the format of your puzzle is **invalid** or if the puzzle is **unsolvable**, the terimal will output the follwing message:

- *The provided Sudoku board in at least one of `{SELECTED_PUZZLE_FILES_HERE}` is either unsolvable or has invalid formatting. Keep in mind that all direct and indirect constraints of the input board must be satisfied, and check the formatting of the other .txt files in '/puzzles' directory.*


Now, two boards of valid formatting will be displayed to avoid confusion:


*Example 1 - All cells are empty:*

```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

*Example 2 - Using '|' to separate subgrids*

```
5 3 . |. 7 . |. . .
6 . . |1 9 5 |. . .
. 9 8 |. . . |. 6 .
------+------+------
8 . . |. 6 . |. . 3
4 . . |8 . 3 |. . 1
7 . . |. 2 . |. . 6
------+------+------
. 6 . |. . . |2 8 .
. . . |4 1 9 |. . 5
. . . |. 8 . |. 7 9
```

Lastly, specify the name of the .txt file in *utils.py* and run the entrypoint *main.py*



## System Overview

Before presenting the obtained results, a brief overview of the developed system’s modules and abilities will be explained, since the results are acquired/gathered/based on the system’s structure.

![system-data-flow](readme-material/system-data-flow.PNG)


### Python Modules

- **utils.py:** Developer configurations and refactored general functions used across many Python modules

- **main.py:** Main entrypoint of system. Execution input and output occurs in this file. Imports all other modules

- **visualization.py:** Only responsible for the fronted plotting using matplotlib. It reads the data generated from *sudokuPropagation.py* and *sudokuAnnealing.py* via their respective declared objects in *main.py*

- **sudokuPropagation.py:** Implemented functionality for the *Backtracking & Constraint Propagation* approach, refactored into an object. Note that many general functions are used from the imported module *utils.py*

- **sudokuAnnealing.py:** Implemented functionality for the *Simulated Annealing* approach, refactored into an object. Note that many general functions are used from the imported module *utils.py*

- **puzzleParser:** Responsible for parsing a given Sudoku puzzle from a .txt file in `/puzzles` directory into a format comprehensible for this system. More specifically, *sudokuAnnealing.py* and *sudokuPropagation.py* expects to recieve the parsed formats. Decomposed into 3 main parts, the parsing method looks like this:


*Step 1 - Read .txt file*

```
5 3 . |. 7 . |. . .
6 . . |1 9 5 |. . .
. 9 8 |. . . |. 6 .
------+------+------
8 . . |. 6 . |. . 3
4 . . |8 . 3 |. . 1
7 . . |. 2 . |. . 6
------+------+------
. 6 . |. . . |2 8 .
. . . |4 1 9 |. . 5
. . . |. 8 . |. 7 9
```


*Step 2 - Divide each subgrid by their row*

```
53..7....6..195....98....6.
8...6...34..8.3..17...2...6
.6....28....419..5....8..79
```


*Step 3 - Concatinate each subgrid row*

```
53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79
```


### Directories

There are three directories, each with their own distinct objectives, that make up for the entirety of the system and its multitude of offered features. In order to properly understand the system, it's crucial to be familiar with how they collaborate throughout the execution.

#### Puzzles Directory

This directory contains a collection of .txt files of Sudoku puzzles that are parsed and solved as the system is executed.

#### Performances Directory

This directory contains two .json files that are generated during the runtime of the system. Both of these hold data of recursive iterations and backtracking exclusively related to the first approach, *Backtracking & Constraint Propagation*. Note that in *utils.py*, you must run this particular approach by configuring one of the following settings:

```
runBacktrackConstraintAlgorithm = True

OPTION = { 1, 3 }
```


#### Graphs Directory

This directory contains .png files of the graphs generated as you run the system. These graphs are visual representations of the *Simulated Annealing* and *Backtracking & Constraint Propagation* approaches.

**Backtracking & Constraint Propagation:**

![backtracking-output](graphs/run-all-puzzles-backtracking.PNG)

**Simulated Annealing:**

*Energies:*

![sa-energies](graphs/simulated-annealing-energies.PNG)


*Time required:*

![sa-time](graphs/simulated-annealing-time-required.PNG)
