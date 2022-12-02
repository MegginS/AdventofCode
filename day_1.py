

def most_calories_carried(elves_calories):
    """finds the number of calories the elf with the most calories is carrying"""


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
    
    max_carried = max(elves_totals)
    print(max_carried)