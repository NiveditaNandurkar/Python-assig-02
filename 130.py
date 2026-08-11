"""Write a Python program to create a dictionary by mapping two equal-length lists, one containing keys and the other containing values."""
keys = ["name", "age", "city"]
values = ["Bob", 25, "London"]
mapped_dict = dict(zip(keys, values)) 
print("Mapped dictionary:", mapped_dict)
