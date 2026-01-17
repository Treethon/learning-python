number_reached = False

def collatz(number):
    total = 0
    if number % 2 == 0:
        total = number // 2
        print(total, end= ' ')
        return total
    else:
        total = (3 * number) + 1
        print(total, end= ' ')
        return total

user_input = input('Enter an integer: ')
try:
    number = int(user_input)
except ValueError:
    print('Error!  Must be an integer.')

num_to_check = collatz(user_input)

while number_reached == False:
    if num_to_check == 1:
        number_reached = True
    else:
        num_to_check = collatz(num_to_check)
