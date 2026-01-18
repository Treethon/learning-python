def add(num1, num2):
    total_sum = num1
    for i in range(num2):
        total_sum += plus_one(0)
    return total_sum

def plus_one(number):
    return number + 1

def multiply(num1, num2):
    total_product = 0
    for i in range(num1):
        total_product += num1
    for i in range(num2):
        total_product += num2
    return total_product

user_num1 = input('Please enter the first number: ')
user_num2 = input('Please enter the second number: ')
print('Sum: ' + str(add(int(user_num1), int(user_num2))))
print('Product: ' + str(multiply(int(user_num1), int(user_num2))))