
# Week 1 Day 2 - Operators & control flow
# Learning: Comparison, Logical Operators, If-Else Statements)

print("=" * 50)
print("COMPARISON OPERATORS")
print("=" * 50)

x = 4
y = 10

print(f"x = {x}, y ={y}\n")
print(f"x == y: {x == y}")  #Equal to
print(f"x != y: {x != y}")  #Not equal to
print(f"x > y: {x > y}")    #Greater than
print(f"x < y: {x < y}")    #Less than
print(f"x >= y: {x>= y}")  #Greater than or equal to
print(f"x <= y: {x <= y}")  #Less than or equal to

print("\n" + "=" * 50)
print("LOGICAL OPERATORS")
print("=" * 50)

age = 20
score = 85

print(f"age = {age}, score = {score}\n")
print(f"age >= 18 and score >= 80: {age >= 18  and score >= 80}")
print(f"age < 18 or score >= 80: {age < 18 or score >= 80}")
print(f"not (score >= 80): {not (score >= 80)}")

print("\n" + "=" * 50)
print("IF-ELSE STATEMENTS")
print("=" * 50)

#Example 1: Simple if
print("\nExample 1: Simple if")
if 5>3:
    print("5 is greater than 3")

print("\nExample 2: If-Else")
temperature = 25
if temperature > 30:
    print("It's hot today!")
else:
    print("It's cool today!")

#Example 3: If-Elif-Else
print("\nExample 3: If-Elif-Else (Weather)")
weather = "sunny"

if weather == "sunny":
    print("Go to the beach!")
elif weather == "rainy":
    print("stay indoors!")
elif weather == "cold":
    print("Wear a jacket!")
else:
    print("check the weather forecast!")

#Example 4: Nested If
print("\nExample 4: Nested If")
age = 22
has_license = True
if age>=18:
    print("You can drive")
    if has_license:
        print("You have a license!")
    else:
        print("You need a license to drive!")
else:
    print("You are not eligible to drive!")

#Example 5: Real-world(login system)
print("\n" + "=" * 50)
print("Example 5: Real-world(login system)")
print("=" * 50)

username = "admin"
password = "password123"
entered_username = "admin"
entered_password = "password123"

if entered_username == username and entered_password == password:
    print("✅Login successful!")
elif entered_username != username:
    print("❌Incorrect username!")
else:
    print("❌Incorrect password!")

print("\n" + "=" * 50)
print("✨ Control Flow Examples Complete!")
print("=" * 50)