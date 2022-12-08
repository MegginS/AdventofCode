import numpy


def create_tree_farm(file):

    tree_farm = []

    data = open(file)

    for line in data:
        info = [*line.rstrip()]
        tree_farm.append(info)

    return tree_farm

tree_farm = create_tree_farm("inputs/8input.txt")


def check_from_left(matrix, turns = 0, visible_trees = 0):

    first_row = True

    for row in matrix:
        tallest_left_tree = 0
        for i, tree in enumerate(row):
            tree = int(tree)
            if tree == 0 and first_row:
                    visible_trees += 1
            elif tree < 0:
                value_check = -tree
                if tallest_left_tree < value_check:
                    tallest_left_tree = value_check
            elif tallest_left_tree < tree:
                tallest_left_tree = tree
                row[i] = -tree
                visible_trees += 1
        first_row = False
    if turns < 3:
        matrix = numpy.rot90(matrix)
        turns += 1
        check_from_left(matrix, turns, visible_trees= visible_trees)
    else:
        print(f'There are {visible_trees} visible trees')

check_from_left(tree_farm, 0)
