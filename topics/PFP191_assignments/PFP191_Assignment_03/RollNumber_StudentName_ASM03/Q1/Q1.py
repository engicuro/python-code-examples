# Question 1 (2 marks):
# The given file Q1.py already contains statements to input a string s.
# You should write statements to print the number of digits in strings s.
# Notes:
# - Do not edit given statements in the main function
# - You can create new functions if you see it is necessary.
# - The string was removed all extra space.
# Sample input and output:
# Input: Test Q1 (2 marks)
# After processing: 2
# Output for marking:
# OUTPUT:
# 2
def count_digits(s: str) -> int:
    # Write your statements here
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    return count
    # End your statements
#End def count_digits
#=============DO NOT ADD NEW OR CHANGE THIS FUNCTIONS========
def remove_extra_spaces(s: str) -> str:
    # Replace multiple spaces with a single space
    s = ' '.join(s.split())
    
    # Remove leading and trailing spaces
    return s.strip()
#End def remove_extra_spaces
#============================================================

#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Q1 (2 marks):\n")
    s = input("Input string: ")
    
    cleaned_string = remove_extra_spaces(s)  # Remove extra spaces
    count = count_digits(cleaned_string)  # Call the function to count digits
    
    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:\n")
    print(count)
    print()    
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================