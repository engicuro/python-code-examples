"""
Question 1 (3 marks):
The given file Q1.cpp contains statements to input data for 2 integers a and b,
which are 2 sides of a right triangle. You should write statements to print the
area and perimeter of the triangle.

Hint:
- The area of a right triangle is (a*b)/2
- The hypotenuse c of a right triangle is calculated as sqrt(a*a + b*b)
- The perimeter of the triangle is a+b+c

Notes:
- The output result is formatted in two decimal places

Sample input and output:
Input: a = 3, b = 4
After processing: 6.00 and 12.00
Output for marking:
OUTPUT:
6.00
12.00
"""

# This program calculates the area and perimeter of a right triangle.
# A right triangle has two sides (a and b) that form the right angle,
# and a hypotenuse (c) which is the longest side.
#
# Formulas:
#   - Area = (a * b) / 2
#   - Hypotenuse c = sqrt(a^2 + b^2)
#   - Perimeter = a + b + c

import math

# DO NOT ADD NEW OR CHANGE THESE STATEMENTS
def main():
    print("\nTEST Q1 (3 marks):\n")
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    area = 0
    perimeter = 0
#===========================================
    
    # Write your statements here
    # Step 1: Calculate the hypotenuse using the Pythagorean theorem
    c = math.sqrt(a*a + b*b)
    # Step 2: Calculate the area of the right triangle
    area = (a * b) / 2
    # Step 3: Calculate the perimeter by adding all three sides
    perimeter = a + b + c
    # End your statements

# DO NOT ADD NEW OR CHANGE THESE STATEMENTS
# Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:")
    print(f"{area:.2f}")
    print(f"{perimeter:.2f}")
#===========================================
#end def main
    
if __name__ == "__main__":
    main()
#===========================================