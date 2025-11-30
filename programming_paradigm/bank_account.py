class BankAccount:
    # Constructor initializes a new bank account.
    # initial_balance is optional and defaults to 0 if nothing is passed.
    def __init__(self, initial_balance=0):
        # Encapsulated attribute representing the current balance
        self.account_balance = initial_balance

    # Adds money to the account balance
    def deposit(self, amount):
        self.account_balance += amount

    # Attempts to withdraw money from the account.
    # Returns True if successful, False if there are insufficient funds.
    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    # Displays the current account balance in a formatted, user-friendly way.
    def display_balance(self):
        print(f"Your current balance is: ${self.account_balance:.2f}")


# --- Example usage below (NOT required in ALX task, just demonstration) ---

acc = BankAccount(250)   # Create an account starting with $250

acc.display_balance()    # Should print: $250.00

acc.deposit(50)          # Add $50 to the account
acc.display_balance()    # Should print: $300.00

acc.withdraw(120)        # Withdraw $120
acc.display_balance()    # Should print: $180.00
