print('Enter an integer')
user_number = int(input())
if user_number % 3 == 0 and user_number % 5 == 0:
    print('Fizz Buzz')
elif user_number % 3 == 0:
    print('Fizz')
elif user_number % 5 == 0:
    print('Buzz')
else:
    print(str(user_number))