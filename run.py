def main():
    print("Welcome to Battleships!")
    grid_size = get_grid_size()
    print(f"Starting game with a {grid_size}x{grid_size} grid.")



if __name__ == "__main__":
    main()

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
