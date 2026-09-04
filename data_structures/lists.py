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


#unpacking
person = ['Maria', 29, 'Data engineer','Kenya']

name, age, role, country = person
print(role)
print(name)

#order of values ids very important
person = ['Maria', 29, 'Data engineer','Kenya']

name, *details, country = person
print(name)
print(details)

#skipping items -- use the special character _
person = ['Maria', 29, 'Data engineer','Kenya']

name, _, role, _ = person
print(name)
print(role)
print("\n")
print("*" *20)

#explore and analyzing data.
#max() -- find extreme high
#min() -- find extreme low
#sum() -- Find total
#len() -- find length
#.count() -- How often -- returns how many times a value appears in the list
#.index -- where it appears

numbers = [1,5,2,4,3,5]
print("max:", max(numbers))
print("min:", min(numbers))
print("sum:", sum(numbers))
print("Length:", len(numbers))
print("Count:", numbers.count(5))
print("Index:", numbers.index(5))  # only the first appearance.