"""Write a Python program to remove all items from a dictionary while keeping the dictionary object itself intact."""
inventory = {"apples": 10, "bananas": 5, "oranges": 8}
inventory.clear()
print("After clear:", inventory, type(inventory))

