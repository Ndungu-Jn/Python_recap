# creating list
empty = []
letters = ["a", "b", "c"]
numbers = [1, 2, 3, 4]
mixed = [1, "a", True, None]
print(letters)
print(numbers)
print(mixed)

# using the function list() -- needs a sequence
empty = list("Python")
print(empty)

some_numbers = list(range(5))
print(some_numbers)

# Nested lists
# matrix = [["a", "b", "c", ["d", "e", "f"]]]
# print(matrix)

print("*" * 30)
# Reading and accessing the values in the list
lst = ["a", "b", "c"]
# Access only one item
# indexing - getting the position

print(lst[0])
print(lst[-1])

# Accessing things in the matrix. and entire list inside or just one thing.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Get the whole matrix
print(matrix)
# Get the last row
print(matrix[2])
# getting the last number in the last row
print(matrix[-1][2])
