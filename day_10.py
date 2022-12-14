instructions = open("inputs/10input.txt").read().split()

x = i = 1
totals = []
signal_strength =0
cycle = 20

for instruction in instructions:
    if instruction != "addx" and instruction != "noop":
        x += int(instruction)
    i+=1

    if i % cycle == 0:
        totals.append(i*x)
        cycle += 40

for total in totals:
    signal_strength += total

print(signal_strength)
