# types
name = "Ndungu"
print(type(name))

age = 24
print(type(age))

print("Your age is:" + str(age))

# Math
password = "123a655363"
print(len(password))

if len(password) < 8:
    print("Your password is too short")
else:
    print("The password is ok")


text = """
Python is easy to learn.
Python is powerful
Many people love python.
"""
print(text.count("Python"))

# Transfomations
price = "1234,56"
print(price.replace(",", "."))

messyNumber = "+49 (176 123-4567"
print(
    messyNumber.replace(
        "+",
        "",
    )
    .replace(" ", "")
    .replace("(", "")
    .replace(")", "")
    .replace(" ", "")
    .replace("-", "")
)
print(messyNumber)


first_name = "Ian"
second_name = "Wright"

full_name = first_name + " " + second_name
print(full_name)


name = "Sam"
age = 29
is_student = False

print(f"My name is {name} and I am {age} my student status is {is_student}")

print(f"2 + 3 = {2 + 3}")

stamp = "2026-09-20 14:30"
print(stamp.split(" "))

date_stamp = "2026-09-20"
print(date_stamp.split("-"))

print("ha " * 4)

# Indexes & slicing
text = "python"

# Extract the first charcter
print(text[0])
print(text[-6])

# Extract the last character
print(text[5])
print(text[-1])

# Extract h
print(text[3])

date = "2026-09-20"
# extract the year

print(date[0:4])
# or
print(date[:4])

# extract the month
print(date[5:7])

# data cleaning -- Removing spaces
# using strip() -- both sides lstrip()-- left side and rstrip()--- right side

text = " Engineering"
print(text.lstrip())

text = "Engineering ".rstrip()
print(text)

text = " Engineering ".strip()
print(text)

text = "###abc###".strip("#")
print(text)

text = "python PROGRAMMING"
print(text.lower())
print(text.upper())

phone = "+254-76628263"

print(phone.startswith("+254"))

email = "ndungu@gmail.com"
print(email.endswith("@gmail.com"))

print("@" in email)

phone1 = "+254-76628263"
phone2 = "245-6737463"
phone3 = "245-6653737"

print(phone1[phone1.find("-") + 1 :])
print(phone2[phone2.find("-") + 1 :])
print(phone3[phone3.find("-") + 1 :])

# Validation
country = "Kenya"
print(country.isalpha())

phone = "0983746463"
print(phone.isnumeric())
