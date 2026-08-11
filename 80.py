"""Write a Python program to determine how many elements are in a set without using the built-in len() function."""
animals = {"cat", "dog", "bird", "fish"}
count = 0
for a in animals:
    count += 1
print("Count without len():", count)
