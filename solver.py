board = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

def print_board(bo):
    for row in range(len(bo)):
        if row % 3 == 0 and row != 0:
            print("------------------------")
    
        for col in range(len(bo[0])):
            if col % 3 == 0 and col != 0:
                print (" | ", end = "")

            if col == 8:
                print(bo[row][col])
            else:
                print(str(bo[row][col]) + " ", end = "")

print_board(board)