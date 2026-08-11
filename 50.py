"""Given a list of integers, iterate through the items and count how many are even and how many are odd."""
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for n in numbers:
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count