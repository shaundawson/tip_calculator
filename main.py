print("Welcome to the tip calculator")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person would pay: ${final_amount}")



# Day 2: Data Types, Numbers, Operations, Type Conversion, F-Strings

# num_char = len(input("What is your name?\n"))
# print(type(num_char))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# a = float(123)
# print(type(a))
# print(70 + float("100.5"))
# print(str(70) + str(100))

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# two_digit_number = input("Type a two digit number: ")
# first_num = int(two_digit_number[0])
# second_num= int(two_digit_number[1])
# print(first_num + second_num)

# PEMDAS - Parenthesis (), Exponents **, Multiplication *, Division/, Addition +, Subtraction - 
# print(3 * (3 + 3) / 3 -3) 


# BMI Calculator
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# conv_height = float(height)
# conv_weight = float(weight)
# bmi = conv_weight/(conv_height **2)
# whole_bmi = int(bmi)
# print(whole_bmi)

# f-string
# score = 0
# height = 1.8
# isWinning = True
# print(f"your score is {score}, your height is {height}, you are winning is: {isWinning}")


# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# age = input("What is your current age?\n")
# yrs_left = 90 - int(age)
# months = yrs_left * 12
# weeks = yrs_left * 52
# days = yrs_left * 365
# message = (f"You have {days} days, {weeks} weeks, and {months} months left.")
# print(message)

# print("Welcome to the tip calculator.")
# total_bill = input("What was the total bill? \n$")
# bill_amount = float(total_bill)
# tip_percent = input("What percentage tip would you like to give? 10, 12, or 15\n")
# tip_amount = float(tip_percent)
# get_dec = tip_amount *0.01
# add_tip = bill_amount * get_dec 
# bill_with_tip = float(total_bill) + add_tip
# num_people = input("how many people to split the bill?\n")
# total_each = bill_with_tip / int(num_people)
# convert_tip = (round(total_each,2))
# print(f"Each person should pay: ${convert_tip}")