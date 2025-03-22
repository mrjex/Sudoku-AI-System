import time
import utils

class SudokuPropagation:

    # Initialization of a 'Backtracking & Constraint Propagation' object
    # For each object, attach board-data in the form of attributes
    def __init__(self, puzzleFile):

        # Cell (variable) domains and positions
        self._COLS = '123456789'
        self._ROWS = 'ABCDEFGHI'
        self._CELLS = utils.getCartesianProduct(self._ROWS, self._COLS)

        self.recursiveIterations = [0]      # Store as list to retain contained value
        self.numBacktracks = [0]            # Store as list to retain contained value
        self.backtracksTimeline = {}        # Initialize dictionary and map recusriveIterations and numBacktracks

        # Cell units or value holders
        col_u = [utils.getCartesianProduct(self._ROWS, col) for col in self._COLS] # Units of columns
        row_u = [utils.getCartesianProduct(row, self._COLS) for row in self._ROWS] # Units of rows
        cell_u = [utils.getCartesianProduct(row, col) for row in ('ABC', 'DEF', 'GHI') for col in ('123', '456', '789')] # General cell units

        self.exec_time = [0.]  # Initialize timer
        self._units = row_u + col_u + cell_u
        units = utils.mapCellsToUnits(self._units, self._CELLS)
        self._peers = utils.mapCellsToPeers(units, self._CELLS)

    
    # The recursive depth-first-search-based exploration of the board
    def recursiveSolve(self, board):
        board = self._run_epoch(board) # For each recursive call, run the constrain propagation to maximize efficiency

        # Return 'False' if board can't be solved
        if board is False:
            self.numBacktracks[0] += 1
            self.backtracksTimeline[self.recursiveIterations[0]] = self.numBacktracks[0]
            return False
        
        # Return sucessful base case if all cells only have one value
        if all(len(v) == 1 for v in board.values()):
            return board
        
        # Recursively access cells with the least values and assign new values before trying to solve the board
        _, k = min((len(v), k) for k, v in board.items() if len(v) > 1)
        for num in board[k]:
            self.recursiveIterations[0] += 1
            new_board = board.copy()
            new_board[k] = num
            new_board = self.recursiveSolve(new_board)

            # Return sucessful case if board is solved
            if new_board:
                return new_board
            
    # Selectively remove the values of solved cells from their peers to make the backtracking algorithm more efficient
    def _constraint_propagation(self, board):  
        for k, v in board.items():
            if len(v) != 1:
                peers_k = self._peers[k]
                peer_v = set(board[peer] for peer in peers_k if len(board[peer]) == 1)
                board[k] = ''.join(set(board[k]) - peer_v)
        return board

    # Assign value to variable (cell)
    def _set_value(self, board):
        for unit in self._units:
            for num in self._COLS:
                cells_num = [cell for cell in unit if num in board[cell]]
                if len(cells_num) == 1:
                    board[cells_num[0]] = num
        return board

    # Run constraint propagation and 'only choice' strategy to further improve constraint propagation
    def _run_epoch(self, board):
        changed = True
        while changed:
            before_count = sum(len(v) == 1 for v in board.values()) # Retrieve the current number of cells in the partial solution

            start_time = time.perf_counter()
            board = self._constraint_propagation(board)
            board = self._set_value(board)
            self.exec_time.append((time.perf_counter() + self.exec_time[-1] - start_time))

            after_count = sum(len(v) == 1 for v in board.values())
            changed = before_count != after_count  # Check if the partial solution persists

            # Return 'False' if at least one cell has no value
            if any(len(v) == 0 for v in board.values()):
                return False
        
        return board # Return the board if the case is successful
    
    # Print the board visually on the developer's terminal output
    def display(self, values):
        width = max(len(values[s]) for s in self._CELLS) + 1
        line = '+'.join(['-' * (width * 3)] * 3)

        for r in self._ROWS:
            print(''.join(values[r + c].center(width) + ('|' if c in '36' else '') for c in self._COLS))
            if r in 'CF':
                print(line)
        return