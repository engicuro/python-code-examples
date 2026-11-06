"""
Question 2 (2 marks):
The given file Q2.cpp contains statements to input data for 3 integers a, b and c.
You should write statements to get the smallest and largest number among the 3 numbers.

Sample input and output:
Input: a = 6, b = 5, c = 3
After processing: result : 3 6
Output for marking:
OUTPUT:
3
6
"""

# DO NOT ADD NEW OR CHANGE THESE STATEMENTS
def main():
    print("\nTEST Q2 (2 marks):\n")
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    c = int(input("Enter c = "))
    smallest = 0
    largest = 0
#===========================================
    
    # Write your statements here
    smallest = min(a, b, c)
    largest = max(a, b, c)
    # End your statements

# DO NOT ADD NEW OR CHANGE THESE STATEMENTS
# Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:")
    print(smallest)
    print(largest)
#===========================================
#end def main
    
if __name__ == "__main__":
    main()
