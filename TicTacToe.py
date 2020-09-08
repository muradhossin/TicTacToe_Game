import random

board_place = {"1": " ", "2": " ", "3": " ",
               "4": " ", "5": " ", "6": " ",
               "7": " ", "8": " ", "9": " "}

def desgin_board(board):
    print(board["1"] + " | " + board["2"] + " | " + board["3"])
    print("---------")
    print(board["4"] + " | " + board["5"] + " | " + board["6"])
    print("---------")
    print(board["7"] + " | " + board["8"] + " | " + board["9"])


def valueChoise():
    while True:

        intputVal = input("Select X or O: ")

        if intputVal.upper() == "X":
            return intputVal.upper()
            break
        if intputVal.upper() == "O":
            return intputVal.upper()
            break
        else:
            print("Incorrect Selected")
            continue


def decisionMaking():

    if (board_place["1"] == "X") and (board_place["2"] == "X") and (board_place["3"] == "X"):
        print("1,2,3 numbers are matched.")
        return "x"

    if (board_place["1"] == "O") and (board_place["2"] == "O") and (board_place["3"] == "O"):
        print("1,2,3 numbers are matched.")
        return "o"

    if (board_place["4"] == "X") and (board_place["5"] == "X") and (board_place["6"] == "X"):
        print("4,5,6 numbers are matched.")
        return "x"

    if (board_place["4"] == "O") and (board_place["5"] == "O") and (board_place["6"] == "O"):
        print("4,5,6 numbers are matched.")
        return "o"

    if (board_place["7"] == "X") and (board_place["8"] == "X") and (board_place["9"] == "X"):
        print("7,8,9 numbers are matched.")
        return "x"

    if (board_place["7"] == "O") and (board_place["8"] == "O") and (board_place["9"] == "O"):
        print("7,8,9 numbers are matched.")
        return "o"

    if (board_place["1"] == "X") and (board_place["4"] == "X") and (board_place["7"] == "X"):
        print("1,4,7 numbers are matched.")
        return "x"

    if (board_place["1"] == "O") and (board_place["4"] == "O") and (board_place["7"] == "O"):
        print("1,4,7 numbers are matched.")
        return "o"

    if (board_place["2"] == "X") and (board_place["5"] == "X") and (board_place["8"] == "X"):
        print("2,5,8 numbers are matched.")
        return "x"

    if (board_place["2"] == "O") and (board_place["5"] == "O") and (board_place["8"] == "O"):
        print("2,5,8 numbers are matched.")
        return "o"

    if (board_place["3"] == "X") and (board_place["6"] == "X") and (board_place["9"] == "X"):
        print("3,6,9 numbers are matched.")
        return "x"

    if (board_place["3"] == "O") and (board_place["6"] == "O") and (board_place["9"] == "O"):
        print("3,6,9 numbers are matched.")
        return "o"

    if (board_place["1"] == "X") and (board_place["5"] == "X") and (board_place["9"] == "X"):
        print("1,5,9 numbers are matched.")
        return "x"

    if (board_place["1"] == "O") and (board_place["5"] == "O") and (board_place["9"] == "O"):
        print("1,5,9 numbers are matched.")
        return "o"

    if (board_place["3"] == "X") and (board_place["5"] == "X") and (board_place["7"] == "X"):
        print("3,5,7 numbers are matched.")
        return "x"

    if (board_place["3"] == "O") and (board_place["5"] == "O") and (board_place["7"] == "O"):
        print("3,5,7 numbers are matched.")
        return "o"



def ComputerFast():
    val = ["X", "O"]
    value = random.choice(val)
    count = 0

    trackVal = value
    arr2 = []
    arr1 = []

    for i in range(5):
        print("AI has selected symbol "+ value + ". And selected a board number.")

        for i in range(30):

            valx = str(random.randint(1, 9))
            if valx in arr1:
                continue

            arr1.append(valx)

            if valx in arr2:
                continue

            if valx not in arr2:
                board_place[valx] = value
                count += 1
                break


        desgin_board(board_place)
        res = decisionMaking()

        if trackVal == "X":
            if res == "x":
                print("You Lose!")
                break
        if trackVal == "O":
            if res == "o":
                print("You Lose")
                break

        if count == 9:
            break
        if value == "X":
            trackVal1 = "O"
            value = "O"
        else:
            trackVal1 = "X"
            value = "X"


        print("Your symbol is " + value + ". Which board number wants to select?")

        for i in range(30):
            boardNum = input()
            x = int(boardNum)
            if 1 <= x <= 9:
                if boardNum in arr2:
                    print("Wrong board number selected. Try again...")
                    continue

                arr2.append(boardNum)

                if boardNum in arr1:
                    print("Wrong board number selected. Try again...")
                    continue
                else:
                    board_place[boardNum] = value
                    count += 1
                    break

            else:
                print("Wrong board number selected. Try again...")
                continue


        desgin_board(board_place)
        res = decisionMaking()

        if trackVal1 == "X":
            if res == "x":
                print("You Win!")
                break
        if trackVal1 == "O":
            if res == "o":
                print("You Win!")
                break

        if value == "X":
            value = "O"
        else:
            value = "X"

        if count == 9:
            break

    if res != "x" and res != "o":
        print("Oops! Match Draw.")


def HumanVsComputer():
    print("Who will play first? 1.You or 2.AI")

    inpN = int(input("Enter 1 or 2: "))
    if 1 > n or n > 2:
        print("Incorrect Selected")
        HumanVsComputer()

    if inpN == 2:
        ComputerFast()
    if inpN == 1:
        value = valueChoise()
        trackVal = value
        count = 0
        arr2 = []
        arr1 = []

        for i in range(5):

            print("Your symbol is " + value + ". Which board number wants to select?")
            for i in range(30):
                boardNum = input()
                x = int(boardNum)
                if 1 <= x <= 9:
                    if boardNum in arr2:
                        print("Wrong board number selected. Try again...")
                        continue

                    arr2.append(boardNum)

                    if boardNum in arr1:
                        print("Wrong board number selected. Try again...")
                        continue
                    else:
                        board_place[boardNum] = value
                        count += 1
                        break

                else:
                    print("Wrong board number selected. Try again...")
                    continue

            for i in range(30):

                valx = str(random.randint(1, 9))
                if valx in arr1:
                    continue

                arr1.append(valx)

                if valx in arr2:
                    continue

                if valx not in arr2:
                    computerMode = valx
                    count += 1
                    break

            comBoardNum = computerMode

            if value == "X":
                trackVal1 = "O"
                board_place[comBoardNum] = "O"

            else:
                trackVal1 = "X"
                board_place[comBoardNum] = "X"

            desgin_board(board_place)

            res = decisionMaking()

            if trackVal == "X":
                if res == "x":
                    print("You Win!")
                    break
            if trackVal == "O":
                if res == "o":
                    print("You Win")
                    break

            if trackVal1 == "X":
                if res == "x":
                    print("You Lose!")
                    break
            if trackVal1 == "O":
                if res == "o":
                    print("You Lose!")
                    break

            if count == 9:
                break

        if res != "x" and res != "o":
            print("Oops! Match Draw.")


def HumanVsHumanMode():

    p1 = input("Enter Player1 Name: ")
    p2 = input("Enter Player2 Name: ")
    print("Who will play first?")

    n = int(input("Enter 1 or 2: "))

    if n == 1:
        player1 = p1
        player2 = p2

    if n == 2:
        player1 = p2
        player2 = p1

    if 1 > n or n > 2:
        print("Incorrect Selected")
        HumanVsHumanMode()


    value = valueChoise()
    trackVal = value
    count = 0
    arr2 = []
    arr1 = []
    for i in range(5):

        print(player1, "has taken symbol " + value + ".", player1, "now It's your time to select a board Number..." )

        for i in range(30):

            boardNum = input()
            x = int(boardNum)

            if 1 <= x <= 9:

                if boardNum in arr2:
                    print("Wrong board number selected. Try again...")
                    continue

                arr2.append(boardNum)

                if boardNum in arr1:
                    print("Wrong board number selected. Try again...")
                    continue
                else:
                    board_place[boardNum] = value
                    count += 1
                    break

            else:
                print("Wrong board number selected. Try again...")
                continue


        desgin_board(board_place)

        res = decisionMaking()

        if trackVal == "X":
            if res == "x":
                print(player1, "Win!")
                break
        if trackVal == "O":
            if res == "o":
                print(player1, "Win!")
                break

        if count == 9:
            break

        if value == "X":
            trackVal1 = "O"
            value = "O"
        else:
            trackVal1 = "X"
            value = "X"

        print(player2, "has taken symbol " + value + ".", player2, "now It's your time to select a board Number...")


        for i in range(30):

            valx = input()
            x = int(valx)

            if 1 <= x <= 9:

                if valx in arr1:
                    print("Wrong board number selected. Try again...")
                    continue

                arr1.append(valx)

                if valx in arr2:
                    print("Wrong board number selected. Try again...")
                    continue

                if valx not in arr2:
                    board_place[valx] = value
                    count += 1
                    break

            else:
                print("Wrong board number selected. Try again...")
                continue


        desgin_board(board_place)

        res = decisionMaking()

        if trackVal1 == "X":
            if res == "x":
                print(player2, "Win!")
                break
        if trackVal1 == "O":
            if res == "o":
                print(player2, "Win!")
                break

        if value == "X":
            value = "O"
        else:
            value = "X"

        if count == 9:
            break


    if res != "x" and res != "o":
        print("Oops! Match Draw.")



print("Welcome to TicTacToe Game.")
print("-------MadeBy Md. Murad Hossin")
print("")
print("Here is Board Number")
boardSample = {"1": "1", "2": "2", "3": "3",
               "4": "4", "5": "5", "6": "6",
               "7": "7", "8": "8", "9": "9"}
desgin_board(boardSample)
print("")

while True:

    print("Which game mode you wants to play? 1. Single player mode  2. Multi-player mode")

    n = int(input("Enter 1 or 2: "))

    if 1 > n or n > 2:
        print("You selected incorrect!")
        continue

    if n == 1:
        print("You are playing Single player mode.")
        desgin_board(board_place)
        HumanVsComputer()

    if n == 2:
        print("You are playing Multi-player mode.")
        desgin_board(board_place)
        HumanVsHumanMode()
    print("")
    print("Do you want to continue game?")

    usInp = input("Enter Yes or No: ")

    if usInp.lower() == "yes":
        board_place = {"1": " ", "2": " ", "3": " ",
                       "4": " ", "5": " ", "6": " ",
                       "7": " ", "8": " ", "9": " "}
        desgin_board(board_place)
        continue

    if usInp.lower() == "no":
        print("Game End. Thank you for played.")
        break
