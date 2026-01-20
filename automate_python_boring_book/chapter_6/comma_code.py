def list_to_string(old_list):
    new_string = ''
    for i in old_list:
        if i in old_list[-1]:
            new_string += 'and ' + i
        else:
            new_string += i + ', '
    print(new_string)
    return new_string

test_list = ['Spartacus', 'Spooky', 'Tibbs']

list_to_string(test_list)