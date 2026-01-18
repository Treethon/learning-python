def after_transaction(balance, transaction):
    balance = int(balance)
    transaction = int(transaction)

    if transaction < 0: # Negative was passed
        if balance + transaction < 0: # Double negative, overdrafting
            print('You are overdrafting! Transaction declined.')
            return balance
        else:
            balance = balance + transaction # Double negative
            return balance
    else:
        balance = balance + transaction
        return balance

input_balance = input('Please enter a starting balance: ')
input_transaction = input('Please enter a transaction amount: ')
print('Your balance is: $' + str(after_transaction(input_balance, input_transaction)))