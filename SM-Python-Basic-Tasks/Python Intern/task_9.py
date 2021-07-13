# Task 9

# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.



#########################################################################################################################################################################

def binary_search(list, x):
    left = 0
    right = len(list) - 1
    mid = 0
 
    while(left <= right):
        mid = (right + left) // 2
        if list[mid] < x:
            left = mid + 1
        elif list[mid] > x:
            right = mid - 1
        else:
            return mid
    return -1

#Driver Code

list=[]
n = int(input("Enter number of elements = "))
print("Enter elements in list:")
for i in range(0, n):
    e = int(input())
    list.append(e)
list.sort()
print(list)
x = int(input("Enter an element to search = "))
result = binary_search(list, x)
 
if (result):
    print("Element is present at index", (result))
else:
    print("Element is not present in array")   
    
