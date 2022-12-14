# area = [["S"],["a"],["b"],["q"],["p"],["o"],["n"],["m"],
# ["a"],["b"],["c"],["r"],["y"],["x"],["x"],["l"],
# ["a"],["c"],["c"],["s"],["z"],["E"],["x"],["k"],
# ["a"],["c"],["c"],["t"],["u"],["v"],["w"],["j"],
# ["a"],["b"],["d"],["e"],["f"],["g"],["h"],["i"]]

area = [
["S", "a", "b", "q", "p", "o", "n", "m"],
["a", "b", "c", "r", "y", "x", "x", "l"],
["a", "c", "c", "s", "z", "E", "x", "k"],
["a", "c", "c", "t", "u", "v", "w", "j"],
["a", "b", "d", "e", "f", "g", "h", "i"]]

quickest_route = None
route_sequence = []
next_char = "E"

for i, row in enumerate(area):
    if "E" in row:
        column = row.index('E')
        start = area[i][column]
        next_char = "z"
        N, S, E, W = area[i-1][column], area[i+1][column], area[i][column+1], area[i][column-1]
        if next_char == N or next_char == S or next_char == E or next_char == W:
            route_sequence.append(N)
            
            
            print("yes")
print(f'north = {N}, south = {S}, east = {E},  west = {W}')
