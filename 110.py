"""
Write a Python program to add a new key-value pair to a dictionary, modify an existing value, and access a specific key.
"""
student = {"name": "Alice", "age": 20, "grade": "B"}
# Add a new key-value pair 
student["school"] = "XYZ High"
print("After adding key:", student)
# Modify an existing value 
student["age"] = 21
print("After modifying value:", student)
# Access a specific key 
print("Accessing 'name':", student["name"])
