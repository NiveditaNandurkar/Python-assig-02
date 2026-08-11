"""Write a Python program to remove all elements from a set using .clear(), while keeping the variable itself intact."""
colors = {"red", "green", "blue"}
colors.clear()
print("After clear:", colors, type(colors))
