import re

def find_overlapping_sections(sections):

    data = open(sections)

    fully_contained_pairs = 0

    for line in data:
        info = line.rstrip()
        elf_a_start, elf_a_finish, elf_b_start, elf_b_finish = re.split("-|,", info)
        
        if int(elf_a_start) <= int(elf_b_start) and int(elf_a_finish) >= int(elf_b_finish):
            fully_contained_pairs += 1
        elif int(elf_a_start) >= int(elf_b_start) and int(elf_a_finish) <= int(elf_b_finish):
            fully_contained_pairs += 1 

    print(fully_contained_pairs)

find_overlapping_sections("4input.txt")