# ============================================================================
# Question 3 (2 marks) - PFP191 Assignment 04
# ============================================================================
# The given file Q3.py already contains statements to input data for the
# collection and an integer variable named x. You should write statements to
# print the average of all the elements that are prime and greater than x
# (the primes start from 2). If none prime greater than x then print 0.00.
#
# Notes:
# - Do not edit given statements in the main function.
# - You can create new functions if you see it is necessary.
# - The output result is formatted in two decimal places
#
# Sample input and output:
#   Input: n = 9
#   Array: 1 3 5 4 2 7 8 11 9
#   Input: x = 3
#   After processing: (5 + 7 + 11) / 3 = 23/3 = 7.67
#   Output for marking:
#   OUTPUT:
#   7.67
#
# Full Question:
# The given file Q3.py already contains statements to input data for the
# collection and an integer variable named x. You should write statements to
# print the average of all the elements are prime greater than x (the primes
# start from 2). If none prime greater than x then print 0.00.
#
# Notes:
# - Do not edit given statements in the main function.
# - You can create new functions if you see it is necessary.
# - The output result is formatted in two decimal places
#
# Sample input and output:
# Input: n = 9
# Array: 1 3 5 4 2 7 8 11 9
# Input: x = 3
# After processing: (5 + 7 + 11) / 3 = 23/3 = 7.67
# Output for marking:
# OUTPUT:
# 7.67
# ============================================================================

def is_prime(num):
    # Write your statements here
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    #End your statements
#End def is_prime

def calculate_avg(n, a, x):
    # Write your statements here
    total = 0
    count = 0
    for i in range(n):
        if a[i] > x and is_prime(a[i]):
            total += a[i]
            count += 1
    if count == 0:
        return 0.0
    return total / count
    #End your statements
#End def calculate_avg   
#=============DO NOT ADD NEW OR CHANGE THIS FUNCTIONS========
def read_input():    
    n = int(input("Enter n = "))
    a = [int(input(f"a[{i}] = ")) for i in range(n)]
    x = int(input("Enter x = "))
    return n, a, x
#End def read_input
#============================================================
#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Q3 (2 marks):")
    n, a, x = read_input()
    avg = calculate_avg(n, a, x)
    
    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.   
    print("\nOUTPUT:")    
    print(f"{avg:.2f}")
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================
