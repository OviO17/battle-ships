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


def main():
    print("Welcome to Battleships!")
    grid_size = get_grid_size()
    grid = create_grid(grid_size)
    display_grid(grid)


if __name__ == "__main__":
    main()

