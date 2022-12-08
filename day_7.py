class Node:
    """Node of a Tree"""
    def __init__(self, name, parent, size=0, children=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = children or []


def create_directory_tree(files):
    """Creates a filesystem tree"""

    info = open(files)
    root = parent = Node("/", parent=None)

    for line in info:
        line = line.rstrip()
        if line[0].startswith("$") and line[2] == "c":
            directory = line[5:]
            if directory == "..":
                node = node.parent
                parent = node.parent
            else:
                for child in parent.children:
                    if child.name == directory:
                        parent = child
        elif line[0].startswith("d"):
            directory = line[4:]
            node = Node(directory, parent=parent)
            parent.children.append(node)
        elif line[0].isdigit():
            size, filename = line.split(" ")
            node = Node(filename, size=size, parent=parent)
            parent.children.append(node)
            parent.size += int(node.size)
            temp = parent
            while temp.parent:
                temp.parent.size += int(node.size)
                temp = temp.parent

    return root


def find_requested_info(files):
    """finds combined space of directories under 100000 & finds 
    smallest directory that if removed, will leave 30000000"""

    root = create_directory_tree(files)

    to_visit = [root]
    overall_size = 0
    delete_for_space = int(root.size)
    space_needed = 30000000 - (70000000 - int(root.size))

    while to_visit:
        current = to_visit.pop()
        size = current.size

        if int(size) < 100000 and current.children != []:
            overall_size += int(size)
        if int(size) > space_needed and int(size) < delete_for_space:
            delete_for_space = size
        to_visit.extend(current.children)
  
    print(f'total = {overall_size}')
    print(f'delete =  {delete_for_space}')


find_requested_info("inputs/7input.txt")
