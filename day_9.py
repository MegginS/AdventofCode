import numpy

with open("inputs/9input.txt") as f:
    data = [line.rstrip().split(" ") for line in f]
    directions = [(line[0], int(line[1])) for line in data]

head = [0,0]
coordinates = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
part_one= set()
part_two = set()

for direction, steps in directions:
        j = 1
        while steps >= j:
            if direction == "R":
                head[0] += 1
            elif direction == "L":
                head[0] -= 1
            elif direction == "U":
                head[1] += 1
            elif direction == "D":
                head[1] -= 1

            coor_before = head
            for i, coordinate in enumerate(coordinates):
                distance = (coor_before[0] - coordinate[0], coor_before[1] - coordinate[1])
                moves = (round((distance[0] / 2) + (distance[0] * .001))), (round((distance[1] / 2) + (distance[1] * .001)))
                
                if distance not in [(0,0),(-1,1),(1,1),(1,-1),(-1,-1),(0,1),(0,-1),(-1,0),(1,0)]:
                    coordinates[i] = tuple(numpy.add(coordinates[i], moves))
                    part_one.add(coordinates[0])
                    part_two.add(coordinates[-1])
                coor_before = coordinates[i]
            j+=1

print(len(part_one))
print(len(part_two))

