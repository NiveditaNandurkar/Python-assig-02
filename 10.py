"""Write a script to perform the following three operations on given list:
1.	Access the third element of a list
2.	List Length: Print the total number of items
3.	Check if the list is empty"""
my_list = [1, 2, 3, 4, 5]

# 1. Access the third element of a list
print("Third element:", my_list[2])

# 2. List Length: Print the total number of items
print("List length:", len(my_list))

# 3. Check if the list is empty
if not my_list:
    print("The list is empty.")
else:
    print("The list is not empty.")