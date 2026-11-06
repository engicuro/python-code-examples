# ============================================================================
# Question 1 (2 marks) - PFP191 Assignment 04
# ============================================================================
# The given file Q1.py already contains statements to input data for the
# collection. You should write statements to print the average of odd numbers
# in even places in the array. If none item, then print 0.00.
#
# Notes:
# - Do not edit given statements in the main function
# - You can create new functions if you see it is necessary.
# - The output result is formatted in two decimal places
#
# Sample input and output:
#   Input: n = 6
#   Array: 1 3 7 4 9 11
#   After processing: (1+7+9) / 3 = 5.67
#   Output for marking:
#   OUTPUT:
#   5.67
#
# Full Question:
# The given file Q1.py already contains statements to input data for the
# collection. You should write statements to print the average of odd numbers
# in even places in the array. If none item, then print 0.00.
#
# Notes:
# - Do not edit given statements in the main function
# - You can create new functions if you see it is necessary.
# - The output result is formatted in two decimal places
#
# Sample input and output:
# Input: n = 6
# Array: 1 3 7 4 9 11
# After processing: (1+7+9) / 3 = 5.67
# Output for marking:
# OUTPUT:
# 5.67
# ============================================================================

def calculate_average(a, n):
    # Write your statements here
    total = 0
    count = 0
    for i in range(0, n, 2):
        if a[i] % 2 != 0:
            total += a[i]
            count += 1
    if count == 0:
        return 0.0
    return total / count
    #End your statements
#End def calculate_average

#=============DO NOT ADD NEW OR CHANGE THIS FUNCTIONS========
def read_input():    
    n = int(input("Enter n = "))
    a = [int(input(f"a[{i}] = ")) for i in range(n)]
    return n, a
#End def read_input
#============================================================
#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Q1 (2 marks):")
    n, a = read_input()

    # Call the function to calculate the average
    avg = calculate_average(a, n)
    
    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:\n")
    # Print the result formatted to two decimal places
    print(f"{avg:.2f}")
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
