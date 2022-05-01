import os
from copy import deepcopy
from queue import PriorityQueue
import time
import math


def main():
    # TODO: substitute environment variable for SID for final submission
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

    start_time = time.time()
    search(puzzle, heuristic, algo)
    end_time = time.time()
    print('Search took ', end_time - start_time, ' seconds')


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


# graph search inspired by above pseudo code
def search(puzzle, heuristic, algo):
    frontier = PriorityQueue()
    expanded = []
    nodes_expanded = 0
    frontier_size = 0
    max_frontier_size = 0
    node = Problem(puzzle)
    node.hn = heuristic

    # add this puzzle state to expanded to indicate that this puzzle state has been seen
    frontier.put(node)
    frontier_size += 1
    max_frontier_size += 1

    while True:
        if frontier.qsize() == 0:
            print('Search failed: empty frontier')
            return
        node = frontier.get()
        frontier_size -= 1
        if not node.expanded:
            node.expanded = True
            nodes_expanded += 1

        # check for goal state after a node has been removed from the frontier
        if node.puzzle == goal_state:
            print('Goal!!!\n\nTo solve this problem, the search algorithm expanded a total of ' + str(nodes_expanded) +
                  'nodes.\nThe maximum number of nodes in the queue at any one time: ' + str(max_frontier_size) +
                  '.\nThe depth of the goal node was ' + str(node.depth) + '.')

        print('The best state to expand with g(n) = ' + str(node.depth) + ' and h(n) = ' +
              str(node.hn) + ' is...\n' + str(node.puzzle) + '\tExpanding this node...')

        expanded_parent = expand_nodes(node, expanded)
        children = (expanded_parent.move_up, expanded_parent.move_down, expanded_parent.move_left,
                    expanded_parent.move_right)

        for child in children:
            if child is not None:
                child.depth += 1
                if algo == '1':
                    child.hn = ucs(child.puzzle)
                # misplaced tile heuristic
                elif algo == '2':
                    child.hn = a_star_mth(child.puzzle)
                # euclidean distance heuristic
                elif algo == '3':
                    child.hn = a_star_edh(child.puzzle)
                frontier.put(child)
                expanded.append(child.puzzle)
                frontier_size += 1

        if frontier_size > max_frontier_size:
            frontier_size = max_frontier_size


def expand_nodes(node, expanded):
    row_index = -1
    col_index = -1
    # find position of the blank
    for row in range(len(node.puzzle)):
        for col in range(len(node.puzzle)):
            if node.puzzle[row][col] == '0':
                row_index = row
                col_index = col

    if row_index > 0:
        up_child = deepcopy(node.puzzle)
        # swapping the 0 with the puzzle piece directly above it
        swap = up_child[row_index][col_index]
        up_child[row_index][col_index] = up_child[row_index - 1][col_index]
        up_child[row_index - 1][col_index] = swap
        '''
        up_child[row_index][col_index] = up_child[row_index - 1][col_index]
        up_child[row_index - 1][col_index] = 0 # maybe '0'?
        '''
        if up_child not in expanded:
            node.move_up = Problem(up_child)

    if row_index < len(node.puzzle) - 1:
        down_child = deepcopy(node.puzzle)
        # swapping the 0 with the puzzle piece directly above it
        swap = down_child[row_index][col_index]
        down_child[row_index][col_index] = down_child[row_index + 1][col_index]
        down_child[row_index + 1][col_index] = swap
        '''
        up_child[row_index][col_index] = up_child[row_index + 1][col_index]
        up_child[row_index + 1][col_index] = 0 # maybe '0'?
        '''
        if down_child not in expanded:
            node.move_down = Problem(down_child)

    if col_index > 0:
        left_child = deepcopy(node.puzzle)
        # swapping the 0 with the puzzle piece directly above it
        swap = left_child[row_index][col_index]
        left_child[row_index][col_index] = left_child[row_index][col_index - 1]
        left_child[row_index][col_index - 1] = swap
        '''
        left_child[row_index][col_index] = left_child[row_index][col_index - 1]
        left_child[row_index][col_index - 1] = 0 # maybe '0'?
        '''
        if left_child not in expanded:
            node.move_left = Problem(left_child)

    if col_index < len(node.puzzle) - 1:
        right_child = deepcopy(node.puzzle)
        # swapping the 0 with the puzzle piece directly above it
        swap = right_child[row_index][col_index]
        right_child[row_index][col_index] = right_child[row_index][col_index + 1]
        right_child[row_index][col_index + 1] = swap
        '''
        right_child[row_index][col_index] = right_child[row_index][col_index + 1]
        right_child[row_index][col_index + 1] = 0 # maybe '0'?
        '''
        if right_child not in expanded:
            node.move_right = Problem(right_child)

    return node


class Problem:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.expanded = False
        self.parent = None
        self.move_up = None
        self.move_down = None
        self.move_left = None
        self.move_right = None
        self.hn = 0
        self.gn = 0
        self.fn = 0
        self.depth = 0

    def __lt__(self, other):
        return other.hn > self.hn


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
