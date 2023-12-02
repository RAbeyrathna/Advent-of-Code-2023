calibration_string_file = open("day_1_input.txt", "r")
calibration_strings = []
for string in calibration_string_file:
    string = string.strip()  # Remove /n from each string
    calibration_strings.append(string)  # Updates lines with new string


list_numbers = (
    "0123456789"  # Digits from 1 - 9 in string format to compare within the loop
)
total = 0  # Initializes inital total
i = 0

for calibration_string in calibration_strings:  # Checks each string provided
    i += 1
    print(f"Iteration: {i} - Current calibration string is {calibration_string}")
    calibration_value = ""  # Initalizes empty string to be appended
    for char in calibration_string:  # Checks each individual string character
        if char in list_numbers:
            calibration_value = (
                calibration_value + char
            )  # Concatenates the current character if it is present in the list_numbers variable
        else:
            continue
    print(f"Unadjusted calibration value: {calibration_value}")
    if (
        len(calibration_value) != 2
    ):  # Takes only the first and last digits if string is larger than 2 digits
        first_char = calibration_value[0]
        last_char = calibration_value[-1]
        calibration_value = first_char + last_char
        print("Calibration value has been adjusted")
    else:
        print("Current value does not need adjusting. Skipping")
    print(f"Calibration value is: {calibration_value}")
    total += int(calibration_value)
    print(f"Current total is {total} \n")
print(f"Sum of all calibration values is {total}")
