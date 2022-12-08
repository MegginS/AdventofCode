class Node:

    def __init__(self, name, parent, size=0, children=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = children or []

    def __repr__(self):
        return f" <Node= {self.name}, size = {self.size}, children = {self.children}, parent = {self.parent}>"


def create_directory_tree(files):

    info = open(files)
    root = Node("/", parent=None)
    parent = root

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
    
    to_visit = [root]
    overall_size = 0

    while to_visit:
        current = to_visit.pop()
        size = current.size

        if (int(size)) < 100000 and current.children != []:
            overall_size += int(size)
        to_visit.extend(current.children)
        
    print(f'total = {overall_size}')

create_directory_tree("inputs/7input.txt")
