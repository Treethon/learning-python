branch = '^'
trunk = '#'
space = ''
print('Please enter a number 1-5 to construct a tree.')
user_input = int(input('>'))

for num in range(1, user_input):
    print(branch * num)
