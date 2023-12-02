i = 1
dictionary_i = 1

# raw_game_data = [
#     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
# ]


game_data_file = open("day_2_input.txt", "r")
raw_game_data = []
for string in game_data_file:
    string = string.strip()  # Remove /n from each string
    raw_game_data.append(string)  # Updates lines with new string


upd_game_dict = {}

red = 12
green = 13
blue = 14

highest_red = 0
highest_green = 0
highest_blue = 0
cube_power_sum = 0
total = 0


# Extract game data to a dictionary, using each game as a seperate dictionary and rounds as lists
for game in raw_game_data:
    dictionary_key = dictionary_i
    print(dictionary_key)
    dictionary_i += 1
    upd_game_dict[dictionary_key] = game[8::].split(";")


print(upd_game_dict)

while i <= len(upd_game_dict):
    j = 1
    gamePossible = True
    highest_red = 0
    highest_green = 0
    highest_blue = 0
    print("----")
    print(f"Game {i}")
    for round in upd_game_dict[i]:
        print(f"\nRound {j}")
        print(f"Current highest red: {highest_red}")
        print(f"Current highest green: {highest_green}")
        print(f"Current highest blue: {highest_blue}")
        current_round = round.split(",")
        for draw in current_round:
            current_draw = draw.strip()
            if ":" in current_draw:
                current_draw = current_draw.replace(":", "")
            if "red" in current_draw:
                current_draw_val = int(current_draw.replace("red", "").strip())
                print(f"Drew {current_draw_val} red cubes")
                if current_draw_val > highest_red:
                    highest_red = current_draw_val
            elif "green" in current_draw:
                current_draw_val = int(current_draw.replace("green", "").strip())
                print(f"Drew {current_draw_val} green cubes")
                if current_draw_val > highest_green:
                    highest_green = current_draw_val
            else:
                current_draw_val = int(current_draw.replace("blue", "").strip())
                print(f"Drew {current_draw_val} blue cubes")
                if current_draw_val > highest_blue:
                    highest_blue = current_draw_val
        j += 1
    print(f"\nCalculating cube power:")
    cube_power = highest_red * highest_blue * highest_green
    cube_power_sum += cube_power
    print(f"Highest red that round was: {highest_red}")
    print(f"Highest green that round was: {highest_green}")
    print(f"Highest blue that round was: {highest_blue}")
    print(
        f"\nCurrent cube power: {cube_power} Current cube power sum: {cube_power_sum}"
    )
    print("\n")
    i += 1

print(f"Completed all games. Total of all game ID's is {total}")
