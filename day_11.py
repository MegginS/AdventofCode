import math

def starting_items():
    monkeys = []
    with open("inputs/12input.txt") as f:
        info = f.read().splitlines()
        for line in info:
            line = line.strip().rstrip(":") 
            if line.startswith("M"):
                monkey = []
            elif line.startswith("S"):
                stolen_items = line[16:].split(",")
                for stolen_item in stolen_items:
                    monkey.append(stolen_item)
                monkeys.append(monkey)
    return monkeys

monkeys = starting_items()
activity = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}

def moving_items(monkeys, turns):

    with open("inputs/12input.txt") as f:
        info = f.read().splitlines()
        item_moving = []

        for line in info:
            line = line.strip().rstrip(":")

            if line.startswith("M"):
                i = int(line[7:])
                current_monkey = monkeys[i]

            if line.startswith("O"):
                for j, holding_item in enumerate(current_monkey):
                    operation = line[21:].split(" ")
                    if operation[1] == "old":
                        operation[1] = holding_item
                    if operation[0] == "*":
                        holding_item = math.floor((int(holding_item) * int(operation[1])) /3)
                        monkeys[i][j] = holding_item
                    if operation[0] == "+":
                        holding_item = math.floor((int(holding_item) + int(operation[1])) /3)
                        monkeys[i][j] = holding_item

            if line.startswith("T"):
                test = line[19:]

            if line.startswith("I"):
                if len(current_monkey) > 0:
                    activity[i] += len(current_monkey)
                while len(current_monkey) > 0:
                    if current_monkey[-1] % int(test) == 0:
                        item_moving.append([current_monkey.pop(), True])
                    else:
                        item_moving.append([current_monkey.pop(), False])

            if line.startswith("If t"):
                k = len(item_moving) - 1
                while k >=0:
                    direction = int(line[25:])
                    if item_moving[k][1] is True:
                        monkeys[direction].append(item_moving[k][0])
                        item_moving.pop(k)
                    k -=1

            if line.startswith("If f"):
                k = len(item_moving)  - 1
                while k >=0:
                    direction = int(line[26:])
                    if item_moving[k][1] is False:
                        monkeys[direction].append(item_moving[k][0])
                        item_moving.pop(k)
                    k -=1

    if turns < 20:
        moving_items(monkeys, turns= turns + 1)  
    else:
        print(activity)     

moving_items(monkeys, 1)
