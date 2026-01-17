balance = 0

def after_transaction(balance, transaction):
    if transaction [is positive]
        balance + transaction
    else transaction [is negative]
        balance - transaction
    
    if the transaction would bring the balance negative, discard transaction and print the original balance