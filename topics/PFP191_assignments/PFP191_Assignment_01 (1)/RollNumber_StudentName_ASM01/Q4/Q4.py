"""
Question 4 (3 marks):
The given file Q4.cpp contains statements to input data for 2 integers r and h,
which are the radius and height of the cylinder. You should write statements to print the volume of the cylinder.

Hint:
- You must use PI in math library to get the Pi number.

Notes:
- The output result is formatted in two decimal places

Sample input and output:
Input: a=1, h =5
After processing: 15.71
Output for marking:
OUTPUT:
15.71
"""

# This program calculates the volume of a cylinder.
# A cylinder has a radius (r) and a height (h).
#
# Formula:
#   - Volume = pi * r^2 * h

import math

# DO NOT ADD NEW OR CHANGE THESE STATEMENTS
def main():
    print("\nTEST Q4 (3 marks):\n")
    r = int(input("Enter r = "))
    h = int(input("Enter h = "))
#===========================================
    
    # Write your statements here
    # Calculate the volume of the cylinder
    # Volume = pi * radius^2 * height
    volume = math.pi * r * r * h
    # End your statements

# DO NOT ADD NEW OR CHANGE THESE STATEMENTS
# Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:")
#===========================================
    
    # Write your statements output here in the specified format.
    print(f"{volume:.2f}")
    # End your statements
    
# DO NOT ADD NEW OR CHANGE THESE STATEMENTS
#end def main
if __name__ == "__main__":
    main()
#===========================================