calibration_string_file = open("day_1_input.txt", "r")
initial_calibration_strings = []
for string in calibration_string_file:
    string = string.strip()  # Remove /n from each string
    initial_calibration_strings.append(string)  # Updates lines with new string


# Test case data
# initial_calibration_strings = [
#     "two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen",
# ]


upd_calibration_strings = []


# Dictionary to compare when converting string number to integers
str_list_number = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

int_list_numbers = "0123456789"  # Digits from 1 - 9 in string format to compare within calculation loop


# Function to convert string numbers into integers and append to new list
def calstring_to_int():
    print("Converting all strings into integer format \n")
    for calibration_string in initial_calibration_strings:
        print(f"\nSelected string: {calibration_string}")
        working_str = ""
        append_str = ""
        for char in calibration_string:
            print(f"Current character: {char}")
            # Compares each character and appends to string if it is an integer
            if char in int_list_numbers:
                append_str = append_str + char
                print(f"Character is number, appending: {char}")
                continue
            # if not an integer, check if the characters build into number as string
            else:
                working_str = working_str + char
                print(
                    f"Character is not a number. Updating working string to {working_str}"
                )
                # checks if updated string is in the str_list_number dictionary
                for str_num in str_list_number:
                    if str_num in working_str:
                        print(f"Found and appending string integer {str_num}.")
                        append_str = append_str + str_list_number[str_num]
                        # Keep last character of the string in case it is used for the next number
                        working_str = working_str[-1]

                    else:
                        continue
        # Append completed string to new list
        upd_calibration_strings.append(append_str)

    print("\nCompleted string conversion. \n")


# Function to convert calibration strings into calibration values and calculate sum
def calstring_sum():
    total = 0  # Initializes inital total
    i = 0  # Used to track current iteration
    print("Calculating calibration strings \n")
    for calibration_string in upd_calibration_strings:  # Checks each string provided
        i += 1
        print(f"Iteration: {i} - Current calibration string is {calibration_string}")
        calibration_value = ""  # Initalizes empty string to be appended
        for char in calibration_string:  # Checks each individual string character
            if char in int_list_numbers:
                calibration_value = (
                    calibration_value + char
                )  # Concatenates the current character if it is present in the list_numbers variable
            else:
                continue
        if len(calibration_value) != 2:
            # Takes only the first and last digits if string is larger than 2 digits
            first_char = calibration_value[0]
            last_char = calibration_value[-1]
            calibration_value = first_char + last_char
            print(f"Calibration value has been adjusted to {calibration_value}")
        else:
            print("Current value does not need adjusting. Skipping")
        total += int(calibration_value)
        print(f"Current total is {total} \n")
    print(f"Sum of all calibration values is {total}")


calstring_to_int()
calstring_sum()
