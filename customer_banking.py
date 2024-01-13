from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    savings_balance = float(input("Enter initial savings balance: $"))
    savings_rate = float(input("Enter savings interest rate (%): "))
    savings_months = int(input("Enter the duration in months: "))
    updated_balance, interest_earned = create_savings_account(savings_balance, savings_rate, savings_months)
    print(f"Updated balance: ${updated_balance:.2f}")
    print(f"Interest earned: ${interest_earned:.2f}")

    cd_balance = float(input("Enter initial CD balance: $"))
    cd_rate = float(input("Enter CD interest rate (%): "))
    cd_months = int(input("Enter the duration in months: "))
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_rate, cd_months)
    print(f"Updated CD balance: ${updated_cd_balance:.2f}")
    print(f"CD Interest earned: ${cd_interest_earned:.2f}")

if __name__ == "__main__":
    main()
