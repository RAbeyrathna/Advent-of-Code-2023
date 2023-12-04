# Test case data
# schematic_list = [
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",
#     "..592....*",
#     "......755.",
#     "...$......",
#     ".664.598..",
# ]

# # Imports read data for challenge
schematic_list_file = open("day_3_input.txt", "r")
schematic_list = []
for string in schematic_list_file:
    string = string.strip()  # Remove /n from each string
    schematic_list.append(string)  # Updates lines with new string


special_characters = "!@#$%^&*()-+?_=,<>/"

i = 0
j = 0

total = 0
while i < len(schematic_list):
    current_num = ""
    current_num_si = 0
    current_num_ei = 0
    previousLine = schematic_list[i - 1]
    current_line = schematic_list[i]
    nextLine = schematic_list[i + 1] if (i != len(schematic_list) - 1) else None
    print(f"Iteration {i + 1}: Current list is {current_line}")
    for charid, char in enumerate(current_line):
        above_passed = False
        if char.isdigit() == True:
            print(f"{char} is a digit")
            current_num = current_num + char
        elif char.isdigit() == False and current_num != "":
            current_num_ei = charid
            current_num_si = current_num_ei - len(current_num) + 1
            print(
                f"Complete number is {current_num}. It's start index is {current_num_si} and it's final index is {current_num_ei}\n"
            )
            print(
                f"Starting check for special characters directly next to {current_num}"
            )
            if (schematic_list[i][current_num_si - 2]) in special_characters or (
                schematic_list[i][current_num_ei] in special_characters
            ):
                print(f"Special character detected. Adding number to total.\n")
                print(
                    f"Printing indexes: {schematic_list[i][current_num_si - 2]} {schematic_list[i][current_num_ei]}"
                )
                total += int(current_num)
                current_num = ""
                print(f"Total is now {total}\n\n")
                continue
            else:
                print("No special characters detected next to number\n")
                if i != 0:  # Don't check list above if on first list
                    print(
                        f"Starting check for special characters ajacent on line above {current_num}"
                    )
                    for index in range(current_num_si - 2, current_num_ei + 1):
                        if previousLine[index] in special_characters:
                            print(
                                f"Found special character {previousLine[index]} on line above. Adding number to total."
                            )
                            total += int(current_num)
                            current_num = ""
                            print(f"Total is now {total}\n\n")
                            # Skip iterating through line below if special character was found
                            above_passed = True
                            break
                        else:
                            print(
                                f"{previousLine[index]} is not a special chracter. Checking next character."
                            )
                            above_passed = False
                if (i != len(schematic_list) - 1) and (
                    above_passed == False
                ):  # Don't check list below if on final list and if above loop passed
                    print(
                        f"Starting check for special characters ajacent on line below {current_num}"
                    )
                    for index in range(current_num_si - 2, current_num_ei + 1):
                        if nextLine[index] in special_characters:
                            print(
                                f"Found special character {nextLine[index]} on line below. Adding number to total."
                            )
                            total += int(current_num)
                            current_num = ""
                            print(f"Total is now {total}\n\n")
                            break
                        else:
                            print(f"{nextLine[index]} is not a special chracter")
                    print(
                        f"No special characters found below {current_num} Continuing code..\n\n"
                    )
            current_num = ""
        else:
            # print(f"{char} is not a digit")
            pass
    i += 1
print(f"Code completed\n")
print(f"The total of all valid numbers is {total}")
