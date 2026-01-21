def get_end_coordinates(directions):
    x_axis = 0
    y_axis = 0
    for direction in directions:
        if direction == 'E':
            x_axis += 1
        elif direction == 'W':
            x_axis -= 1
        elif direction == 'N':
            y_axis += 1
        else:  # Direction is S
            y_axis -= 1
    print('[' + str(x_axis) + ',' + str(y_axis) + ']')

user_directions = []
while True:
    user_input = input('Please enter N/S/E/W or press enter: ').upper()
    if user_input == '':
        break
    else:
        user_directions += user_input

get_end_coordinates(user_directions)