import re

stacks = {
    "1" : ["C", "Z", "N", "B", "M", "W", "Q", "V"],
    "2" : ["H", "Z", "R", "W", "C", "B"],
    "3" : ["F", "Q", "R", "J"],
    "4" : ["Z", "S", "W", "H", "F", "N", "M", "T"],
    "5" : ["G", "F", "W", "L", "N", "Q", "P"],
    "6" : ["L", "P", "W"],
    "7" : ["V", "B", "D", "R", "G", "C", "Q", "J"],
    "8" : ["Z", "Q", "N", "B", "W"],
    "9" : ["H", "L", "F", "C", "G", "T", "J"]
}

def rearranging_crates(instructions):

    data = open(instructions)

    for line in data:
        info = line[5:].replace(" ", "").rstrip()
        num_moves, origin, destination  = re.split("from|to", info)
        making_moves(num_moves, origin, destination)


def making_moves(num_moves, origin, destination, i=0):

    removed_item = stacks.get(origin).pop()
    stacks[destination].append(removed_item)
    i+=1
    if i < int(num_moves):
        making_moves(num_moves, origin, destination, i)


def getting_top_crates():

    rearranging_crates("5input.txt")

    top_stacks = ""
    stack = 1
    while stack <= len(stacks):
        top_stacks = top_stacks + stacks.get(str(stack))[-1]
        stack += 1

    print(top_stacks)
