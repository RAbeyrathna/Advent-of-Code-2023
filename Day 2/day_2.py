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
total = 0


# Extract game data to a dictionary, using each game as a seperate dictionary and rounds as lists
for game in raw_game_data:
    # dictionary_key = int(game[5])
    dictionary_key = dictionary_i
    print(dictionary_key)
    dictionary_i += 1
    upd_game_dict[dictionary_key] = game[8::].split(";")


print(upd_game_dict)

while i <= len(upd_game_dict):
    j = 1
    gamePossible = True
    print("----")
    print(f"Game {i}")
    for round in upd_game_dict[i]:
        print(f"\nRound {j}")
        current_round = round.split(",")
        for draw in current_round:
            current_draw = draw.strip()
            if ":" in current_draw:
                current_draw = current_draw.replace(":", "")
            if "red" in current_draw:
                current_draw_val = int(current_draw.replace("red", "").strip())
                print(f"Drew {current_draw_val} red cubes")
                if current_draw_val > red:
                    gamePossible = False
                    print(
                        f"Drew {current_draw} which is higher than total possible red {red} cubes"
                    )
                    break
            elif "green" in current_draw:
                current_draw_val = int(current_draw.replace("green", "").strip())
                print(f"Drew {current_draw_val} green cubes")
                if current_draw_val > green:
                    gamePossible = False
                    print(
                        f"Drew {current_draw} which is higher than total possible green {green} cubes"
                    )
                    break
            else:
                current_draw_val = int(current_draw.replace("blue", "").strip())
                print(f"Drew {current_draw_val} blue cubes")
                if current_draw_val > blue:
                    gamePossible = False
                    print(
                        f"Drew {current_draw} which is higher than total possible blue {blue} cubes"
                    )
                    break
        j += 1
        if gamePossible == False:
            print(f"\nGame was not possible. Moving to next game.")
            break
    if gamePossible == True:
        print(f"\nGame was possible. Adding game ID {i} to total.")
        total += i
        print(f"Total is now {total}")
    print("\n")
    i += 1

print(f"Completed all games. Total of all game ID's is {total}")
