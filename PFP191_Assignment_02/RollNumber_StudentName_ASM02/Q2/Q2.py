# ============================================================================
# Question 2 (2 marks) - PFP191 Assignment 02
# ============================================================================
# The given file Q2.py contains the commands to input the temperature and the
# temperature selection (Celsius, Fahrenheit and Kelvin). You should write the
# commands to convert the three temperatures.
#
# Hint:
# - Fahrenheit = (Celsius * 9.0 / 5.0) + 32
# - Kelvin     = Celsius + 273.15
#
# Notes:
# - The output result is formatted in two decimal places
# - Print all three values (Celsius, Fahrenheit, Kelvin), each on its own line.
#
# Sample input and output:
#   Input: 37 and 1 (Celsius)        ->  37.00 / 98.60 / 310.15
#   Input: 98.60 and 2 (Fahrenheit) ->  37.00 / 98.60 / 310.15
#   Input: 310.15 and 3 (Kelvin)    ->  37.00 / 98.60 / 310.15
# ============================================================================

def main():
    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    print("\nTEST Q2(2 marks):\n")
    
    temp = float(input("Enter temperature: "))
    choice = int(input("Enter temperature unit (1: Celsius, 2: Fahrenheit, 3: Kelvin): "))
    
    #============================================================
    
    # Write your statements here
    if choice == 1:          # input is Celsius
        celsius = temp
    elif choice == 2:        # input is Fahrenheit
        celsius = (temp - 32.0) * 5.0 / 9.0
    else:                    # input is Kelvin
        celsius = temp - 273.15

    fahrenheit = (celsius * 9.0 / 5.0) + 32.0
    kelvin = celsius + 273.15
    # End your statements
    
    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:\n")
    #============================================================
    
    # Write your statements output here in the specified format.
    print("{:.2f}".format(celsius))
    print("{:.2f}".format(fahrenheit))
    print("{:.2f}".format(kelvin))
    # End your statements
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
