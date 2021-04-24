# Register
# - first names,last names, password, email
# - generate the user account

# login
# - Account number email and Password

# bank Operations
# Initializing the system
import random
import validation
import database
from getpass import getpass


def init():

    print("Welcome to Bank PHP")
    have_account = int(input("Do you have account with us : 1. (yes) 2. (no)\n"))
    if have_account == 1:
        login()

    elif have_account == 2:
        register()

    else:
        print("You have selected invalid option")
        init()

def login():
    print("**********'Please login in your account'**********")

    account_number_from_user = input("What is your account number?\n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password? \n")

        user = database.authenticated_user(account_number_from_user,password);

        if user:
            bank_operation(user)

        #for account_number,user_details in database.items():
            #if account_number == account_number_from_user :
                #if user_details[3] == password:
                    #bank_operation(user_details)

        print('Invalid account or password')
        login()
    else:
        print("Account number invalid: Check that your have upto 10 digits and only numbers")
        init()

def register():

    print("************Kindly register with our bank*************")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create your password? \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name,last_name,email,password)

    if is_user_created:

        print("your account has been created ")
        print("=============== =================== ============")
        print("Your account number is : %d" % account_number)
        print("Make sure you keep it sale and don't share your password with anyone")
        print("============= =================== =============")

        login()

    else:
        print("something went wrong register the account again ")

        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do ? (1)  Cash deposit (2) Cash withdrawal (3) LogOut (4) Exit \n"))

    if selected_option == 1:

        deposit_operational()

    elif selected_option == 2:

        withdrawal_operational()

    elif selected_option == 3:

        logout()
    elif selected_option == 4:
        exit()
    else:
        print(" Invalid Option selected")

        bank_operation(user)


def withdrawal_operational():
    print("print Withdrawal")

def deposit_operational():
    print("print deposit")

def generation_account_number():

    print("account number generator")
    return random.randrange(0000000000,9999999999)

def set_current_balance(user_details):
    user_details[4] = balance

def get_current_balance(user_details):
    return user_details[4]

## ACTUAL BANKING SYSTEM

def logout():
    login()

init()