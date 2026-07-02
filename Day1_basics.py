#Week 1 Day 1 - Python Fundamentals
#My first program from IIT Jodhpur BS/BSC in Applied AI

print("Hello from IIT Jodhpur!")
print("I'm starting Semester 1!")
print("="*50)

#Variables and data types
name = "Priyanshu shah"  #String
age = 17           #Integer
height = 6.2         #Float
is_student = True   #Boolean
city = "Kotdwar"    # string

#Print variables
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Sutdent: {is_student}")
print(f"City: {city}")

#Data type checking
print("\n" + "=" * 50)
print("Data Types:")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print(f"Type of is_student: {type(is_student)}")
print(f"Type of city: {type(city)}")

#String operations
print("\n" + "=" * 50)
message = "Learning Python at IIT Jodhpur"
print(f"Origninal: {message}")
print(f"Uppercase: {message.upper()}")
print(f"Lowercase: {message.lower()}")
print(f"Length: {len(message)}")

#Simple math
print("\n" + "=" * 50)
x = 30
y = 40
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} % {y} = {x % y}")   #Modulo ( remainder)
print(f"{x} ** {y} = {x ** y}") #Power

print("\n✨ First program completed! ✨")
