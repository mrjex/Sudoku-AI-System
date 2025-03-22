#####     PUZZLEPARSER.PY     #####
#
#   - Responsible for parsing a given Sudoku puzzle into a format comprehensible for this system


# Takes a .txt file containing a Sudoku puzzle as input and returns the parsed version of it
def readSudokuPuzzle(puzzleFile):
    with open(f'{puzzleFile}', 'r') as file:
        rows = []

        # Read each line in the file
        for line in file:

            # Improve the ease for the developer of testing different puzzles online: Account for "0" and "." as the empty symbols
            line = line.replace("0", ".")

            if line[0] == "-":
                continue

            line = line.strip()
            myLine = line.replace("|", "")
            myLine = myLine.replace(" ", "")

            rows.append(myLine)

        return "".join(rows)