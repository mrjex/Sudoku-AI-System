# Sudoku AI System

> An Intelligent Sudoku Solver System implementing Backtracking and Simulated Annealing Algorithms

## Table of Contents

- [Sudoku AI System](#sudoku-ai-system)
  - [Table of Contents](#table-of-contents)
  - [System Architecture](#system-architecture)
  - [Getting Started](#getting-started)
  - [Configuration Guide](#configuration-guide)
    - [Demo Configurations](#demo-configurations)
      - [Backtracking \& Constraint Propagation](#backtracking--constraint-propagation)
      - [Simulated Annealing](#simulated-annealing)
  - [Adding Custom Puzzles](#adding-custom-puzzles)
    - [Supported Formats](#supported-formats)
    - [Format Rules](#format-rules)
  - [Performance Analysis](#performance-analysis)
    - [Backtracking Results](#backtracking-results)
    - [Simulated Annealing Analysis](#simulated-annealing-analysis)
  - [Technical Documentation](#technical-documentation)
    - [Puzzle Processing Pipeline](#puzzle-processing-pipeline)


## System Architecture

![system-data-flow](readme-material/system-data-flow.PNG)


## Getting Started

1. Configure settings in `utils.py`
2. Run `main.py`


## Configuration Guide

The system offers flexible configuration through `utils.py`:

| Parameter | Type | Description | Options |
|-----------|------|-------------|----------|
| `runBacktrackConstraintAlgorithm` | Boolean | Algorithm selection | `True`: Backtracking, `False`: Simulated Annealing |
| `OPTION` | Integer | Execution mode | `1`: Single puzzle, `2`: Two puzzles, `3`: Multiple puzzles |
| `SELECTED_PUZZLE` | String | Single puzzle path | Active when `OPTION=1` |
| `EASY_HARD_PUZZLES` | Dict | Two puzzle paths | Active when `OPTION=2` |
| `SELECTED_PUZZLES_LIST` | List | Multiple puzzle paths | Active when `OPTION=3` |

### Demo Configurations

#### Backtracking & Constraint Propagation

**Single Puzzle Mode:**
![backtrack-option-1](readme-material/backtrack-option1.mp4)
*Solving a single puzzle using backtracking*

**Dual Puzzle Mode:**
![backtrack-option-2](readme-material/backtrack-option2.mp4)
*Comparative analysis of two puzzles*

**Multi-Puzzle Mode:**
![backtrack-option-3](readme-material/backtrack-option3.mp4)
*Batch processing of multiple puzzles*

#### Simulated Annealing

**Optimization Process:**
![simulated-annealing](readme-material/simulated-annealing.mp4)
*Temperature-based optimization in action*

## Adding Custom Puzzles

### Supported Formats

```python
# Format 1: Simple Grid
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
...

# Format 2: Subgrid Separation
5 3 . |. 7 . |. . .
6 . . |1 9 5 |. . .
...
```

### Format Rules
- Empty cells: Use `.` or `0`
- Cell separation: Single space
- Subgrid boundaries: `|` (optional)
- Grid size: 9x9


## Performance Analysis

### Backtracking Results
![backtracking-output](graphs/run-all-puzzles-backtracking.PNG)
*Comparative performance across puzzle complexity*

### Simulated Annealing Analysis
![sa-energies](graphs/simulated-annealing-energies.PNG)
*Energy optimization over iterations*

![sa-time](graphs/simulated-annealing-time-required.PNG)
*Time performance analysis*

## Technical Documentation

### Puzzle Processing Pipeline

1. **Input Processing**
   ```python
   # Raw Input
   5 3 . |. 7 . |. . .
   ...
   
   # Subgrid Division
   53..7....6..195....98....6.
   ...
   
   # Final Format
   53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79
   ```

2. **Solution Generation**
3. **Performance Metrics Collection**
4. **Visualization Generation**
