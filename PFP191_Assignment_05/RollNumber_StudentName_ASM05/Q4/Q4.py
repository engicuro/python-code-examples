# Question 4 (3 marks)
# Employee class with:
#   - id: string
#   - name: string
#   - salary: float
#   - position: string
#
# Constructor: Employee(id, name, salary, position)
#   - set the values to id, name, salary, position
#
# Methods:
#   - getAllowance(): float - returns allowance according to position:
#       DEV: 20% of salary
#       TES: 10% of salary
#       Other: 0
#   - getIncome(): float - return salary + allowance
#   - toString(): string - return format: id,name,salary,position,income

class Employee:
    # Write your statements here
    def __init__(self, id, name, salary, position):
        self.id = id
        self.name = name
        self.salary = salary
        self.position = position

    def getAllowance(self):
        if self.position == "DEV":
            return self.salary * 0.2
        elif self.position == "TES":
            return self.salary * 0.1
        else:
            return 0.0

    def getIncome(self):
        return self.salary + self.getAllowance()

    def __str__(self):
        return f"{self.id},{self.name},{self.salary},{self.position},{self.getIncome()}"
    #End your statements
#End class
#=============DO NOT ADD NEW OR CHANGE THIS FUNCTIONS========
def displayMenu():
    print("1. Test getAllowance()")
    print("2. Test getIncome()")
    choice = int(input("Enter TC(1/2):"))
    return choice
#End def displayMenu
#============================================================
#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Employee class (2 marks):")

    id = input("Enter Employee id: ")
    name = input("Enter Employee name: ")
    salary = float(input("Enter Employee salary: "))
    position = input("Enter Employee position: ")

    employee = Employee(id, name, salary, position)

    choice = displayMenu()

    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:")
    if choice == 1:
        print(f"{employee.getAllowance():.2f}")
    elif choice == 2:
        print(f"{employee.getIncome():.2f}")
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
