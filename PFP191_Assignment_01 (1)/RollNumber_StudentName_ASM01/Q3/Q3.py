"""
Question 3 (2 marks):
The given file Q3.cpp contains statements to input data for two integers a, b (b>0).
You should write statements to print the result of dividing a by b and the remainder of that division.

Sample input and output:
Input: a = 5, b = 2
After processing: 2 1
Output for marking:
OUTPUT:
2
1
"""

# DO NOT ADD NEW OR CHANGE THESE STATEMENTS
def main():
    print("\nTEST Q3 (2 marks):\n")
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
#===========================================
    
    # Write your statements here
    quotient = a // b
    remainder = a % b
    # End your statements

# DO NOT ADD NEW OR CHANGE THESE STATEMENTS
# Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:")
#===========================================
    
    # Write your statements output here in the specified format.
    print(quotient)
    print(remainder)
    # End your statements

# DO NOT ADD NEW OR CHANGE THESE STATEMENTS
#end def main
if __name__ == "__main__":
    main()
#===========================================