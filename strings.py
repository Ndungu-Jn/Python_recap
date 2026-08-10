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
print(messyNumber.replace("+", "",).replace(" ", "").replace("(", "").replace(")",
                                                                              "").replace(" ", "").replace("-", ""))
print(messyNumber)


first_name = "Ian"
second_name = "Wright"

full_name = first_name + " " + second_name
print(full_name)


name = "Sam"
age = 29
is_student = False

print(f"My name is {name} and I am {age} my student status is {is_student}")
