# ============================================================================
# Question 4 (3 marks) - PFP191 Assignment 04
# ============================================================================
# The given file Q4.py already contains statements to input data for the
# collection. You should write statements to print the sum of the largest
# and smallest elements in the array.
#
# Notes:
# - Do not edit given statements in the main function.
# - You can create new functions if you see it is necessary.
# - The output result is formatted in two decimal places
#
# Sample input and output:
#   Input: n = 10
#   Array: 2 3 5 4 2 7 8 11 9 11
#   After processing: (2 + 2 + 11 + 11) = 26
#   Output for marking:
#   OUTPUT:
#   26
#
# Full Question:
# The given file Q4.py already contains statements to input data for the
# collection. You should write statements to print the sum of the largest
# and smallest elements in the array.
#
# Notes:
# - Do not edit given statements in the main function.
# - You can create new functions if you see it is necessary.
# - The output result is formatted in two decimal places
#
# Sample input and output:
# Input: n = 10
# Array: 2 3 5 4 2 7 8 11 9 11
# After processing: (2 + 2 + 11 + 11) = 26
# Output for marking:
# OUTPUT:
# 26
# ============================================================================

def find_min_max(a, n):    
    min_value = a[0]
    max_value = a[0]
    # Write your statements here
    for i in range(1, n):
        if a[i] < min_value:
            min_value = a[i]
        if a[i] > max_value:
            max_value = a[i]
    #End your statements        
    return min_value, max_value
#End def find_min_max

def sum_min_max_values(a, n, min_value, max_value):
    # Write your statements here
    total = 0
    for i in range(n):
        if a[i] == min_value or a[i] == max_value:
            total += a[i]
    return total
    #End your statements
#End sum_min_max_values
#=============DO NOT ADD NEW OR CHANGE THIS FUNCTIONS========
def read_input():    
    n = int(input("Enter n = "))
    a = [int(input(f"a[{i}] = ")) for i in range(n)]
    return n, a
#End def read_input
#============================================================
#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Q4 (3 marks):")
    n, a = read_input()
    min_value, max_value = find_min_max(a, n)
    total_sum = sum_min_max_values(a, n, min_value, max_value)
    
    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:")
    print(total_sum)
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
