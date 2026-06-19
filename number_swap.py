# Input three values
a = input("Enter value for a: ")
b = input("Enter value for b: ")
c = input("Enter value for c: ")

print(f"\nBefore swapping: a = {a}, b = {b}, c = {c}")

# Swapping logic: a gets b, b gets c, and c gets a
a, b, c = b, c, a

print(f"After swapping:  a = {a}, b = {b}, c = {c}")
