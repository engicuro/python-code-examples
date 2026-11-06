# ============================================================================
# Question 1 (3 marks) - PFP191 Assignment 02
# ============================================================================
# The given file Q1.py contains statements to input data for 3 integers a, b
# and c, which are the scores of subjects of a student. You should write
# statements to calculate the avg average of the above subjects and print the
# result, which can be classified as "Excellent" if avg >= 9, "Good" if
# avg >= 8, "Average" if avg >= 7, and "Poor" otherwise.
#
# Notes:
# - The output result is formatted in two decimal places
#
# Sample input and output:
#   Input: a = 9, b = 9, c = 9  ->  Output: 9.00 / Excellent
#   Input: a = 8, b = 8, c = 8  ->  Output: 8.00 / Good
#   Input: a = 6, b = 6, c = 6  ->  Output: 6.00 / Poor
#       (PDF sample table has a typo: it shows "9.00 Average" for this case,
#        but avg = 6 < 7, so by the stated rule the class is "Poor")
#   Input: a = 4, b = 4, c = 5  ->  Output: 4.33 / Poor
# ============================================================================

def main():
    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    print("\nTEST Q1 (3 marks):\n")
    
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    c = int(input("Enter c = "))
    
    #============================================================
    
    # Write your statements here
    avg = (a + b + c) / 3.0
    # End your statements
    
    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:\n")
    #============================================================
    
    # Write your statements output here in the specified format.
    print("{:.2f}".format(avg))
    if avg >= 9:
        print("Excellent")
    elif avg >= 8:
        print("Good")
    elif avg >= 7:
        print("Average")
    else:
        print("Poor")
    # End your statements
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================

