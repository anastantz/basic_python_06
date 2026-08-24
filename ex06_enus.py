# Program that reads a number and displays its double, triple, and square root

number = float(input("Enter a number: "))
double = number * 2
triple = number * 3
square_root = number ** (1/2)

print(f"Analyzing the number {number}:")
print(f"The double is {double}.")
print(f"The triple is {triple}.")
print(f"The square root is {square_root:.2f}.")