#####     UTILS.PY     #####

#   - You as a developer are faced with a few options of executing sudoku puzzles to test the program's behavior.
#     In the "Developer's Configuration Settings" section below in this file, there are a few important variables
#     to pay attention to. Therefore, the following mapping between the variables and their implication was made:
#
#
#       VARIABLE:                                   IMPLICATION:

#       'runBacktrackConstraintAlgorithm'   -->     Run Backtracking & Constraint Propagation or Simulated Annealing
#
#       'OPTION'                            -->     Ranges between 1-3:
#                                                       - 1     -->     'SELECTED_PUZZLE'
#                                                       - 2     -->     'EASY_HARD_PUZZLES'
#                                                       - 3     -->     'SELECTED_PUZZLES_LIST'
#
#       'SELECTED_PUZZLE'                   -->     Run the one and only selected puzzle
#
#       'EASY_HARD_PUZZLES'                 -->     Run the selected pair of two puzzles
#
#       'SELECTED_PUZZLES_LIST'             -->     Run all puzzles defined in the list
#
#
#   - IMPORTANT NOTE: Simulated Annealing is only supported by 'OPTION=2', meaning that setting
#                     'runBacktrackConstraintAlgorithm' to false automatically defaults to running the
#                     selected pair of puzzles in 'EASY_HARD_PUZZLES'
#


import puzzleParser
import json


####    DEVELOPER'S CONFIGURATION SETTINGS    ####
#
#   - Configure execution options for the system. All modifiable settings gathered in this file.


runBacktrackConstraintAlgorithm = False # IMPORTANT: Change this variable to 'True' or 'False' to toggle between Backtracking and Simulated Annealing

##  Backtracking Settings Only  ##
OPTION = 3
SELECTED_PUZZLE = "puzzles/extreme3.txt" # Active when OPTION=1
SELECTED_PUZZLES_LIST= [ # Active when OPTION=3
    "puzzles/easy1.txt",
    "puzzles/easy2.txt",
    "puzzles/empty.txt",
    "puzzles/hard1.txt",
    "puzzles/hard2.txt",
    "puzzles/extreme.txt",
    "puzzles/extreme2.txt",
    "puzzles/extreme3.txt",
    "puzzles/extreme4.txt",
    "puzzles/assignment.txt"
    ]


##  Backtracking (OPTION=2) and Simulated Annealing Settings  ##

EASY_HARD_PUZZLES = {"Easy": "puzzles/easy1.txt", "Hard": "puzzles/hard1.txt"} # Active when OPTION=2, or when runBacktrackConstraintAlgorithm=False


# Returns the selected files based on the developer's configuration variables defined in this file
def getParsedPuzzle():
    if OPTION == 2 or runBacktrackConstraintAlgorithm == False:
        return {
            EASY_HARD_PUZZLES["Easy"]: puzzleParser.readSudokuPuzzle(EASY_HARD_PUZZLES["Easy"]),
            EASY_HARD_PUZZLES["Hard"]: puzzleParser.readSudokuPuzzle(EASY_HARD_PUZZLES["Hard"])
        }

    # If developer choose to parse one puzzle, or simulated annuealing (which defaults to 1 puzzle at a time)
    if OPTION == 1:
        return puzzleParser.readSudokuPuzzle(SELECTED_PUZZLE)
    elif OPTION == 3: # Run all specified in list
        outputDictionary = {}
        for (i, puzzleFile) in enumerate(SELECTED_PUZZLES_LIST):
            outputDictionary[puzzleFile] = puzzleParser.readSudokuPuzzle(SELECTED_PUZZLES_LIST[i])
        return outputDictionary
    

# Returns a list of the selected puzzles in the system's execution
def getSelectedPuzzles():
    if OPTION == 2 or runBacktrackConstraintAlgorithm == False:
        return EASY_HARD_PUZZLES
    
    if OPTION == 1:
        return SELECTED_PUZZLE
    
    if OPTION == 3:
        return SELECTED_PUZZLES_LIST
    
    return "Invalid configuration. OPTION must range between 1-3"



def getCartesianProduct(s1, s2):
    return [i + j for i in s1 for j in s2]

def mapCellsToUnits(units, cells):
    return dict((cell, [unit for unit in units if cell in unit]) for cell in cells) # map each cell to its units

def mapCellsToPeers(units, cells):
    return dict((cell, set(sum(units[cell], [])) - {cell}) for cell in cells) # map each cell to its peers



# Writes to a .txt file the data retrieved in the latest execution of 'Backtracking & Propagation' algorithm
# where OPTION=3 was selected, such that all Sudoku puzzles in the defined list was solved
def registerPerformanceAnalysis(backtrackConstraintAnalysisData):
    outputFile = "performances/recursive-data.json"

    with open(outputFile, "w") as outputPerformanceFile:
        print(f"Performances of this execution for each puzzle is stored in '{outputFile}'")
        json.dump(backtrackConstraintAnalysisData, outputPerformanceFile, indent=4)



# Only run when OPTION=1 and backtracking algorithm
# variable: SELECTED_PUZZLE
def registerBacktrackingTimeline(backtrackTimelineData):
    outputFile = "performances/backtrack-timeline.json"
    backtrackTimelineData["puzzle"] = SELECTED_PUZZLE

    with open(outputFile, "w") as outputPerformanceFile:
        json.dump(backtrackTimelineData, outputPerformanceFile, indent=4)


def displayUnsolvedBoardUI(selfObj, puzzleFile, approach, values):

    print("\n\n###########################################\n\n")
    print(f"PUZZLE: '{puzzleFile}'\n\n")
    print(f"UNSOLVED BOARD:\n")

    if approach == "annealing":
        selfObj.display()
    else:
        selfObj.display(values)