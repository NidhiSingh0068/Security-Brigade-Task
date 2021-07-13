# Task 2

# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

# My name is Michele

# Then I would see the string:

#  Michele is name My

# shown back to me.


#######################################################################################################################################################################


#method 1
def reverse_str(str):
    words = str.split()
    words = list(reversed(words))
    return(" ".join(words))

#method 2
def reverse_string(str):
    list_of_words = str.split()
    reverse_list = list_of_words[::-1]
    #print(reverse_list)
    rev_str = " " 
    return (rev_str.join(reverse_list))
    

#Driver Code
str = input("Enter a string : ")
print("Original String : ",str)
print("Reversed String (Method 1) : ",reverse_str(str))
print("Reversed String (Method 2) : ",reverse_string(str))
