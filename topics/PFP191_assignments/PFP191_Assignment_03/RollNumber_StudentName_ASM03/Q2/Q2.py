# Question 2 (3 marks):
# The given file Q2.py already contains statements to input a string s.
# You should write statements to print the number of word in strings s.
# Notes:
# - Do not edit given statements in the main function.
# - You can create new functions if you see it is necessary.
# - The string was removed all extra space.
# Sample input and output:
# Input: I miss you
# After processing: 3
# Output for marking:
# OUTPUT:
# 3
def count_words(s: str) -> int:
    # Write your statements here
    if not s:
        return 0
    return len(s.split())
    # End your statements
#End def count_words
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
    print("\nTEST Q2 (3 marks):\n")
    s = input("Input string: ")

    cleaned_string = remove_extra_spaces(s)  # Remove extra spaces
    count = count_words(cleaned_string)  # Call the function to count words

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