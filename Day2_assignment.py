# Week 1 Day 2 Assignment - Student Eligibility Checker
#Requirements: Your program should check if a student is eligible for a scholarship based on:
#1. Age must be 18 or older
#2. GPA must be 3.5 or higher
#3. Must be a full-time student


# Data of student
name = "Priyanshu"
age = 18
gpa = 3.5
is_full_time = True

#Scholarship eligibility check
print("\n" + "=" * 70)
print("SCHOLARSHIP ELIGIBILITY CHECKER")
print("=" * 70)

print(f"StudentName: {name}")
print(f"Age: {age}")
print(f"GPA: {gpa}")
print(f"Full-time student: {is_full_time}")
      
print("\n" + "=" * 70)
print("ElIGIBILITY CHECK")
print("=" * 70)

age_eligible = age>=18
gpa_eligible = gpa>=3.5
full_time_eligible = is_full_time

print(f"Age requirement (>=18): {age_eligible}")
print(f"GPA requirement (>=3.5): {gpa_eligible}")
print(f"full Time Student Requriement: {full_time_eligible}\n")


#Check each condition
if age_eligible and gpa_eligible and full_time_eligible:
    print(f"CONGRATULATIONS {name}! You are eligible for the scholarsip")

else:
    print(f"Sorry {name}! You are not eligible for the scholarsip. Here is the reason")
    if age<18:
        print(f"Your Age must be 18 or older")
    if gpa<3.5:
        print(f"Your GPA must be 3.5 or higher")
    if is_full_time == False:
        print("Your are not full time student")

print("=" * 70)