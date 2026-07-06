# Week 1 Day 3 - Loops & Iteration
# Learning: For loops, While loops, Break/Continue, Nested loops, Loop-else

#STEP 1: FOR LOOPS
print("=" * 50)
print("FOR LOOPS - THE BASICS")
print("=" * 50)

#1. Basic for loop
print("\n1. Simple For Loop (range 0-4):")        
for i in range(5):          #range(5) means 0,1,2,3,4 (Not including 5)
    print(f"Number: {i}")   #The loop repeats 5 times

#2. For loop with custom range
print("\n2. For Loop with Custom Range (1-5):")
for i in range(1,6):      #Start at 1, go upto 5 (not including 6)
    print(f"Number: {i}")

#3. For loop with step
print("\n3. For Loop with Step (Even numbers):")
for i in range(0,10,2): # Start 0, go to 10, step by 2
    print(f"Even number: {i}")

#4. For loop with step (Backwards)
print("\n4. For Loop Backwards (Countdown):")
for i in range(5,0,-1):    # Start 5, go down to 1, step -1
    print(f"Countdown: {i}")

#5. For loop over a list
print("\n5. For Loop Over a List:")
fruits = ["Apple", "Banana", "Orange", "Mango"]
for fruit in fruits:
    print(f" I like {fruit}")

#6. For loop with index
print("\n6. For Loop with Index (enumerate):")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

#7. Multiplication table using for loop
print("\n7. Multiplication Table (5)")
for i in range(1,11):
    result = 5 * i
    print(f"5 x {i} = {result}")

#8. Sum using for loop
print("\n8. Sum Numbers 1 to 10:")
total = 0
for i in range(1,11):
    total = total + i
print(f"Sum of Numbers 1 to 10 is: {total}")

#9. Nested for loop (loop inside loop)
print("\n9. Nested For Loop (Multiplication Table 3x3):")
for i in range(1,4):
    for j in range(1,4):
        print(f"{i}x{j}={i*j}", end=" ")  #end prevents newline
    print()  #New line after inner loop completes

print("\n" + "=" * 50)

#STEP 2: WHILE LOOPS
print("\n" + "=" * 50)
print("WHILE LOOPS")
print("=" * 50)

#1. Simple while loop
print("\n1. Simple while loop:")
count = 0
while count<5:
    print(f"Count: {count}")
    count = count + 1           # IMPORTANT: Must increment, or infinite loop!

#2. while with user input (simulated)
print("\n2. While Loop - ATM Withdrawal (Simulated):")
balance = 1000
attempts = 0
while balance > 0 and attempts < 3:
    withdrawal = 100
    if balance >= withdrawal:
        balance = balance - withdrawal
        attempts = attempts + 1 
        print(f"Withdrawal : {withdrawal}, Remaining : {balance}")
        
    else:
        print(f"Insufficient Balance: {balance}")
        break   #Exits loop immediately

print(f"Final balance: {balance}")

#3. while loop - password verification
print("\n3. While Loop - Password Check:")
password = "PriyanshuandAnjali#12"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_password = "PriyanshuandAnjali#12" #In real we use input()
    if entered_password == password:
        print(f"✅Password is correct")
        break

    else:
        attempts = attempts + 1
        print(f"❌Wrong Password. Attempt remaining: {max_attempts - attempts}")
        

if attempts == max_attempts:
    print(f"❌ Account locked!")

#4. While True with break
print("\n4. While True - Repeat until Condition Mer: ")
number = 0
while True:
    number = number + 1
    print(f"Number: {number}")
    if number >= 5:
        print("Reached 5, breaking out!")
        break  #Exit the loop

print("\n"+"="*50)

#STEP 3: LOOP CONTROL - BREAK & CONTINUE
print("=" * 50)
print("LOOP CONTROL - BREAK & CONTINUE")
print("=" * 50)

#1. BREAK example
print("\n1. Break - Exit Loop Early:")
for i in range(10):
    if i == 5:
        print("Found 5, breaking!")
        break
    print(f"Number: {i}")

#2. CONTINUE example
print("\n2. Continue - Skip This Iteration:")
for i in range(10):
    if i == 5:
        print("Skipping 5")
        continue
    print(f"Number: {i}")

#3. Break with search
print("\n3. Real Example - Find Item in List:")
shopping_list = ["Apple", "Banana", "Orange", "Mango", "Grapes"]
searching_for = "Orange"
for fruit in shopping_list:
    if fruit == searching_for:
        print(f"✅{searching_for} founded in Shopping_list")
        break
else:
    print(f"❌{searching_for} not founded in Shopping_list")

#4. Continue to skip even numbers
print("\n4. Continue - Skip Even Numbers:")
print("Odd numbers from 1 to 10:")
for i in range(1,11):
    if i%2==0:
        continue
    print(i, end=" ")

print("\n" + "="*50)

#STEP 4: NESTED LOOPS
print("=" * 50)
print("NESTED LOOPS - PATTERNS")
print("=" * 50)

# Pattern 1: Triangle
print("\n1. Triangle Pattern:")
for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 2: 2D Grid
print("\n2. 2D Grid (3×3):")
for i in range(3):
    for j in range(3):
        print(f"({i},{j})",end=" ")
    print()

# Pattern 3: Multiplication Table
print("\n3. Multiplication Table (5×5):")
for i in range(1,6):
    for j in range(1,6):
        print(f"{i*j:2}", end=" ")
    print()

# Pattern 4: Diamond (Advanced)
print("\n4. Diamond Pattern:")
for i in range(1, 5):
    for j in range(5-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()

print("\n" + "=" * 50)

#STEP 5: LOOP-ELSE
print("=" * 50)
print("LOOP-ELSE (ADVANCED)")
print("=" * 50)

# Example 1: Loop completes normally
print("\n1. Loop Completes Normally (No Break):")
for i in range(5):
    print(f"Number: {i}")
else:
    print("✅ Loop completed successfully!")

# Example 2: Loop breaks (else doesn't run)
print("\n2. Loop Breaks (Else Doesn't Run):")
for i in range(10):
    if i == 5:
        print(f"Found {i}, breaking!")
        break
    print(f"Number: {i}")
else:
    print("This won't print because we broke!")

## Real example: Search in list
print("\n3. Real Example - Search:")
numbers = [1, 3, 5, 7, 9]
searching = 6

for num in numbers:
    if num == searching:
        print(f"✅ Found {searching}!")
        break
else:
    print(f"❌ {searching} not found in list")

print("\n" + "=" * 50)