# Test case data
# schematic_list = [
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598..",
# ]

# schematic_list = [
#     "311...672...34...391.....591......828.......................738....................223....803..472..................................714.840.",
#     ".......*...........*.....*...........*........631%...703.......*..12....652.................*.$............368.769*148.................*....",
#     "....411...........2....837.121........511.745...........*.48.422.@.........@.............311........887......*................457........595",
#     "........*328...............&..........................144.*...................138............48.......*......682.........@...*.......777....",
# ]

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
    print(f"Iteration {i + 1}: Current list is {schematic_list[i]}")
    for charid, char in enumerate(schematic_list[i]):
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
                # print(
                #     f"Printing indexes: {test_list[i][current_num_si - 2]} {test_list[i][current_num_ei]}"
                # )
                if i != 0:  # Don't check list above if on first list
                    print(
                        f"Starting check for special characters ajacent on line above {current_num}"
                    )
                    for index in range(current_num_si - 2, current_num_ei + 1):
                        if schematic_list[i - 1][index] in special_characters:
                            print(
                                f"Found special character {schematic_list[i - 1][index]} on line above. Adding number to total."
                            )
                            total += int(current_num)
                            current_num = ""
                            print(f"Total is now {total}\n\n")
                            above_passed = True
                            break
                        else:
                            print(
                                f"{schematic_list[i - 1][index]} is not a special chracter. Checking next character."
                            )
                            above_passed = False
                if (i != len(schematic_list) - 1) and (
                    above_passed == False
                ):  # Don't check list below if on final list and if above loop passed
                    print(
                        f"Starting check for special characters ajacent on line below {current_num}"
                    )
                    for index in range(current_num_si - 2, current_num_ei + 1):
                        if schematic_list[i + 1][index] in special_characters:
                            print(
                                f"Found special character {schematic_list[i + 1][index]} on line below. Adding number to total."
                            )
                            total += int(current_num)
                            current_num = ""
                            print(f"Total is now {total}\n\n")
                            break
                        else:
                            print(
                                f"{schematic_list[i + 1][index]} is not a special chracter"
                            )
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
