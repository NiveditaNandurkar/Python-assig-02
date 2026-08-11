"""Write a Python program to combine two dictionaries into a single dictionary. If both dictionaries share a key, the value from the second dictionary should take precedence.
"""
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2} 
print("Merged dictionary:", merged)
