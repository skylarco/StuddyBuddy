import random

def login_generator(first_name, last_name):
    login = first_name[0] + last_name[:7]
    return login

def password_generator(login):
    password = ""
    for i in range(0, len(login)):
        password += str(random.randint(0, 9))
    return password

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    login = login_generator(first_name, last_name)
    password = password_generator(login)
    print("Your login is: " + login)
    print("Your password is: " + password)
import json
filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

main()
print("Hello, user!")
import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

print('What is ' + str(num1) + ' + ' + str(num2) + '?')
answer = input()

if answer == str(num1 + num2):
    print('Correct!')
else:
    print('Nope! The answer is ' + str(num1 + num2))
import random

# generate two random numbers
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

# prompt the user to enter an answer
answer = eval(input("What is " + str(num1) + " + " + str(num2) + "? "))

# display result
print(num1, "+", num2, "=", answer, "is", num1 + num2 == answer)
import random

# generate two random numbers
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

# prompt the user to enter an answer
answer = eval(input("What is " + str(num1) + " + " + str(num2) + "? "))

# display result
print(num1, "+", num2, "=", answer, "is", num1 + num2 == answer)
import random

# generate two random numbers
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

# prompt the user to enter an answer
answer = eval(input("What is " + str(num1) + " + " + str(num2) + "? "))

# display result
print(num1, "+", num2, "=", answer, "is", num1 + num2 == answer)
import random

# generate two random numbers
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

# prompt the user to enter an answer
answer = eval(input("What is " + str(num1) + " + " + str(num2) + "? "))

import random

# generate two random numbers
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

# prompt the user to enter an answer
answer = eval(input("What is " + str(num1) + " + " + str(num2) + "? "))

# display result
print(num1, "+", num2, "=", answer, "is", num1 + num2 == answer)
import random

# generate two random numbers
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

# prompt the user to enter an answer
answer = eval(input("What is " + str(num1) + " + " + str(num2) + "? "))

# display result
print(num1, "+", num2, "=", answer, "is", num1 + num2 == answer)
import random

# generate two random numbers
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

# prompt the user to enter an answer
answer = eval(input("What is " + str(num1) + " + " + str(num2) + "? "))

# display result
print(num1, "+", num2, "=", answer, "is", num1 + num2 == answer)
print("Hello, StudyBuddy here. Do you need help?")

answer = input()

if answer == "yes":
    print("I can help you with that.")
else:
    print("okay, let's continue.")
print("Do you want to take a quiz?")
answer = input()

while answer == "yes":
    print("Here is a quiz:")
    print("What is the capital of Alaska?")
    print("1. Melbourne")
    print("2. Anchorage")
    print("3. Juneau")

    answer = input("Type the number of your answer: ")

    if answer == "3":
        print("That is correct!")
    else:
        print("Sorry, that is incorrect.")

print("Awesome! Let's do another quiz.")
answer = input()
import random

# generate two random numbers
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

# prompt the user to enter an answer
answer = eval(input("What is " + str(num1) + " + " + str(num2) + "? "))

print("You're doing a great job!")
print("Rate your experience from 1 to 10")

rating = input()

if rating == "10":
    print("Thank you for your feedback")
elif rating == "9":
    print("Thank you for your feedback")
elif rating == "8":
    print("Thank you for your feedback")
elif rating == "7":
    print("Thank you for your feedback")
elif rating == "6":
    print("Thank you for your feedback")
elif rating == "5":
    print("Thank you for your feedback")
elif rating == "4":
    print("Thank you for your feedback")
elif rating == "3":
    print("Thank you for your feedback")
elif rating == "2":
    print("Thank you for your feedback")
elif rating == "1":
    print("Thank you for your feedback")
else:
    print("Invalid input")
while True:
    print("Would you like to continue?")
    answer = input()
    if answer == "no":
        break
    if answer == "yes":
        print("Okay, let's do another quiz.")
        break
import random

# generate two random numbers
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

# prompt the user to enter an answer
answer = eval(input("What is " + str(num1) + " + " + str(num2) + "? "))

# display result
print(num1, "+", num2, "=", answer, "is", num1 + num2 == answer)
import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

print('What is ' + str(num1) + ' + ' + str(num2) + '?')
answer = input()

if answer == str(num1 + num2):
    print('Correct!')
else:
    print('Nope! The answer is ' + str(num1 + num2))
import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

print('What is ' + str(num1) + ' + ' + str(num2) + '?')
answer = input()

if answer == str(num1 + num2):
    print('Correct!')
else:
    print('Nope! The answer is ' + str(num1 + num2))




