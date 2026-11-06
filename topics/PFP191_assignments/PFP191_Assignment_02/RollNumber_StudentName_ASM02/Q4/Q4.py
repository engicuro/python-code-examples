# ============================================================================
# Question 4 (3 marks) - PFP191 Assignment 02
# ============================================================================
# The given file Q4.py contains statements to input data for non-negative
# integers less than 100. You should write statements to print that number
# in words (digit by digit).
#
# Notes:
# - The output result is formatted in two decimal places (per PDF notes)
#
# Sample input and output:
#   Input: 80  ->  Output: Eight Zero
#   Input: 8   ->  Output: Eight
#   Input: 18  ->  Output: One Eight
# ============================================================================

def main(): 
    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    print("\nTEST Q4 (3 marks):\n")

    n = int(input("Enter a number (0-99): "))
    division, remainder = 0, 0

    #============================================================

    # Write your statements here
    words = ["Zero", "One", "Two", "Three", "Four",
             "Five", "Six", "Seven", "Eight", "Nine"]

    division, remainder = n // 10, n % 10

    if division == 0:
        result = words[remainder]
    else:
        result = words[division] + " " + words[remainder]
    # End your statements

    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:\n")
    #============================================================

    # Write your statements output here in the specified format.
    print(result)
    # End your statements
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================