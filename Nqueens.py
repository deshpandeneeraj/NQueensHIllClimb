"""
@Author : Neeraj Deshpande
 Date: 2 May 2020
@GitHub ID : deshpandeneeraj
 GitHub Link : https://github.com/deshpandeneeraj/NQueensHIllClimb
"""

import random

def display(board, size):
    for row in board:
        string = "|"
        for i in range(row - 1):
            string += "_|"
        string += "Q|"
        for i in range(size - row):
            string += "_|"
        print(string)

def get_h_cost(board):
    h = 0
    for i in range(len(board)):
    #Check every column we haven't already checked
        for j in range(i + 1,len(board)):
            #Queens are in the same row
            if board[i] == board[j]:
                h += 1
            #Get the difference between the current column
            #and the check column
            offset = j - i
            #To be a diagonal, the check column value has to be
            #equal to the current column value +/- the offset
            if board[i] == board[j] - offset or board[i] == board[j] + offset:
                h += 1

    return h

def no_start(size):
    board = [random.randint(1,size)]
    for i in range(size-1):
        temp = []
        for j in range(1, size+1):
            if j not in board:
                temp.append(board+[j])
        min = size + 1
        for option in temp:
            if get_h_cost(option) < min:
                best = option[-1]
                min = get_h_cost(option)
        board.append(best)
    final, moves = with_start2(board, size)
    return final, moves


def with_start(size):
    board = []
    moves = 0
    for i in range(1,size + 1):
        board.append(int(input(f"Enter Collumn for row {i}: ")))
    print(f"Start State is :")
    display(board, size)
    while not get_h_cost(board) == 0:
        for id, val in enumerate(board):
            temp = []
            for j in range(1, size+1):
                temp = temp + [board.copy()]
            i = 1
            for option in temp:
                option[id] = i
                i+=1
            min = size + 1
            for option in temp:
                if get_h_cost(option) < min:
                    best = option
                    min = get_h_cost(option)
            possible = []
            for option in temp:
                if get_h_cost(option) == min:
                    possible.append(option)
            if (min == 0):
                if len(possible[0]) > 1:
                    board = random.choice(possible)
                else:
                    board = possible
                flag = True
            else:
                if len(possible[0]) > 1:
                    board = random.choice(possible)
                else:
                    board = possible
                flag = False
            print("BOARD:", board)
            moves += 1
    return board, moves

def with_start2(board, size):
    print(f"Start State is :")
    display(board, size)
    moves = 0
    while not get_h_cost(board) == 0:
        for id, val in enumerate(board):
            temp = []
            for j in range(1, size+1):
                temp = temp + [board.copy()]
            i = 1
            for option in temp:
                option[id] = i
                i+=1
            min = size + 1
            for option in temp:
                if get_h_cost(option) < min:
                    best = option
                    min = get_h_cost(option)
            possible = []
            for option in temp:
                if get_h_cost(option) == min:
                    possible.append(option)
            if (min == 0):
                if len(possible[0]) > 1:
                    board = random.choice(possible)
                else:
                    board = possible
            else:
                if len(possible[0]) > 1:
                    board = random.choice(possible)
                else:
                    board = possible
        print("BOARD:", board)
        moves += 1
    return board, moves


if __name__ == "__main__":
    size = int(input("Enter Size of Board : "))
    choice = input("Do you want to specify start state? ")

    if choice.lower().startswith("y"):
        final, moves = with_start(size)
        print(f"Solution:{final}, Reached in {moves} moves ")
    elif choice.lower().startswith("n"):
        final, moves = no_start(size)
        print(f"Solution reached in {moves} moves ")
        print("Final State:")
        display(final, size)
    else:
        print("Wrong Choice")
