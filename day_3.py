import itertools

def rucksack_mishaps(rucksacks):
    """calculated the sum of priorities of mishaps"""

    total = 0

    alphabet = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    data = open(rucksacks)

    mishapped_characters = []

    for line in data:
        line = line.rstrip()
        comp_one, comp_two = set(line[:int(len(line)/2)]), set(line[int(len(line)/2):])
        common_characters = list(comp_one.intersection(comp_two))
        mishapped_characters.append(common_characters)

    flat_mishapped_characters = list(itertools.chain(*mishapped_characters))

    for char in flat_mishapped_characters:
        total += alphabet.index(char)
    print(total)

