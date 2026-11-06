# ============================================================================
# Question 3 (2 marks) - PFP191 Assignment 02
# ============================================================================
# The given file Q3.py contains statements to input data for two integers
# a, b. You should write statements to print value of T.
#
# T is given by the piecewise formula (shown as an image in the PDF):
#
#              | a^2 + a*b + sqrt(a*b)   if  a < b  AND  a < 10
#     T   =   |
#              | a*b^2 - 2*a + 5*b       if  a = b  OR   b > 10
#
#   (otherwise T stays 0.0, e.g. a = 9, b = 8 matches neither condition)
#
# Notes:
# - The output result is formatted in two decimal places
#
# Sample input and output:
#   Input: a = 5, b = 9  ->  Output: 76.71   (25 + 45 + sqrt(45))
#   Input: a = 9, b = 9  ->  Output: 756.00  (729 - 18 + 45)
#   Input: a = 9, b = 8  ->  Output: 0.00
# ============================================================================

# This program calculates a value T based on two numbers a and b.
# The formula for T depends on the values of a and b:
#   - If a < b AND a < 10: T = a^2 + a*b + sqrt(a*b)
#   - If a == b OR b > 10: T = a*b^2 - 2*a + 5*b
#   - Otherwise: T = 0

import math
def main():    
    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    print("\nTEST Q3(2 marks):\n")
    
    a = float(input("Enter a = "))
    b = float(input("Enter b = "))
    T = 0.0
    
    #============================================================
    
    # Write your statements here
    # Check the conditions and calculate T accordingly
    if a < b and a < 10:
        # Formula 1: a squared plus a times b plus square root of a times b
        T = a * a + a * b + math.sqrt(a * b)
    elif a == b or b > 10:
        # Formula 2: a times b squared minus 2 times a plus 5 times b
        T = a * b * b - 2 * a + 5 * b
    else:
        # Neither condition matched, so T is 0
        T = 0.0
    # End your statements
    
    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:\n")
    #============================================================
    
    # Write your statements output here in the specified format.
    print("{:.2f}".format(T))
    # End your statements
    
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
