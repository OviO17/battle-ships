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


def create_grid(size):
    return [["~" for _ in range(size)] for _ in range(size)]


def display_grid(grid):
    for row in grid:
        print(" ".join(row))


def place_ship(grid_size):
    row = random.randint(0, grid_size - 1)
    col = random.randint(0, grid_size - 2)

    ship_positions = [
        (row, col),
        (row, col + 1)
    ]

    return ship_positions


def get_player_guess(grid_size, previous_guesses):
    while True:
        try:
            row = int(input("Guess row: "))
            col = int(input("Guess column: "))

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
        print(" Hit!")
    else:
        print("Miss.")

def is_ship_sunk(ship_positions, hits):
    return len(hits) == len(ship_positions)


def main():
    print("Welcome to Battleships!")

    grid_size = get_grid_size()
    grid = create_grid(grid_size)

    ship = place_ship(grid_size)
    player_guesses = []
    ship_hits = []

    while True:
        display_grid(grid)

        guess = get_player_guess(grid_size, player_guesses)
        player_guesses.append(guess)

        hit = check_hit(guess, ship)
        update_grid(grid, guess, hit)
        display_result(hit)

        if hit:
            ship_hits.append(guess)

        if is_ship_sunk(ship, ship_hits):
            print("🎉 You sank the battleship! You win!")
            display_grid(grid)
            break


if __name__ == "__main__":
    main()
