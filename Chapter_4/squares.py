squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    
print(squares)

# The same results can be acheived with less code.

squares = []
for value in range(1, 11):
    squares.append(value**2)
    
print(squares)

# Using list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)