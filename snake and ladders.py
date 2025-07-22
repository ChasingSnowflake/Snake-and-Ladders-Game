import random

# Create the board with snakes and ladders
board = [i for i in range(101)]

# Snakes: The key is the snake's head, and the value is the tail
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}

# Ladders: The key is the bottom of the ladder, and the value is the top
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Function to simulate the dice roll
def roll_dice():
    return random.randint(1, 6)

# Function to move the player
def move_player(player_name, position):
    dice_roll = roll_dice()
    print(f"{player_name} rolled: {dice_roll}")

    position += dice_roll
    if position > 100:
        print(f"Position {position} is beyond 100, staying at {position - dice_roll}")
        return position - dice_roll

    if position in snakes:
        print(f"Oops! A snake at {position}! {player_name} goes down to {snakes[position]}")
        position = snakes[position]

    elif position in ladders:
        print(f"Yay! A ladder at {position}! {player_name} climbs up to {ladders[position]}")
        position = ladders[position]

    return position

# Main game loop for two players
def play_game():
    player1_position = 1  # Player 1 starts at position 1
    player2_position = 1  # Player 2 starts at position 1
    turn = 1  # 1 for Player 1, 2 for Player 2
    
    while player1_position < 100 and player2_position < 100:
        if turn == 1:
            input("Player 1, press Enter to roll the dice...")
            player1_position = move_player("Player 1", player1_position)
            print(f"Player 1 is now at position {player1_position}\n")
            if player1_position == 100:
                print("Player 1 wins! Congratulations!")
                break
            turn = 2  # Switch turn to Player 2
        else:
            input("Player 2, press Enter to roll the dice...")
            player2_position = move_player("Player 2", player2_position)
            print(f"Player 2 is now at position {player2_position}\n")
            if player2_position == 100:
                print("Player 2 wins! Congratulations!")
                break
            turn = 1  # Switch turn to Player 1

# Start the game
if __name__ == "__main__":
    play_game()
