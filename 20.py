"""Take a given list and modify it through five specific actions:
1.	Change Element: Change the second element of a list to 200 and print the updated list.
2.	Append Element: Add 600 to the end of a list and print the new list.
3.	Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
4.	Remove Element (by value): Remove 600 from the list and print the list.
5.	Remove Element (by index): Remove the element at index 0 from the list and print the list.
"""
my_list = [100, 200, 300, 400, 500]

# 1. Change Element: Change the second element of a list to 200 and print the updated list.
my_list[1] = 200
print("After changing second element:", my_list)

# 2. Append Element: Add 600 to the end of a list and print the new list.
my_list.append(600)
print("After appending 600:", my_list)

# 3. Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
my_list.insert(2, 300)
print("After inserting 300 at index 2:", my_list)

# 4. Remove Element (by value): Remove 600 from the list and print the list.
my_list.remove(600)
print("After removing 600:", my_list)

# 5. Remove Element (by index): Remove the element at index 0 from the list and print the list.
del my_list[0]
print("After removing element at index 0:", my_list)
