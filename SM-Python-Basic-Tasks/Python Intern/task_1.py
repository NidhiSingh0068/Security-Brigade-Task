# Task 1

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

#######################################################################################################################################################################




def first_and_last_element_list(num_list):
    return [num_list[0], num_list[-1]]


#Driver Code

num_list=[]
n = int(input("Enter number of elements in list = "))
print("Enter elements :")
for i in range(0, n):
    e = int(input())
    num_list.append(e)
print(num_list)
print("The first and last element in given list are = ",first_and_last_element_list(num_list))
    
    
