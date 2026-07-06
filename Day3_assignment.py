# Week 1 Day 3 Assignment - Loop Challenges
# Complete all 5 challenges

print("=" * 50)
print("LOOP CHALLENGES")
print("=" * 50)

# CHALLENGE 1: Print numbers 1 to 20
print("=" * 50)
print("CHALLENGE 1: Print numbers 1 to 20")
print("-" * 50)

for i in range(1,21):
    print(i, end=" ")

# CHALLENGE 2: Sum of numbers 1 to 100
print("\n" + "=" * 50)
print("CHALLENGE 2: Sum of numbers 1 to 100")
print("-" * 50)

total = 0
for i in range(101):
    total = total + i
print(f"Sum of numbers 1 to 100 is: {total}")

# CHALLENGE 3: Print only odd numbers from 1 to 20
print("=" * 50)
print("CHALLENGE 3: Print only odd numbers from 1 to 20")
print("-" * 50)
for i in range(1,21,2):
    print(i,end=" ")

# Alternate Method of CHALLENGE 3: Print only odd numbers from 1 to 20
print("\n" + "=" * 50)
print("ALTERNATE METHOD OF CHALLENGE 3: Print only odd numbers from 1 to 20")
print("-" * 50)
for i in range(1,21):
    if i%2 != 0:
        print(i, end=" ")

# CHALLENGE 4: Multiplication Table for 7
print("\n" + "=" * 50)
print("CHALLENGE 4: Multiplication Table for 7")
print("-" * 50)
for i in range(1,11):
    result = 7 * i
    print(f"7 x {i} = {result}")

# CHALLENGE 5: Find number in list
print("\n" + "=" * 50)
print("CHALLENGE 5: Find number in list")
print("-" * 50)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
searching = 50

for num in numbers:
    if num == searching:
        print(f"✅ Found {searching} in the list!")
        break
else:
    print(f"❌ {searching} not found")

print("\n" + "=" * 50)
print("✨ All challenges completed!")
print("=" * 50)


