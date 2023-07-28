# Step 1: Create an empty dictionary to represent the game library
game_library = {}

# Step 2: Implement functions to manage the library
def add_game(title, genre, release_year):
    game_info = {
        "genre": genre,
        "release_year": release_year,
       
    }
    game_library[title] = game_info
    print(f"Game '{title}' added to the library.")

def remove_game(title):
    if title in game_library:
        del game_library[title]
        print(f"Game '{title}' removed from the library.")
    else:
        print(f"Game '{title}' not found in the library.")

def display_library():
    if not game_library:
        print("The library is empty.")
    else:
        print("Game Library:")
        for title, info in game_library.items():
            print(f"Title: {title}")
            print(f"Genre: {info['genre']}")
            print(f"Release Year: {info['release_year']}")
            
            print("-----------------------")

# Step 3: Test the functions
add_game("Pacman.", "Maze", 1980)
add_game("God of War", " Action-adventure game", 2018,)
add_game("Bayonetta", "Action-adventure game, Beat 'em up", 2022)
add_game("Resident Evil", " Survival horror,", 2019)

display_library()

remove_game("Pacman")

display_library()
