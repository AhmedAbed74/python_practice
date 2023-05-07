# print("200 is great number")

# to_seconds = 24 * 60 * 60
# print("20 days are " + str(50) + " minutes")
# print(f"20 days are {20 * 24 * 60} minutes")
# print(f"20 days are {20 * calculation_of_unit} {name_of_unit}")

calculation_of_unit = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        print('all good~')
        return f"{num_of_days} days are {num_of_days * calculation_of_unit} {name_of_unit}"
    else:
        return "bad you enter invalid value"


user_input = input("Enter num of days and i will convert to hours\n")
user_input_number = int(user_input)

x = days_to_units(user_input_number)
print(x)