"""Write a Python program to remove a specific key from a dictionary, retrieve all key-value pairs, and check whether a given key exists."""
car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
# Remove a specific key 
del car["color"]
print("After removing key:", car)
# Retrieve all key-value pairs
print("All key-value pairs:",
 car.items())
# Check whether a given key exists
print("Does 'model' exist?", "model" in car)
