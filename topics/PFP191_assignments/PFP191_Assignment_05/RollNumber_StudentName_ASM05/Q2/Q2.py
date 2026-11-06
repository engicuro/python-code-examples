# Question 2 (3 marks)
# BankAccount class with:
#   - account: string
#   - holder: string
#   - balance: float
#
# Constructor: BankAccount(account, holder, balance)
#   - set the values to account, holder and balance
#
# Methods:
#   - deposit(float amount) - Increase balance with amount
#   - withdraw(float amount): bool - if balance < amount return false; otherwise decrease balance with amount and return true
#   - toString(): string - return format: account,holder,balance (balance formatted with two decimal places)

class BankAccount:
    #Write your statements here
    def __init__(self, account, holder, balance):
        self.account = account
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            return False
        else:
            self.balance -= amount
            return True

    def __str__(self):
        return f"{self.account},{self.holder},{self.balance:.2f}"
    #End your statements
#End class
#=============DO NOT ADD NEW OR CHANGE THIS FUNCTIONS========
def displayMenu():
    print("1. Test deposit()")
    print("2. Test withdraw()")
    choice = int(input("Enter TC(1/2):"))
    return choice
#End def displayMenu
#============================================================
#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Q2 (3 marks):")

    accNumber = input("Enter account number: ")
    accHolder = input("Enter account holder name: ")
    initialBalance = float(input("Enter initial balance: "))

    account = BankAccount(accNumber, accHolder, initialBalance)

    print("\nAccount information:")
    print(account)

    choice = displayMenu()

    if choice == 1:
        depositAmount = float(input("Enter amount to deposit: "))
        account.deposit(depositAmount)
    elif choice == 2:
        withdrawAmount = float(input("Enter amount to withdraw: "))
        account.withdraw(withdrawAmount)        

    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:")
    print(account)
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
