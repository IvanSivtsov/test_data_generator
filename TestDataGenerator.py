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
premium_users_counter = 0
basic_users_counter = 0
testdata_linebreak = "\n--------------------\n"


for i in range(len(names)):
    age = ages[i]
    name = names[i]
    print(f"User #{i + 1}")
    print(f"Name: {names[i]}")
    print(f"Age: {ages[i]}")
    if  30 <= age < MAX_AGE:
        user_status = "Premium"
        premium_users_counter += 1
    elif MIN_AGE < age < 30:
        user_status = "Basic"
        basic_users_counter += 1
    else:
        user_status = "Unknown"
        print("Age is not valid")
    print(f"Status: {user_status}")
    print(testdata_linebreak)

print("\n----------REPORT----------\n"
        f"Total users: {len(names)}\n"
        f"Premium users: {premium_users_counter}\n"
        f"Basic users: {basic_users_counter}\n")