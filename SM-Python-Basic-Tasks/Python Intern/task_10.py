# Task 10


# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Example:
# If the following email address is given as input to the program:

# akita@securitybrigade.com

# Then, the output of the program should be:

# securitybrigade

# In case of input data being supplied to the question, it should be assumed to be a console input.


#######################################################################################################################################################################


def get_company_name(a):
        return a.replace("@",".").split(".")[1]


# Driver Code
e_mail=input("Enter your e-mail id : ")
print(get_company_name(e_mail))
