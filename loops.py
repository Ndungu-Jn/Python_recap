# Repeat a block of code over and over until a condition is met
# for loops and the While loops
# for loop -- go through a group of items one by one to do something for each item
print("*" * 10)
print("Round: 1")
print("Round: 2")
print("Round: 3")
print("Round: 4")
print("Round: 5")

print("*" * 10)
for i in (1, 2, 3, 4, 5):
    print(f"Round: {i}")

# end
print("*" * 10)
items = (1, 2, 3, 4, "Hi", "You")
for item in items:
    print(f"Round: {item}")

print("*" * 10)

# start
for number in range(1, 6):
    print(f"Round: {number}")
print("*" * 10)

# step
for number in range(1, 11, 2):
    print(f"Round: {number}")

print("*" * 10)
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
    print(f"Current total is: {total}")
print(f"Final total is: {total}\n")

print("*" * 10)

# first clean up then manipulate
files = [" Report.CSV ", "Data.csv ", " final.TXT"]
for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print(f"Process {file}")
