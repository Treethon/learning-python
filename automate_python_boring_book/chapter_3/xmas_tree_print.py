import random

branch = '^'
trunk = '#'
space = ' '
ornament = 'o'
print('Enter the tree size.')
size = int(input('>'))

for row_num in range(1, size + 1):
    num_spaces = size - row_num
    num_branches = (row_num * 2 - 1)
    print((num_spaces * space) + (num_branches * branch))

print((space * (size - 1)) + trunk)
print((space * (size - 1)) + trunk)