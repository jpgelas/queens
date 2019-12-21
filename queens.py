#!/usr/bin/env python3

import os
import time

CHESSBOARD_SIZE = 22
WITH_ANIMATION = False
DELAY_SECONDS = 0.200
chessboard = []

def initChessboard(size):
    return [[0] * size for i in range(size)]

def clearScreen():
    _=os.system('clear')

def displayChessboard(chessboard):
    print("-" * 20)
    print("| Chessboard {0}x{0}   |".format(CHESSBOARD_SIZE))
    print("-" * 20)
    for row in chessboard:
        print(*row)

def setQueen(i, j, chessboard, value=1):
    chessboard[i][j] = value

def removeQueen(i, j, chessboard):
    setQueen(i, j, chessboard, 0)

# must be re written to check only upper cells
def isColumnAvailable(j, chessboard):       
    column = [row[j] for row in chessboard]
    return all(elem == 0 for elem in column)

def isUpperLeftAndRightDiagonalsAvailable(row, col, chessboard):
    # Test upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if chessboard[i][j] != 0:
            return False
    # Test upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, CHESSBOARD_SIZE, 1)): 
        if chessboard[i][j] != 0:
            return False
    return True

def isSafe(i, j, chessboard):
    return isColumnAvailable(j,chessboard) and isUpperLeftAndRightDiagonalsAvailable(i,j,chessboard)




# # # # # # # #
# S O L V E R #
# # # # # # # #
def solver(row, chessboard): 
    # base case: If all queens are placed 
    # then return true 
    if row >= CHESSBOARD_SIZE: 
        return True
  
    # Consider this row and try placing 
    # this queen in all columns one by one 
    for j in range(CHESSBOARD_SIZE): 
  
        if isSafe( row, j, chessboard): 
            # Place this queen in board[row][j] 
            setQueen(row,j,chessboard)
            if WITH_ANIMATION:
                clearScreen()
                displayChessboard(chessboard)
                time.sleep(DELAY_SECONDS)

            # recur to place rest of the queens 
            if solver(row + 1, chessboard) == True: 
                return True
  
            # If placing queen in board[i][col 
            # doesn't lead to a solution, then 
            # queen from board[i][col] 
            removeQueen(row,j, chessboard)
            if WITH_ANIMATION:
                clearScreen()
                displayChessboard(chessboard)
                time.sleep(DELAY_SECONDS)
  
    # if the queen can not be placed in any columns in 
    # this row row  then return false 
    return False



def main():
    chessboard = initChessboard(CHESSBOARD_SIZE)
    
    print("Processing Chessboard {0}x{0}".format(CHESSBOARD_SIZE))
    start_time = time.time() 
    if solver(0, chessboard) == False: 
        print("Solution does not exist")
        return False
    interval = time.time() - start_time  

    if not WITH_ANIMATION:
        displayChessboard(chessboard)
    print('Total time in seconds:', interval)

    
    
    return True


main()

# https://kbroman.org/github_tutorial/pages/init.html
# https://www.snakify.org/fr/lessons/two_dimensional_lists_arrays/
# https://www.geeksforgeeks.org/python-program-for-n-queen-problem-backtracking-3/

# a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# # useless functions
# def isCellAvailable(i,j,chessboard):
#     return True if chessboard[i][j] == 0 else False
# def isRowAvailable(i, chessboard):
#     return all(elem == 0 for elem in chessboard[i])
