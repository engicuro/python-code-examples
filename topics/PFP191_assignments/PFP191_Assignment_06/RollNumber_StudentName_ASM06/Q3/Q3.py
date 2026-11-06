# Question 3 (4 marks):
# Complete the Medicine class and the PrescriptionMedicine class (inheriting from Medicine).
# Medicine has name, indication, and expirationYear attributes with getters and toString().
# PrescriptionMedicine adds a doctorName attribute with getDoctorName(), setDoctorName(),
# isExpired() (returns "Expired" or "Valid"), and an overridden toString().

class Medicine:
    # Write your statements here

    def __init__(self, name="", indication="", expirationYear=0):
        self.name = name
        self.indication = indication
        self.expirationYear = expirationYear

    def getName(self):
        return self.name.capitalize()

    def getIndication(self):
        return self.indication.capitalize()

    def getExpirationYear(self):
        return self.expirationYear

    def toString(self):
        return f"{self.getName()}, {self.getIndication()}, {self.getExpirationYear()}"
    #End your statements
#End class Medicine

class PrescriptionMedicine(Medicine):
    # Write your statements here

    def __init__(self, name="", indication="", expirationYear=0, doctorName=""):
        super().__init__(name, indication, expirationYear)
        self.doctorName = doctorName

    def getDoctorName(self):
        return self.doctorName.capitalize()

    def setDoctorName(self, name):
        self.doctorName = name

    def isExpired(self, currentYear):
        if currentYear > self.expirationYear:
            return "Expired"
        else:
            return "Valid"

    def toString(self):
        return f"{self.getName()}, {self.getIndication()}, {self.getExpirationYear()}, {self.getDoctorName()}"

    def __str__(self):
        return self.toString()
    #End your statements
#End class PrescriptionMedicine

#=============DO NOT ADD NEW OR CHANGE THIS FUNCTIONS========
def displayMenu():
    print("1. Test getIndication()")
    print("2. Test isExpired()")
    print("3. Test toString()")
    choice = int(input("Enter TC (1|2|3): "))
    return choice
#End def displayMenu
#============================================================
#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Q3 (4 marks):")

    name = input("Enter the medicine: ")
    indication = input("Enter the indication: ")
    expirationYear = int(input("Enter the expiration year: "))
    doctorName = input("Enter the doctor's name: ")

    med = PrescriptionMedicine(name, indication, expirationYear, doctorName)

    choice = displayMenu()

    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    if choice == 1:
        print("\nOUTPUT:")
        print(med.getIndication())
    elif choice == 2:
        currentYear = int(input("Enter current year: "))
        print("\nOUTPUT:")
        print(med.isExpired(currentYear))
    elif choice == 3:
        print("\nOUTPUT:")
        print(med)
#End def main
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
