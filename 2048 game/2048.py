from logic import *

def print_grid(mat):
    print("\n".join([str(row) for row in mat]))
    print("-" * 20)

def main():
    mat = start_game()

    while True:
        # print the current state of the grid
        print_grid(mat)

        # take user input
        x = input("Press the command (W, A, S, D): ")

        # move up
        if x == 'W' or x == 'w':
            mat, changed = move_up(mat)

        # move down
        elif x == 'S' or x == 's':
            mat, changed = move_down(mat)

        # move left
        elif x == 'A' or x == 'a':
            mat, changed = move_left(mat)

        # move right
        elif x == 'D' or x == 'd':
            mat, changed = move_right(mat)

        else:
            print("Invalid Key Pressed! Try again.")
            continue

        # check if any new tile can be added
        if changed:
            add_new_2(mat)

        # check if the game is won, lost, or still going
        state = get_current_state(mat)
        if state == 'WON':
            print("Congratulations! You won the game!")
            break
        elif state == 'LOST':
            print("Game Over! You lost the game!")
            break

if __name__ == "__main__":
    main()
