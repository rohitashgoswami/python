# logic.py to be 
# imported in the 2048.py file

import random

# function to initialize game / grid at the start
def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)

    print("Commands are as follows:")
    print("'W' or 'w': Move Up")
    print("'S' or 's': Move Down")
    print("'A' or 'a': Move Left")
    print("'D' or 'd': Move Right")

    add_new_2(mat)
    return mat

# function to add a new 2 in grid at any random empty cell
def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while(mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2

# function to get the current state of game
def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 2048):
                return 'WON'

    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 0):
                return 'GAME NOT OVER'

    for i in range(3):
        for j in range(3):
            if(mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]):
                return 'GAME NOT OVER'

    for j in range(3):
        if(mat[3][j] == mat[3][j + 1]):
            return 'GAME NOT OVER'

    for i in range(3):
        if(mat[i][3] == mat[i + 1][3]):
            return 'GAME NOT OVER'

    return 'LOST'

# function to compress the grid after every step
def compress(mat):
    changed = False
    new_mat = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if(mat[i][j] != 0):
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed

# function to merge the cells in matrix after compressing
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if(mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                changed = True
    return mat, changed

# function to reverse the matrix
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append(mat[i][::-1])
    return new_mat

# function to get the transpose of matrix
def transpose(mat):
    new_mat = [[mat[j][i] for j in range(4)] for i in range(4)]
    return new_mat

# function to update the matrix if we move / swipe left
def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    return new_grid, changed

# function to update the matrix if we move / swipe right
def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed

# function to update the matrix if we move / swipe up
def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

# function to update the matrix if we move / swipe down
def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed
