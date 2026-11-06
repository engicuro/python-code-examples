# Question 1 (2 marks)
# Student class with:
#   - code : string
#   - name: string
#   - markOfMath : int
#   - markOfEng: int
#
# Constructor: Student(code, name, markOfMath, markOfEng)
#   - set the values to code, name, markOfMath, markOfEng
#
# Methods:
#   - getMarkOfMath(): int - return markOfMath
#   - getMarkOfEng(): int - return markOfEng
#   - getGPA(): float - return GPA with formula: gpa = (markOfMath * 3 + markOfEng * 2) / 5
#   - toString(): string - return format: code,name,markOfMath,markOfEng

class Student:
    # Write your statements here
    def __init__(self, code, name, markOfMath, markOfEng):
        self.code = code
        self.name = name
        self.markOfMath = markOfMath
        self.markOfEng = markOfEng

    def getMarkOfMath(self):
        return self.markOfMath

    def getMarkOfEng(self):
        return self.markOfEng

    def getGPA(self):
        return (self.markOfMath * 3 + self.markOfEng * 2) / 5

    def __str__(self):
        return f"{self.code},{self.name},{self.markOfMath},{self.markOfEng}"
    #End your statements
#End class
#=============DO NOT ADD NEW OR CHANGE THIS FUNCTIONS========
def displayMenu():
    print("1. Test getMark()")
    print("2. Test getGPA()")
    choice = int(input("Enter TC(1/2):"))
    return choice
#End def displayMenu
#============================================================
#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Q1 (2 marks):")

    code = input("Enter student code: ")
    name = input("Enter student name: ")
    markOfMath = int(input("Enter mark of Math: "))
    markOfEng = int(input("Enter mark of English: "))

    student = Student(code, name, markOfMath, markOfEng)

    print("\nStudent information:")
    print(student)

    choice = displayMenu()

    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:")
    if choice == 1:
        print(f"{student.getMarkOfMath()},{student.getMarkOfEng()}")
    elif choice == 2:
        print(f"{student.getGPA():.2f}")

#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
