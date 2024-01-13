from Account import Account

def create_savings_account(balance, interest_rate, months):
    savings_account = Account(balance, 0)
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    new_balance = balance + interest_earned
    savings_account.set_balance(new_balance)
    savings_account.set_interest(interest_earned)
    return new_balance, interest_earned
