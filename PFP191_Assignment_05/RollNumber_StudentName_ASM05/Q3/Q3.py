# Question 3 (2 marks)
# Product class with:
#   - id: string
#   - name: string
#   - price: int
#   - quantity: int
#
# Constructor: Product(id, name, price, quantity)
#   - set the values to id, name, price, quantity
#
# Methods:
#   - getTotal(): int - return price * quantity, if quantity >= 50, discount 10%
#   - toString(): string - return format: id,name,price,quantity

class Product:
    # Write your statements here
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def getTotal(self):
        if self.quantity >= 50:
            return self.price * self.quantity * 0.9
        else:
            return self.price * self.quantity

    def __str__(self):
        return f"{self.id},{self.name},{self.price},{self.quantity}"
    #End your statements
#End class
#=============DO NOT ADD NEW OR CHANGE THIS FUNCTIONS========
def displayMenu():
    print("1. Test getTotal()")
    print("2. Test constructor()")
    choice = int(input("Enter TC(1/2):"))
    return choice
#End def displayMenu
#============================================================
#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Q3 (2 marks):")

    id = input("Enter Product id: ")
    name = input("Enter Product name: ")
    price = int(input("Enter Product price: "))
    quantity = int(input("Enter Product quantity: "))

    product = Product(id, name, price, quantity)

    choice = displayMenu()

    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:")
    if choice == 1:
        print(f"{product.getTotal():.2f}")
    elif choice == 2:
        print(product)
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
