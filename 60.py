"""Write a Python program to create a set, add a new element to it, remove an element using remove(), and discard an element using discard()."""
fruits = {"apple", "banana", "cherry"}
fruits.add("mango")
print("After add:", fruits)
fruits.remove("apple")
print("After remove:", fruits)
fruits.discard("banana")
print("After discard:", fruits)