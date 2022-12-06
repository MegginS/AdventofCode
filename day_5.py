import re


def create_stacks(crates):

    with open(crates) as f:
        info = f.read().splitlines()

    stacks = {}

    for row in info:
        i = 1
        j = 1
        if row[i].isdigit():
            return stacks

        total_crates = (len(info[0]) + 1)/4

        while i <= total_crates:
            stacks[i] = stacks.get(i, [])
            if row[j] != " ":
                stacks[i][0:0] = row[j]
            i += 1
            j += 4

elf_stacks = create_stacks("5input.txt")


def rearranging_crates(instructions):

    data = open(instructions)

    for line in data:
        if line.startswith("move"):
            info = line[5:].replace(" ", "").rstrip()
            num_moves, origin, destination  = re.split("from|to", info)
            making_moves(num_moves, origin, destination)


def making_moves(num_moves, origin, destination, i=0):

    removed_item = elf_stacks.get(int(origin)).pop()
    elf_stacks[int(destination)].append(removed_item)
    i+=1
    if i < int(num_moves):
        making_moves(num_moves, origin, destination, i)


def getting_top_crates():

    rearranging_crates("5input.txt")

    top_stacks = ""
    stack = 1
    while stack <= len(elf_stacks):
        top_stacks = top_stacks + elf_stacks.get(stack)[-1]
        stack += 1

    print(top_stacks)

getting_top_crates()
