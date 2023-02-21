class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")


account_number = input("Enter account number: ")

bank_account = BankAccount(account_number)

deposit_amount = float(input("Enter deposit amount: "))

bank_account.deposit(deposit_amount)

withdrawal_amount = float(input("Enter withdrawal amount: "))

bank_account.withdraw(withdrawal_amount)

print("Current balance:", bank_account.balance)
