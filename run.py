import random


def get_grid_size():
    while True:
        try:
            size = int(input("Choose grid size (minimum 5): "))
            if size < 5:
                print("Grid size must be at least 5.")
            else:
                return size
        except ValueError:
            print("Please enter a valid number.")

 data_str = input("Enter your data here:\n")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

def create_grid(size):
    return [["~" for _ in range(size)] for _ in range(size)]


def display_grid(grid):
    size = len(grid)
    header = "  " + " ".join(str(i) for i in range(size))
    print(header)

    for index, row in enumerate(grid):
        print(f"{index} " + " ".join(row))


def place_ship(grid_size):
    row = random.randint(0, grid_size - 1)
    col = random.randint(0, grid_size - 2)

    ship_positions = [
        (row, col),
        (row, col + 1)
    ]

    return ship_positions


def get_player_guess(grid_size, previous_guesses):
    """
    Get a valid guess from the player.
    Ensures the guess is within bounds and not repeated.
    """
    while True:
        try:
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))

            if row < 0 or row >= grid_size or col < 0 or col >= grid_size:
                print("That guess is off the grid.")
            elif (row, col) in previous_guesses:
                print("You already guessed that location.")
            else:
                return (row, col)

        except ValueError:
            print("Please enter valid numbers.")



def check_hit(guess, ship_positions):
    return guess in ship_positions


def update_grid(grid, guess, hit):
    row, col = guess
    if hit:
        grid[row][col] = "X"
    else:
        grid[row][col] = "O"


def display_result(hit):
    if hit:
        print("Direct hit!")
    else:
        print("Missed! Nothing there.")


def is_ship_sunk(ship_positions, hits):
    return len(hits) == len(ship_positions)


def main():
    """
    Main game loop for Battleships.
    """
    print("Welcome to Battleships!")
    print("Try to sink the computer's ship.")
    print("Enter coordinates using numbers starting from 0.\n")

    grid_size = get_grid_size()
    grid = create_grid(grid_size)

    ship = place_ship(grid_size)
    player_guesses = []
    ship_hits = []
    turn_count = 0

    while True:
        display_grid(grid)

        guess = get_player_guess(grid_size, player_guesses)
        player_guesses.append(guess)
        turn_count += 1

        print(f"\nTurn {turn_count}")

        hit = check_hit(guess, ship)
        update_grid(grid, guess, hit)
        display_result(hit)

        if hit:
            ship_hits.append(guess)

        if is_ship_sunk(ship, ship_hits):
            print(f"\nYou sank the battleship! You win in {turn_count} turns!")
            display_grid(grid)
            break

if __name__ == "__main__":
    main()
