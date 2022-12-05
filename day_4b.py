import re

def find_any_overlap(sections):

    data = open(sections)

    overlaps = 0

    for line in data:
        info = line.rstrip()
        elf_a_start, elf_a_finish, elf_b_start, elf_b_finish = re.split("-|,", info)
        
        if int(elf_a_start) >= int(elf_b_start) and int(elf_a_start) <= int(elf_b_finish):
            overlaps += 1
        elif int(elf_b_start) >= int(elf_a_start) and int(elf_b_start) <= int(elf_a_finish):
            overlaps += 1 

    print(overlaps)

find_any_overlap("4input.txt")