# Question 1 (3 marks):
# Complete the Shape class and the Circle class (inheriting from Shape).
# Shape has perimeter and area attributes with getters/setters.
# Circle has a radius attribute and methods to calculate area and perimeter,
# storing results into the inherited perimeter and area variables.
#
# Note: We use the value of PI (approximately 3.14159) for calculations.
# PI is the ratio of a circle's circumference to its diameter.

class Shape:
    # Write your statements here

    def __init__(self):
        self.perimeter = 0.0
        self.area = 0.0

    def getArea(self):
        return self.area

    def getPerimeter(self):
        return self.perimeter

    def setPerimeter(self, value):
        self.perimeter = value

    def setArea(self, value):
        self.area = value
    #End your statements
#End class Shape

class Circle(Shape):
    # Write your statements here

    def __init__(self, value=0.0):
        super().__init__()
        self.radius = value
        self.calculateArea()
        self.calculatePerimeter()

    def calculateArea(self):
        self.setArea(3.141592653589793 * self.radius ** 2)

    def calculatePerimeter(self):
        self.setPerimeter(2 * 3.141592653589793 * self.radius)
    #End your statements
#End class Circle

#=============DO NOT ADD NEW OR CHANGE THIS FUNCTIONS========
def displayMenu():
    print("1. Test calculatePerimeter()")
    print("2. Test calculateArea()")
    choice = int(input("Enter TC(1/2): "))
    return choice
#End def displayMenu
#============================================================
#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Q1 (3 marks):")

    radius = float(input("Enter radius: "))
    circle = Circle(radius)
    choice = displayMenu()

    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:")
    if choice == 1:
        print(f"{circle.getPerimeter():.2f}")
    elif choice == 2:
        print(f"{circle.getArea():.2f}")
#End def main
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
