# Question 2 (3 marks):
# Complete the Car class and the SpecCar class (inheriting from Car).
# Car has name and price attributes with getName() (uppercase) and getPrice().
# SpecCar adds a warranty attribute with getWarranty() (AUDI gets +5, others get +2)
# and setWarranty().

class Car:
    # Write your statements here

    def __init__(self, name="", price=0.0):
        self.name = name
        self.price = price

    def getName(self):
        return self.name.upper()

    def getPrice(self):
        return self.price
    #End your statements
#End class Car

class SpecCar(Car):
    # Write your statements here

    def __init__(self, name="", price=0.0, warranty=0):
        super().__init__(name, price)
        self.warranty = warranty

    def getWarranty(self):
        if self.getName() == "AUDI":
            return self.warranty + 5
        else:
            return self.warranty + 2

    def setWarranty(self, value):
        self.warranty = value
    #End your statements
#End class SpecCar

#=============DO NOT ADD NEW OR CHANGE THIS FUNCTIONS========
def displayMenu():
    print("1. Test getName()")
    print("2. Test getWarranty()")
    choice = int(input("Enter TC (1,2): "))
    return choice
#End def displayMenu
#============================================================
#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Q2 (3 marks):")

    name = input("Enter name: ")
    price = float(input("Enter price: "))
    warranty = int(input("Enter warranty: "))

    specCar = SpecCar(name, price, warranty)

    choice = displayMenu()

    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:")
    if choice == 1:
        print(specCar.getName())
    elif choice == 2:
        print(specCar.getWarranty())
#End def main
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
