# Register
# - first names,last names, password, email
# - generate the user account number

# login
# - Account number & Password

# bank Operations
# Initializing the system
import random

database = {} #dictionary

def init():

    isValidOptionSelected = False
    print("Welcome to Bank PHP")

    while isValidOptionSelected == False:

        have_Account = int(input("Do you have account with us : 1. (yes) 2. (no)\n"))
        if have_Account == 1:
            isValidOptionSelected = True

            login()

        elif have_Account == 2:
            isValidOptionSelected = True

            register()

        else:
            print("You have selected invalid option")
            init()


def login():
    print('********Please login in your account***********')

    accountNumberFromUser  = int(input("What is your account Number?\n"))
    password = input("What is your password? \n")

    for account_Number, userDetails in Database.items():
        if account_Number == accountNumberFromUser:
            if userDetails[3] == password:
                bankOperation(userDetails)

    print('Invalid account or password')
    login()



def register():

    print("************Kindly register with our bank*************")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create your password? \n")

    account_Number = generationAccountNumber()

    database[account_Number] = [ first_name, last_name, email, password ]

    print("Your Account has been created")

    login()

def bankOperation():
    print("Bank Operations")

def withdrawalOperational():
    print("withdrawal")

def depositOperational():
    print("Deposits Operations")

def generationAccountNumber():

    print("account number generator")
    return random.randrange(0000000000,9999999999)


### ACTUAL BANKING SYSTEM

init()