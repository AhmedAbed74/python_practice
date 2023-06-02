# print("200 is great number")

# to_seconds = 24 * 60 * 60
# print("20 days are " + str(50) + " minutes")
# print(f"20 days are {20 * 24 * 60} minutes")
# print(f"20 days are {20 * calculation_of_unit} {name_of_unit}")

calculation_of_unit = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_of_unit} {name_of_unit}"


def validate():
    try:
            x = int(num_of_day)
            if x > 0:
                y = days_to_units(x)
                print(y)
            elif x == 0:
                print(" you enter 0")
            else:
                print(" you enter negative number")
    except ValueError:
        print(" you don't place a number")


user_input = ""
while user_input != "exit":
    user_input = input("Enter num of days and i will convert to hours, Enter exit to exit \n")
    for num_of_day in user_input.split():
        validate()
