def calories_carried_by_top3(elves_calories):
    """finds the number of calories the top 3 elves are carrying"""

    with open(elves_calories) as f:
        calorie_data = f.read().splitlines()

    elves_totals = []
    elf_total = 0

    for calories in calorie_data:
        if calories != "":
            elf_total += int(calories)
        else:
            elves_totals.append(elf_total)
            elf_total = 0
    
    elves_totals.sort()

    elf_one = elves_totals.pop()
    elf_two = elves_totals.pop()
    elf_three = elves_totals.pop()

    top3 = elf_one + elf_two + elf_three
    
    print(top3)