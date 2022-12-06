with open("inputs/6input.txt") as f:
    info = f.readlines()


def find_unique(quantity):
    """finds unique characters and gets index of last character"""

    i = 0

    while i < len(info[0]):
        unique_chars = set(info[0][i:i+quantity])
        if len(unique_chars) < quantity:
            i+=1
        else:
            return print(i + quantity)

end_unique_4 = find_unique(4)
end_unique_14 = find_unique(14)



# def find_unique_four_recursively(i=0):
#     """finds for string under 1000 characters before max recursion met"""
    
#     unique_chars = set(info[0][i:i+4])
#     if len(unique_chars) < 4:
#         i+=1
#         find_unique_four_recursively(i)
#     else:
#         print(i + 4)

# find_unique_four_recursively(i = 0)

# # RecursionError: maximum recursion depth exceeded while calling a Python object
