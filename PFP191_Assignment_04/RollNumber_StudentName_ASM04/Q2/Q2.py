# ============================================================================
# Question 2 (3 marks) - PFP191 Assignment 04
# ============================================================================
# The given file Q2.py already contains statements to input data for the
# collection. You should write statements to count the number of occurrences
# of the smallest elements in the array.
#
# Notes:
# - Do not edit given statements in the main function.
# - You can create new functions if you see it is necessary.
#
# Sample input and output:
#   Input: n = 9
#   Array: 1 3 1 4 2 7 8 1 9
#   After processing: 3
#   Output for marking:
#   OUTPUT:
#   3
#
# Full Question:
# The given file Q2.py already contains statements to input data for the
# collection. You should write statements to count the number of occurrences
# of the smallest elements in the array.
#
# Notes:
# - Do not edit given statements in the main function.
# - You can create new functions if you see it is necessary.
#
# Sample input and output:
# Input: n = 9
# Array: 1 3 1 4 2 7 8 1 9
# After processing: 3
# Output for marking:
# OUTPUT:
# 3
# ============================================================================

def find_min_value(a, n):
    # Write your statements here
    min_value = a[0]
    for i in range(1, n):
        if a[i] < min_value:
            min_value = a[i]
    return min_value
    #End your statements
#End def find_min_value

def count_min_items(a, n, min_value):
    # Write your statements here
    count = 0
    for i in range(n):
        if a[i] == min_value:
            count += 1
    return count
    #End your statements
#End def count_min_items
#=============DO NOT ADD NEW OR CHANGE THIS FUNCTIONS========
def read_input():    
    n = int(input("Enter n = "))
    a = [int(input(f"a[{i}] = ")) for i in range(n)]
    return n, a
#End def read_input
#============================================================
#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Q2 (3 marks):")
    n, a = read_input()

    min_value = find_min_value(a, n)

    count = count_min_items(a, n, min_value)
    
    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:")
    print(count)
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
