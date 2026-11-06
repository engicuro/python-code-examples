# Question 3 (2 marks):
# The given file Q3.py already contains statements to input a string s.
# You should write statements to capitalize the strings.
# For example, capitalize from "FPT university" to "Fpt University"
# Notes:
# - Do not edit given statements in the main function.
# - You can create new functions if you see it is necessary.
# - The string was removed all extra space.
# Sample input and output:
# Input: FPT university
# After processing: Fpt University
# Output for marking:
# OUTPUT:
# Fpt University
def capitalize_words(s: str) -> str:
    # Write your statements here
    return s.title()
    # End your statements
#End def capitalize_words
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
    print("\nTEST Q3 (2 marks):\n")
    s = input("Input string: ")

    cleaned_string = remove_extra_spaces(s)  # Remove extra spaces
    # Capitalize words
    capitalized_string = capitalize_words(cleaned_string)

    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:\n")
    print(capitalized_string)
    print()
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================