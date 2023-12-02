# calibration_string_file = open("day_1_input.txt", "r")
# calibration_strings = []
# for string in calibration_string_file:
#     string = string.strip()  # Remove /n from each string
#     calibration_strings.append(string)  # Updates lines with new string

initial_calibration_strings = [
    "two1nine",
    # "eightwothree",
    # "abcone2threexyz",
    # "xtwone3four",
    # "4nineeightseven2",
    "zoneight234",
    # "7pqrstsixteen",
    # "eighthree",
    "sevenine",
]

upd_calibration_strings = []


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


int_list_numbers = (
    "0123456789"  # Digits from 1 - 9 in string format to compare within the loop
)


for calibration_string in initial_calibration_strings:
    print(f"Current string: {calibration_string}")
    working_str = ""
    append_str = ""
    for char in calibration_string:
        print(f"Current character: {char}")
        if char in int_list_numbers:
            append_str = append_str + char
            print(f"Character is number, appending: {char} \n")
            continue
        else:
            working_str = working_str + char
            print(
                f"Character is not a number. Updating working string to {working_str}"
            )
            for str_num in str_list_number:
                if str_num in working_str:
                    print(
                        f"Current working string is in list ({working_str}) Appending {str_num} \n"
                    )
                    append_str = append_str + str_list_number[str_num]
                    working_str = working_str[-1]
                else:
                    continue
    upd_calibration_strings.append(append_str)
print(upd_calibration_strings)

# total = 0  # Initializes inital total
# i = 0

# for calibration_string in calibration_strings:  # Checks each string provided
#     i += 1
#     print(f"Iteration: {i} - Current calibration string is {calibration_string}")
#     calibration_value = ""  # Initalizes empty string to be appended
#     for char in calibration_string:  # Checks each individual string character
#         if char in int_list_numbers:
#             calibration_value = (
#                 calibration_value + char
#             )  # Concatenates the current character if it is present in the list_numbers variable
#         else:
#             continue
#     print(f"Unadjusted calibration value: {calibration_value}")
#     if (
#         len(calibration_value) != 2
#     ):  # Takes only the first and last digits if string is larger than 2 digits
#         first_char = calibration_value[0]
#         last_char = calibration_value[-1]
#         calibration_value = first_char + last_char
#         print("Calibration value has been adjusted")
#     else:
#         print("Current value does not need adjusting. Skipping")
#     print(f"Calibration value is: {calibration_value}")
#     total += int(calibration_value)
#     print(f"Current total is {total} \n")
# print(f"Sum of all calibration values is {total}")
