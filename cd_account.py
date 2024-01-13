from Account import Account

def create_cd_account(balance, interest_rate, months):
    cd_account = Account(balance, 0)
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    new_balance = balance + interest_earned
    cd_account.set_balance(new_balance)
    cd_account.set_interest(interest_earned)
    return new_balance, interest_earned
