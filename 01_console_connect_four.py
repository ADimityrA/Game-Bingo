from copy import deepcopy


def process_field(start_row, chosen_column):
    for row in range(start_row, -1, -1):
        try:
            if field[row][chosen_column - 1] == 0:
                field[row][chosen_column - 1] = player_to_play
                return  # Exit the function if a valid index is found
        except IndexError:
            print("Invalid column. Please choose a different column.")
            chosen_column = chose_col()
            return process_field(row, chosen_column)  # Call the function recursively with the current row index


# Force the player to chose a column. He can't put empty field.
def chose_col():
    try:
        chosen_column = int(input(f"Player {player_to_play}, please chose a column: "))
        return chosen_column
    except ValueError:
        print("You have to chose a column!")
        return chose_col()


# Check if there are 4 consecutive occurrences in any diagonal.
def check_diagonals(matrix, searched_number):
    for x in range(len(matrix) - 3):
        for j in range(len(matrix[0]) - 3):
            # Check main diagonal
            if all(matrix[x + k][j + k] == searched_number for k in range(4)):
                return True
            # Check secondary diagonal
            if all(matrix[x + k][j + 3 - k] == searched_number for k in range(4)):
                return True
    return False


command = input("Do you wanna play BINGO (Yes/No): ")

while command == "Yes":
    width = int(input("Please enter the width of the play field (Number >= 4): "))
    height = int(input("Please enter the height of the play field (Number >= 4): "))

    field = [[0 for col in range(height)] for row in range(width)]

    number_of_players = int(input("Please chose number of players: "))

    player_to_play = 1
    bingo = False

    while not bingo:
        if player_to_play <= number_of_players:
            pass
        else:
            player_to_play = 1

        chosen_column = chose_col()

        process_field(width - 1, chosen_column)

        searched_bingo_number = player_to_play

        for row in field:
            for i in range(len(row) - 3):  # Loop trough elements in the row
                if all(row[i + j] == searched_bingo_number for j in range(4)):
                    # check if all consecutive elements starting from the current position (i) match the searched number
                    print(*field, sep="\n")
                    print(f"The winner is player {player_to_play}")
                    bingo = True
                    break
            if bingo:
                break

        # Transpose the matrix (swap rows and columns).
        transposed_field = list(map(list, zip(*deepcopy(field))))
        for col in transposed_field:
            for i in range(len(col) - 3):  # Loop trough elements in the column
                if all(col[i + j] == searched_bingo_number for j in range(4)):
                    # check if all consecutive elements starting from the current position (i) match the searched number
                    print(*field, sep="\n")
                    print(f"The winner is player {player_to_play}")
                    bingo = True
                    break
            if bingo:
                break

        # Call check_diagonals() to check occurrences in diagonals. Return -> True/False.
        if check_diagonals(field, searched_bingo_number):  # If returned result = True
            print(*field, sep="\n")
            print(f"The winner is player {player_to_play}")
            bingo = True

        print(*field, sep="\n")

        player_to_play += 1

    command = input("Do you want to resume playing BINGO (Yes/No): ")
