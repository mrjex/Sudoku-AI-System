from itertools import product
import sudokuPropagation as sp
import sudokuAnnealing as sa
import visualization
import utils

# Simulated Annealing: Actual child function
def getAnnealingRes(parsedBoard, puzzleFile):
    sudoku_sa = sa.SudokuAnnealing(parsedBoard, puzzleFile)
    energies = sudoku_sa.solve()

    print(f"SOLVED BOARD:\n")
    sudoku_sa.display()

    run_sa = sudoku_sa.exec_time  # Retrieve the time the algorithm needed to solve the puzzle
    del run_sa[0]

    print("TIME REQUIRED TO SOLVE:", end="")
    print(f" {run_sa[-1]} (seconds)")

    return [energies, run_sa]


# Simulated Annealing: Refactored parent function
def runSudokuAnnealing():
    res = utils.getParsedPuzzle()
    puzzles = []

    for puzzleFile in res:
        puzzles.append(puzzleFile)

    energies_easy, run_sa_easy = getAnnealingRes(res[puzzles[0]], puzzles[0])
    energies_hard, run_sa_hard = getAnnealingRes(res[puzzles[1]], puzzles[1])

    visualization.plotAnnealing(energies_easy, energies_hard, run_sa_easy, run_sa_hard)


# Solve a Sudoku board with backtracking and constraint propagation
def getBacktrackRes(parsedBoard, puzzleFile):
    sudoku_sp = sp.SudokuPropagation(puzzleFile)
    utils.displayUnsolvedBoardUI(sudoku_sp, puzzleFile, "propagation", parsedBoard)
    print('\n')

    # Substitute '.' with the possible values in the domain
    for k, v in parsedBoard.items():
        if v == '.':
            parsedBoard[k] = '123456789'
    
    solved_board = sudoku_sp.recursiveSolve(parsedBoard)

    print(f"SOLVED BOARD:\n")
    sudoku_sp.display(solved_board) # Show solved board
    print('\n')

    run_sp = sudoku_sp.exec_time
    del run_sp[0]
    print("TIME REQUIRED TO SOLVE:", end="")
    print(f" {run_sp[-1]} (seconds)")

    return run_sp, sudoku_sp


# Runs 'N' separate puzzles for the 'Backtracking & Constraint Propagation' approach
# and uses the 'visualization' module to plot their performances on the same chart
def runBackTrackN(n):

    # Developer wants to run only one puzzle with the backtracking algorithm
    if n == 1:
        res = utils.getParsedPuzzle()
        parsedBoard = dict(zip([''.join(cell) for cell in product('ABCDEFGHI', '123456789')], res))

        visualization.initFigure()
        run_sp, backtrackObj = getBacktrackRes(parsedBoard, utils.SELECTED_PUZZLE)

        utils.registerBacktrackingTimeline(backtrackObj.backtracksTimeline)

        visualization.appendFigure(run_sp, utils.SELECTED_PUZZLE)
        visualization.showFigure()
    
    # Developer wants to run 'n' puzzles using the backtracking algorithm
    else:
        backtrackConstraintAnalysisData = {
            "recursiveIterations": {},
            "backtrackings": {}
        }

        res = utils.getParsedPuzzle()
        visualization.initFigure()

        for puzzleFile in res:
            currentBoard = res[puzzleFile]
            parsedBoard = dict(zip([''.join(cell) for cell in product('ABCDEFGHI', '123456789')], currentBoard))

            run_sp, backtrackObj  = getBacktrackRes(parsedBoard, puzzleFile)

            backtrackConstraintAnalysisData["recursiveIterations"][puzzleFile] = backtrackObj.recursiveIterations[0]
            backtrackConstraintAnalysisData["backtrackings"][puzzleFile] = backtrackObj.numBacktracks[0]

            visualization.appendFigure(run_sp, puzzleFile)
        

        if utils.OPTION == 3:
            utils.registerPerformanceAnalysis(backtrackConstraintAnalysisData)
        
        visualization.showFigure()



if __name__ == '__main__':

    try:
        if utils.runBacktrackConstraintAlgorithm:
            if utils.OPTION <= 3 and utils.OPTION >= 1:
                runBackTrackN(utils.OPTION)
            else:
                print("Only options in the range 1-3 is supported. Modify the configuration variables in 'utils.py'")
        
        else:
            runSudokuAnnealing()
    except:
        selectedPuzzles = utils.getSelectedPuzzles()
        print(f"The provided Sudoku board in at least one of '{selectedPuzzles}' is either unsolvable or has invalid formatting. Keep in mind that all direct", end="")
        print("and indirect constraints of the input board must be satisfied, and check the formatting of the other .txt files in '/puzzles' directory.")