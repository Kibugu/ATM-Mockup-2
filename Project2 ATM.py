# Register
# - first names,last names, password, email
# - generate the user account

# login
# - Account number email and Password

# bank Operations
# Initializing the system
import random

database = {} #dictionary

def init():


    print("WELCOME TO BANK OF KENYA")

    haveAccount = int(input("Do you have account with us : 1. (yes) 2. (no)\n"))
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        init() # this is to make sure that if the application fails it goes into the application all over again.


def login():
    print("**********'Please login in your account'**********")


    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation('userDetails')
    print('Invalid account or password')

    login()

def register():

    print("************Kindly register with our bank*************")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create your password? \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("your account has been created ")
    print("=============== =================== ============")
    print("Your account number is : %d" % accountNumber)
    print("Make sure you keep it sale and don't share your password with anyone")
    print("============= =================== =============")

    login()



def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    isSelectedOptionValid = False

    while isSelectedOptionValid == False:

        SelectedOption = int(input("What would you like to do ? (1)  Cash deposit (2) Cash withdrawal (3) LogOut (4) Exit \n"))

        if (SelectedOption == 1):
            isSelectedOptionValid = True
            depositOperational()
        elif (SelectedOption == 2):
            isSelectedOptionValid = True
            withdrawalOperational()
        elif (SelectedOption == 3):
            isSelectedOptionValid = True
            logout()
        elif (SelectedOption == 4):
            isSelectedOptionValid = True
            exit()
        else:
            print(" Invalid Option selected")

            bankOperation(user)


def withdrawalOperational():
    selectwithdrawalAmount = int(input('How much would you like to withdraw? \n'))
    selectContinue = int(input("Do you want to continue with other bank operations?  press (1) or (2) logout\n"))
    if (selectContinue ==1):
        login()
    elif (selectContinue ==2):
        print('Thank you for banking with us please remove you Card and money.')
        logout()

    else:
        exit()



def depositOperational():
    print("**************** Print deposit ********************")
    depositOperational = int(input('How much would you like to Deposit? \n'))
    selectContinue = int(input("Do you want to continue with other  operations?  press (1) or (2) logout\n"))
    if (selectContinue == 1):
        login()
    elif (selectContinue == 2):
        print('Thank you for banking with us remove your Card.')
        logout()

    else:
        exit()

def generationAccountNumber():
    print("account number generator")
    return random.randrange(0000000000,9999999999)

def logout():
    login()
### ACTUAL BANKING SYSTEM

init()