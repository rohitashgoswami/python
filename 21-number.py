def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lose1():
    print("\n\nYou Lose")
    print("Better luck next time")
    exit(0)

def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
        i += 1
    return True

def start1():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first chance")
        print("Enter 'S' to take the second chance")
        chance = input("> ").upper()

        if chance == "F":
            while True:
                if last == 20:
                    lose1()
                else:
                    print("\nYour turn")
                    print("How many numbers do you wish to enter? (1 or 2)")
                    inp = int(input("> "))

                    if inp == 1 or inp == 2:
                        comp = 4 - inp
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        lose1()

                    print("Now enter the values")
                    for _ in range(inp):
                        a = int(input("> "))
                        xyz.append(a)

                    last = xyz[-1]

                    if check(xyz):
                        if last == 21:
                            print("\n\nCongratulations")
                            print("You won!")
                            exit(0)
                        else:
                            print("Computer's turn:")
                            for j in range(1, comp + 1):
                                xyz.append(last + j)

                            print("Order of inputs after computer's turn is: ")
                            print(xyz)
                            last = xyz[-1]
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose1()

        else:
            print("Wrong choice. Choose 'F' or 'S'.")

game = True
while game:
    print("Player 2 is the computer.")
    print("Do you want to play the 21-number game? (Yes / No)")
    ans = input("> ").capitalize()

    if ans == "Yes":
        start1()
    else:
        print("Do you want to quit the game? (Yes / No)")
        nex = input("> ").capitalize()

        if nex == "Yes":
            print("You are quitting the game...")
            exit(0)
        elif nex == "No":
            print("Continuing...")
        else:
            print("Wrong choice.")
