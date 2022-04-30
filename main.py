import os


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
        ucs(puzzle)
    elif algo == '2':
        a_star_mth(puzzle)
    elif algo == '3':
        a_star_edh(puzzle)
    else:
        print('Invalid input. Using A* with the Euclidean Distance Heuristic')
        a_star_edh(puzzle)


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


def ucs(problem):
    # might change these functions
    goal_state = ([1, 2, 3], [4, 5, 6], [7, 8, 0])


def a_star_mth(problem):
    # might change these functions
    goal_state = ([1, 2, 3], [4, 5, 6], [7, 8, 0])


def a_star_edh(problem):
    # might change these functions
    goal_state = ([1, 2, 3], [4, 5, 6], [7, 8, 0])


if __name__ == '__main__':
    main()
