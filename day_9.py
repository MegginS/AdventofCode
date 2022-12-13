import numpy

okay = [(0,0),(-1,1),(1,1),(1,-1),(-1,-1),(0,1),(0,-1),(-1,0),(1,0)]

with open("inputs/9input.txt") as f:
    data = [line.rstrip().split(" ") for line in f]
    directions = [(line[0], int(line[1])) for line in data]

h_coordinates, t_coordinates = [[0,0], (0,0)]
all_visits = set()

for direction, steps in directions:
        i = 1
        while steps >= i:
            if direction == "R":
                h_coordinates[0] += 1
            elif direction == "L":
                h_coordinates[0] -= 1
            elif direction == "U":
                h_coordinates[1] += 1
            elif direction == "D":
                h_coordinates[1] -= 1
            
            distance = (h_coordinates[0] - t_coordinates[0], h_coordinates[1] - t_coordinates[1])
            moves = (round((distance[0] / 2) + (distance[0] * .001))), (round((distance[1] / 2) + (distance[1] * .001)))
            
            if distance not in okay:
                t_coordinates = tuple(numpy.add(t_coordinates, moves))

            all_visits.add(t_coordinates)
            i+=1

print(len(all_visits))
