class Node:
    """Node of a Tree"""
    def __init__(self, height, left = None, up = None, down = None, right= None):
        self.height = height
        self.left = left
        self.up = up
        self.down = down
        self.right = right


with open("inputs/8input.txt") as f:
    trees = list(f.read())
    root = Node(trees[0][0])


def layout_tree_farm(row_above = False, left = root):

    new_row = False
    first_column_up = root

    for tree in trees[1:]:
        if new_row:
            up = first_column_up
            current = Node(tree, up = up)
            current.up.down = current
            left = current
            first_column_up = current
            row_above = True
            new_row = False
        elif tree == "\n":
            new_row = True
        elif row_above:
            current = Node(tree, left)
            current.up = current.left.up.right
            current.left.right = current
            current.left.up.right.down = current
            left = current
            new_row = False
        else:
            current = Node(tree, left)
            current.left.right = current
            left = current
            new_row = False

    return root


def calculating_points(current):

    directions =["left", "right", "up", "down"]
    points =[0,0,0,0]
    i = 0

    while i < 4:
        checker = getattr(current, directions[i])
        while checker is not None:
            points[i] += 1
            if current.height > checker.height:
                checker = getattr(checker, directions[i])
            else:
                break
        i+=1

    return points[0] * points[1] * points[2]* points[3]


def seeing_most_trees():

    root = layout_tree_farm()
    base = current = root
    most_tree_views = 0

    while current:
        if not None in (current.left, current.right, current.up, current.down):
            tree_views = calculating_points(current= current)
            if tree_views > most_tree_views:
                most_tree_views = tree_views
        if not current.right:
            current = base.down
            base = current
        else:
            current = current.right
        if current.right is None and current.down is None:
            break

    print(most_tree_views)
    
seeing_most_trees()
