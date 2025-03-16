# Problem 1 Create a program that takes a number as input and prints"Positive" if the number is greater than zero, and "Negative" if the number is less than zero.
def check_number(num):
    if num > 0:
        return 'Positive'
    else:
        return 'Zero'

number = float(input('Enter your number: '))
print(check_number(number))



# Problem 2 Create a program to determine whether a number entered by the user is even or odd.
def check_even_odd(num):
    if(num % 2  == 0 ):
        return 'Even Number'
    else:
        return 'Odd Number'
    

number = float(input('Enter the number: '))
print(check_even_odd(number))



# Problem 3 Create a program that takes a test score (0-100) as input and determines the grade according to the following criteria:
# • A: 80-100
# • B: 70-79
# • C: 60-69
# • D: 50-59
# • E: 0-49
def check_grades(score):
  if(80 <= score <= 100 ):
      return 'You got A grade'
  elif(70 <= score <= 79):
      return 'Your got B grade'
  elif(60 <= score <= 69):
      return 'Your got C grade'
  elif(50 <= score <= 59):
      return 'Your got D grade'
  elif(0 <= score <= 49):
      return 'You failed'
  else:
    return 'Invalid score! Please enter a number between 0 and 100.'
  
score_number = float(input('Enter the grade: '))
print(check_grades(score_number))



# Problem 4 Create a program that takes three numbers as input and displays the largest of the three numbers.
def check_largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return f'The largest number is {num1}'
    elif num2 >= num1 and num2 >= num3:
        return f'The largest number is {num2}'
    else:
        return f'The largest number is {num3}'


num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

print(check_largest_number(num1, num2, num3))



# Problem 5 Create a program to determine whether a year entered by the user is a leap year or not. A leap year is a year that is divisible by 4, but not divisible by 100, unless the year is divisible by 400
def is_leap_year(year):
    if(year % 2 == 0):
        return f"{year} is leap year"
    else:
        return f"{year} is NOT a Leap Year"
    
year = int(input('Enter a year: '))
print(is_leap_year(year))



# Problem 6 Create a simple calculator program that takes two numbers and one operator (+, -, *, /). The program must check the validity of the operator and handle division by zero.
def calculate(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    else:
        return "Error: Invalid operator. Please use +, -, *, or /."
    
    return result

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

print(f"Result: {calculate(num1, num2, operator)}")



# Problem 7 Create a program to determine a person's BMI (Body Mass Index) category based on the formula BMI = weight(kg) / height²(m). BMI categories:
# • Underweight: BMI < 18.5
# • Normal: 18.5 <= BMI < 25.0
# • Overweight: 25.0 <= BMI < 30.0
# • Obese: BMI >= 30.0
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25.0:
        category = "Normal"
    elif 25.0 <= bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

print(calculate_bmi(weight,height))



# Problem 8 Create a program to check if three entered numbers can form a triangle. If so, determine the type of triangle (equilateral, isosceles, or scalene).
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral Triangle"
    elif a == b or a == c or b == c:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

print(triangle_type(a,b,c))



# Problem 9 Create a program that simulates a simple login system. The program takes username and password input, then checks the following combinations:
# • Username: "admin", Password: "admin123" (admin access)
# • Username: "user", Password: "user123" (limited access)
# • Username: "guest", no password required (minimal access)
# • Other combinations (access denied)
def login(username,password):
    if username == "guest":
        return "Login successful! Minimal Access"
    elif username == "admin" and password == "admin123":
        return "Login successful! Admin Access "
    elif username == "user" and password == "user123":
        return "Login successful! Limited Access "
    else:
        return "Access Denied! Invalid username or password."

username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

print(login(username,password))



# Problem 10 Create a program for the rock-paper-scissors game. The program takes the player's choice as input, then the computer chooses randomly. The program determines the winner based on the rules:
# • Rock beats scissors
# • Scissors beats paper
# • Paper beats rock
# The program should also:
# • Handle invalid input
# • Display the computer's choice
# • Calculate and display the score after several rounds
# • Give the option to continue or end the game
import random
choices = ["rock", "paper", "scissors"]

def play():
    scores = {"player": 0, "computer": 0}

    while True:
        player = input("\nChoose rock, paper, or scissors (or 'quit' to exit): ").strip().lower()
        if player == "quit":
            break
        if player not in choices:
            print("Invalid choice, try again.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (player, computer) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
            print("You win!")
            scores["player"] += 1
        else:
            print("Computer wins!")
            scores["computer"] += 1

        print(f"Score: You {scores['player']} - {scores['computer']} Computer")

    print("Thanks for playing!")

play()
