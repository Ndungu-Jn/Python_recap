# Repeat a block of code over and over until a condition is met
# for loops and the While loops
# for loop -- go through a group of items one by one to do something for each item
"""
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

print("*" * 10)
for i in range(1, 11):
    print(f"7 x {i} = {7*i}")

print("*" * 10)

for i in range(6):
    i += 1
    print("*" * i)
print("\n")
# Break -- stops the loop immediately

names = ["John", "Pesh", "", "Emma"]
for name in names:
    if name == "":
        print("Empty string detected")
        break
    print(f"Name = {name}")
print("*" * 10)


# Continue -- skips one loop cycle without stopping the loop
names = ["John", "Pesh", "", "Emma"]
for name in names:
    if name == "":
        print("Empty string detected")
        continue
    print(f"Name = {name}")
print("*" * 10)

# Loop through a list of days and print the working days, skipping the weekends

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekends = [
    "Saturday",
    "Sunday",
]
for day in days:
    if day in weekends:
        continue
    print(f"Day: {day}")

names = ["Kamara", "Tuba", "Nice", "Modern"]
for name in names:
    if name == None:
        print("Found the missing name")
        break
else:
    print("All names are available")


# Check if all my data is in csv
files = ["data1.csv", "data2.pdf", "data3.csv"]
print(files)
for file in files:
    if not file.endswith(".csv"):
        print(f"{file} is not a .csv")
        break
else:
    print("Checks out")

# NB: else is only used with a break. it cannot work with a continue.

# Nested for loop -- a loop inside a loop
for x in (1, 2, 3):
    for y in (1, 2):
        print(x, y)


for x in range(3):  # Outer loop
    for y in range(2):  # Inner loop
        for z in range(2):
            print(f"({x},{y},{z})")

# used mostly when combining data
colors = ["red", "blue", "green"]
sizes = ["L", "M", "S"]

for color in colors:
    for size in sizes:
        print(f"({color} - {size})")

# also used to go through layers -- that is drilling into hirachy
years = [2026, 2027]
months = ["Jan", "Feb"]
days = range(1, 28)

for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")

# WHILE LOOP -- Repeats a block of code - over and over as long as the condition is true
# the while condition -- until the condition is met
# the wile true -- runs forever until a break is introduced.

# counter
i = 1  # initialization of the while loop -- define the initial value
while i < 4:  # the while loop condition
    print(i)
    i += 1  # an update mechanism.

print("*" * 10)
count = 1
while count <= 6:
    print(count)
    count += 2

answer = ""
while answer != "yes":
    answer = input("Do you agree? (yes/no):").lower()
print("Thank you")
"""

# TEST
attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no):").lower()
    if answer == "yes":
        print("Glad we are on the same page")
        break
    attempts += 1
if answer != "yes":
    print("3 strikes. You're out!")
else:
    print("Thank you")
