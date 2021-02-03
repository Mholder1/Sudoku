
def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None

def is_valid(puzzle, guess, row, col):
    #figures out whether the guess at the row/col is a valid guess
    #returns true if it is valid
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #square 3x3 maker
    #have to know where we are in the puzzle
    #find starting index of row, and find starting column of 3x3 matrix
    #for each of the row, iterate
    row_start = (row // 3) * 3 #divide the number but throw away the remainder
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True


def solve_sudoku(puzzle):
#solve sudoku using backtracking
#our puzzle is a list of lists, where each inner list is a row
#return whether a solution exists
#mutates puzzle to be the solution

#step 1: choose somewhere on the puzzle to make a guess

    row, col = find_next_empty(puzzle)

#step 1.1: if theres nowhere left, then we're done because we only allowed valid inputs


    if row is None:
        return True

#step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        #step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True
        

        puzzle[row][col] = -1

        #step 6: if none of numbers work, this puzzle is unsolvable
    return False

    
if __name__ == "__main__":
    example_board = [

    [-1,-1,-1,2,6,-1,7,-1,1],
    [6,8,-1,-1,7,-1,-1,9,-1],
    [1,9,-1,-1,-1,4,5,-1,-1],
    [8,2,-1,1,-1,-1,-1,4,-1],
    [-1,-1,4,6,-1,2,9,-1,-1],
    [-1,5,-1,-1,-1,3,-1,2,8],
    [-1,-1,9,3,-1,-1,-1,7,4],
    [-1,4,-1,-1,5,-1,-1,3,6],
    [7,-1,3,-1,1,8,-1,-1,-1]

]
    print(solve_sudoku(example_board))
    print(example_board)
