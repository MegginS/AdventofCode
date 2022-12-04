import itertools

def find_elf_badges(rucksacks):
    """finds badge- common item in rucksack"""

    total = 0

    alphabet = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    with open(rucksacks) as f:
        elf_sacks = f.read().splitlines()

    elf_badges = []

    i = 0

    while i+2 < len(elf_sacks):
        elf_a = set(elf_sacks[i])
        elf_b = set(elf_sacks[i + 1])
        elf_c = set(elf_sacks[i + 2])

        common_characters = list(elf_a.intersection(elf_b, elf_c))
        elf_badges.append(common_characters)
        i+=3

    flattened_elf_badges = list(itertools.chain(*elf_badges))
    for char in flattened_elf_badges:
        total += alphabet.index(char)

    print(total)