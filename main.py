import os
import copy
import queue
import time
import math


def main():
    print('Welcome to ' + os.environ['ROY_SID'] + '\'s 8 puzzle solver')
    print('Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.')
    custom_puzzle = input()
    if custom_puzzle == '1':
        # puzzle should be a tuple of lists - tuple is ordered and immutable, but list is ordered and mutable
        # the rows should be immutable, but we should be allowed to modify the elements within each row
        puzzle = ([1, 2, 0], [4, 5, 3], [7, 8, 6])
    elif custom_puzzle == '2':
        print('Enter your puzzle, use a zero to represent the blank')
        print('Enter the first row, use a space between numbers')
        row_1 = input()
        print('Enter the second row, use a space between numbers')
        row_2 = input()
        print('Enter the third row, use a space between numbers')
        row_3 = input()
        puzzle = (row_1.split(), row_2.split(), row_3.split())
    else:
        print('Invalid input. Using default puzzle.')
        puzzle = ([1, 2, 0], [4, 5, 3], [7, 8, 6])

    print('\nHere is the puzzle:')
    print(puzzle)
    print('\nEnter the number of your choice of algorithm:')
    print('(1) Uniform Cost Search')
    print('(2) A* with the Misplaced Tile Heuristic')
    print('(3) A* with the Euclidean Distance Heuristic')
    algo = input()
    if algo == '1':
        heuristic = ucs(puzzle)
    elif algo == '2':
        heuristic = a_star_mth(puzzle)
    elif algo == '3':
        heuristic = a_star_edh(puzzle)
    else:
        print('Invalid input. Using A* with the Euclidean Distance Heuristic')
        heuristic = a_star_edh(puzzle)

    # print(heuristic)
    search_results = search(puzzle, heuristic)

    if search_results:
        print()


# pseudo code
"""
function graphSearch(problem) returns a solution, or failure
    initialize the frontier using the initial state of the problem
    initialize the explored set to be empty
    loop do
        if the frontier is empty then return failure
        choose a leaf node and remove it from the frontier
        if the node contains a goal state then return the corresponding solution
        add the node to the explored set
        expand the chosen node, adding the resulting nodes to the frontier
            only if not in the frontier or explored set
"""


def search(puzzle, heuristic):
    # pseudocode
    if (problem.puzzle == goal_state):
        # maybe instead of a bool, we return some kind of object containing number of nodes expanded, max number of
        # nodes in the queue, and the depth of the goal state
        return True
    return False


class Problem:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.expanded = False
        self.parent = None
        self.mvup = None
        self.mvdwn = None
        self.mvlft = None
        self.mvrht = None
        self.hn = 0
        self.gn = 0
        self.fn = 0
        self.depth = 0



goal_state = ([1, 2, 3], [4, 5, 6], [7, 8, 0])


def ucs(puzzle):
    return 0


# misplaced tile heuristic, returns number of tiles in a position other than their designated goal state position
def a_star_mth(puzzle):
    misplaced_count = 0
    for row in range(len(puzzle)):
        for col in range(len(puzzle)):
            if puzzle[row][col] != goal_state[row][col] and puzzle[row][col] != 0:
                misplaced_count += 1
    return misplaced_count


# euclidean distance heuristic,
def a_star_edh(puzzle):
    distance = 0
    puzzle_row = -1
    puzzle_col = -1
    goal_state_row = -1
    goal_state_col = -1
    for i in range(1, 9):
        for row in range(len(puzzle)):
            for col in range(len(puzzle)):
                if puzzle[row][col] == i:
                    puzzle_row = row
                    puzzle_col = col
                if goal_state[row][col] == i:
                    goal_state_row = row
                    goal_state_col = col
        row_difference = puzzle_row - goal_state_row
        col_difference = puzzle_col - goal_state_col
        hypotenuse = math.sqrt(pow(row_difference + col_difference, 2))
        distance += hypotenuse
    return distance


if __name__ == '__main__':
    main()
