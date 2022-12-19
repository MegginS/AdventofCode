instructions = open("inputs/10input.txt").read().split()

sprite = 1
cycle = 0
i = 0
grid=[[],[],[],[],[],[]]

for instruction in instructions:
    if cycle in [sprite-1, sprite, sprite +1]:
        grid[i].append("#")
    else:
        grid[i].append(".")

    if instruction != "addx" and instruction != "noop":
        sprite = sprite + int(instruction)
        
    cycle +=1
    if len(grid[i]) % 40 == 0:
        i += 1
        cycle = 0
    
j=0
for line in grid:
    cleaned = "".join(str(e) for e in grid[j])
    j +=1
    print(cleaned)