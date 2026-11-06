"""Encapsulation - Exercise."""

class BankAccount:
    """A bank account class demonstrating encapsulation."""

    def __init__(self, owner, balance=0):
        """Initialize the bank account."""
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        """Get the current balance."""
        return self.__balance

def encapsulation():
    """Demonstrate encapsulation."""
    account = BankAccount("Alice", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Final balance: ${account.get_balance()}")

    # Trying to access private attribute directly (will fail)
    try:
        print(account.__balance)
    except AttributeError:
        print("Cannot access private attribute directly!")

if __name__ == "__main__":
    encapsulation()
