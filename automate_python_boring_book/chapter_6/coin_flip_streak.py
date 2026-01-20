import random

number_of_streaks = 0

for experiment_number in range(10000):
    list_to_check = []
    for flip in range(100):
        i = random.randint(0, 1)
        if i == 0:
            list_to_check += 'H'
        else:
            list_to_check += 'T'

    has_streak = False
    for x in range(len(list_to_check) - 5):
        if list_to_check[x:x + 6] == ['T'] * 6  or list_to_check[x:x + 6] == ['H'] * 6:
            has_streak = True
            break
    if has_streak:
        number_of_streaks += 1

print('Chance of streak: %s%%' % (number_of_streaks / 100))