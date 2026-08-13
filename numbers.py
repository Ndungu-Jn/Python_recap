import math
import random

x = 5
y = 5.7
z = 2 + 3j

print(type(y))

x = "24"
print(type(x))
x = float(x)
print(x)
print(type(x))

print(2 + 3)
print(abs(2 - 10))

price = 35.546764736
print(round(price))
print(round(price, 2))

print(math.floor(price))
print(math.ceil(price))

print(math.trunc(price))

random_number = random.randint(1, 100)
print(random_number)
if random_number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Logic and operators
# control flow
# Conditional statements

print(True)
print(False)

email = ""
phone = "4646637346"
username = ""

# Allows registration
# if any field is filled
print(any([email, phone, username]))

# Allows registration
# if any field is filled
print(all([email, phone, username]))

# check if the system is under pressure
cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)

# Cheking user credentials before log in
email = True
password = False
print(email and password)


is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest) and not is_banned)


# conditional statements
score = 70
submitted_project = False
if score >= 90 and submitted_project:
    print("Excelent")
elif score >= 90:
    print("Good Job")
elif score >= 80:
    print("You tried")
elif score >= 70 or submitted_project:
    print("mmmmmhhh")
else:
    print("You really failed")


score = 80
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

# Inline if
print("A" if score >= 90 else "F")
grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)
