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

database = {
5722401131: [ 'James', 'Gikunju', 'james.kibugu@gmail.com', '1234' ]
} #dictionary

def init():

    is_valid_option_selected = False
    print("Welcome to Bank PHP")

    while is_valid_option_selected == False:

        have_account = int(input("Do you have account with us : 1. (yes) 2. (no)\n"))
        if have_account == 1:
            is_valid_option_selected = True
            login()
        elif have_account == 2:
            is_valid_option_selected = True
            register()
        else:
            print("You have selected invalid option")


def login():
    print("**********'Please login in your account'**********")

    is_login_successful = False

    while is_login_successful == False:

        account_number_from_user = int(input("What is your account number? \n"))
        password = input("What is your password? \n")

        for account_number,userDetails in database.items():
            if account_number == account_number_from_user :
                if userDetails[3] == password:
                    is_login_successful = True
        print('Welcome to our Bank services')
    bank_operation('user')

def register():

    print("************Kindly register with our bank*************")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create your password? \n")

    account_number = generation_account_number()

    #database[account_number] = [ first_name, last_name, email, password ]

    print("your account has been created ")
    print("=============== =================== ============")
    print("Your account number is : %d" % account_number)
    print("Make sure you keep it sale and don't share your password with anyone")
    print("============= =================== =============")

    login()



def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    is_selected_option_valid = False

    while not is_selected_option_valid:

        selected_option = int(input("What would you like to do ? (1)  Cash deposit (2) Cash withdrawal (3) LogOut (4) Exit \n"))

        if selected_option == 1:
            is_selected_option_valid = True
            deposit_operational()
        elif selected_option == 2:
            is_selected_option_valid = True
            withdrawal_operational()
        elif selected_option == 3:
            is_selected_option_valid = True
            login()
        elif selected_option == 4:
            is_selected_option_valid = True
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


### ACTUAL BANKING SYSTEM

init()