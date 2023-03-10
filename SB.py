print("Hello World")
# the program will store the email and password in a file
# the program will check if the email and password are correct
# the program will allow the user to sign in if the email and password are correct
# the program will not allow the user to sign in if the email and password are not correct
# the program will allow the user to create an account if the email is not already in the file
# the program will not allow the user to create an account if the email is already in the file

# import the modules
import os
import sys
import time


# create the file
def create_file():
    # create the file
    file = open("accounts.txt", "w")
    # close the file
    file.close()


# create the account
def create_account():
    # ask the user for their email
    email = input("Enter your email: ")
    # ask the user for their password
    password = input("Enter your password: ")
    # open the file
    file = open("accounts.txt", "a")
    # write the email and password to the file
    file.write(email + " " + password + "\n")
    # close the file
    file.close()
    # tell the user that their account has been created
    print("Your account has been created")


# sign in
def sign_in():
    # ask the user for their email
    email = input("Enter your email: ")
    # ask the user for their password
    password = input("Enter your password: ")
    # open the file
    file = open("accounts.txt", "r")
    # read the file
    lines = file.readlines()
    # close the file
    file.close()
    # check if the email and password are correct
    for line in lines:
        # split the line
        line = line.split()
        # check if the email and password are correct
        if email == line[0] and password == line[1]:
            # tell the user that they have signed in
            print("You have signed in")
            # exit the program
            sys.exit()
    # tell the user that the email or password is incorrect
    print("The email or password is incorrect")


# check if the file exists
if os.path.exists("accounts.txt"):
    # ask the user if they want to create an account or sign in
    choice = input("Do you want to create an account or sign in? ")
    # check if the user wants to create an account
    if choice == "create an account":
        # create the account
        create_account()
    # check if the user wants to sign in
    elif choice == "sign in":
        # sign in
        sign_in()
    # check if the user entered something else
    else:
        # tell the user that they entered something else
        print("You entered something else")
# check if the file does not exist
else:
    # create the file
    create_file()
    # ask the user if they want to create an account or sign in
    choice = input("Do you want to create an account or sign in? ")
    # check if the user wants to create an account
    if choice == "create an account":
        # create the account
        create_account()



url = "http://127.0.0.1:5000/api/v1/accounts"

payload = "{\n\t\"username\": \"test\",\n\t\"password\": \"test\"\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "d9f9f9f9-f9f9-f9f9-f9f9-f9f9f9f9f9f9"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

url = "http://127.0.0.1:5000/api/v1/accounts/test/university"

payload = "{\n\t\"university\": \"University of Florida\"\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "d9f9f9f9-f9f9-f9f9-f9f9-f9f9f9f9f9f9"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

url = "http://127.0.0.1:5000/api/v1/accounts/test/major"

payload = "{\n\t\"major\": \"Computer Science\"\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "d9f9f9f9-f9f9-f9f9-f9f9-f9f9f9f9f9f9"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

#!/user/bin/env python3
