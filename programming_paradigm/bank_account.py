class BankAccount:
    """Simple BankAccount class to demonstrate basic OOP and encapsulation."""

    def __init__(self, initial_balance=0):
        """
        Initialize a new BankAccount instance.

        Args:
            initial_balance (int | float, optional): Starting balance. Defaults to 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Add amount to the account balance.

        Args:
            amount (int | float): Amount to deposit.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Attempt to withdraw amount from the account.

        Args:
            amount (int | float): Amount to withdraw.

        Returns:
            bool: True if withdrawal succeeded, False if insufficient funds.
        """
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        """
        Print the current balance in the format expected by the tests.
        Note: tests expect the exact substring "Current Balance:".
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
