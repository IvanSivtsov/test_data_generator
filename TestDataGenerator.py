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
testdata_linebreak = "\n--------------------\n"

users_amount = input("How many users do you want?\n")
if users_amount.isdigit():
    users_amount = int(users_amount)
    if users_amount <= len(names) and users_amount > 0:
        for i in range(users_amount):
            age = ages[i]
            name = names[i]
            print(f"User #{i + 1}")
            print(f"Name: {name}")
            print(f"Age: {age}")
            if PREMIUM_AGE <= age < MAX_AGE:
                user_status = "Premium"
                premium_users_counter += 1
            elif MIN_AGE < age < PREMIUM_AGE:
                user_status = "Basic"
                basic_users_counter += 1
            else:
                user_status = "Unknown"
                print("Age is not valid")
            print(f"Status: {user_status}")
            print(testdata_linebreak)
        print("\n----------REPORT----------\n"
            f"Total users: {users_amount}\n"
            f"Premium users: {premium_users_counter}\n"
            f"Basic users: {basic_users_counter}\n")
    else:
        print("Age is not valid")
else:
    print("Error: invalid input")
