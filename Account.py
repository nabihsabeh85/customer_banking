class Account:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.balance = new_balance
        else:
            print("Invalid balance amount.")

    def set_interest(self, new_interest):
        if new_interest >= 0:
            self.interest = new_interest
        else:
            print("Invalid interest amount.")

