import random as rd

branch = '^'
trunk = '#'
space = ' '
ornament = 'o'
line_output = ''
print('Enter the tree size.')
size = int(input('>'))

for row_num in range(1, size + 1):
    num_spaces = size - row_num
    num_branches = (row_num * 2 - 1)
    line_output = space * num_spaces
    for spot in range(num_branches):
        orn = rd.randint(1, 4)
        if orn == 1:
            line_output += ornament
        else:
            line_output += branch
    print(line_output)

print((space * (size - 1)) + trunk)
print((space * (size - 1)) + trunk)
