# Question 4 (3 marks):
# The given file Q4.py already contains statements to input a string s.
# You should write statements to compress a string using the counts of repeated characters.
# For example, the string "aabcccccaaa" would become "a2b1c5a3".
# Notes:
# - Do not edit given statements in the main function.
# - You can create new functions if you see it is necessary.
# - The string was removed all extra spaces
# Sample input and output:
# Input: aabcccccaaa
# After processing: a2b1c5a3
# Output for marking:
# OUTPUT:
# a2b1c5a3
def compress_string(s: str) -> str:
    # Write your statements here
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return "".join(result)
    # End your statements
#End def compress_string
#=============DO NOT ADD NEW OR CHANGE MAIN FUNCTION=======
def main():
    print("\nTEST Q4 (3 marks):\n")
    s = input("Input string: ")

    compressed_string = compress_string(s)  # Compress the string

    #=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
    # Changing the output format will result in a score of 0 for this question.
    print("\nOUTPUT:\n")
    print(compressed_string)
    print()
#End def main   
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == '__main__':
    main()
#============================================================