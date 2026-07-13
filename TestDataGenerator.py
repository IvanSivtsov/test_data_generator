#Input data

names = [
    "Ivan",
    "Anna",
    "Petr",
    "Maria",
    "Alex"
]

ages = [
    18,
    25,
    31,
    42,
    19
]


MAX_AGE = 120
MIN_AGE = 0
PREMIUM_AGE = 30
premium_users_counter = 0
basic_users_counter = 0
PREMIUM_STATUS = "Premium"
BASIC_STATUS = "Basic"
STATUS_UNKNOWN = "Unknown"

def check_account_status(age):
    if PREMIUM_AGE <= age < MAX_AGE:
        return PREMIUM_STATUS
    elif MIN_AGE < age < PREMIUM_AGE:
        return BASIC_STATUS
    else:
        return STATUS_UNKNOWN


def update_account_counter(status):
    global premium_users_counter, basic_users_counter

    if status == PREMIUM_STATUS:
        premium_users_counter += 1
    elif status == BASIC_STATUS:
        basic_users_counter += 1
    else:
        return


def print_user_info(name, age, account_index, status):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Account index: {account_index + 1}")
    print(f"Status: {status}\n")


def print_report(users_amount, premium_users_counter, basic_users_counter):
    print("\n----------REPORT----------\n"
          f"Total users: {users_amount}\n"
          f"Premium users: {premium_users_counter}\n"
          f"Basic users: {basic_users_counter}\n")

    # for each element
    # check status
    # increase account counter depends on status
    # print user info - index, name, age, account status
    # print report

users_amount = input("How many users do you want?\n")
if users_amount.isdigit():
    users_amount = int(users_amount)
    if users_amount <= len(names) and users_amount > 0:
        for i in range(users_amount):
            age = ages[i]
            name = names[i]
            status = check_account_status(age)
            update_account_counter(status)
            print_user_info(name, age, i, status)
        print_report(users_amount, premium_users_counter, basic_users_counter)
    else:
        print("Invalid number of users.")
else:
    print("Error: invalid input")
