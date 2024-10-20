import random

# Set the number of rounds
NUM_ROUNDS: int = 5

def get_user_guess() -> str:
    """
    Gets a valid input from the user ('higher' or 'lower').
    """
    guess: str = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
    while guess not in ['higher', 'lower']:
        guess = input("Please enter either 'higher' or 'lower': ").strip().lower()
    return guess

def play_round(round_num: int, score: int) -> int:
    """
    Plays a single round of the game.
    :param round_num: Current round number
    :param score: Current score of the player
    :return: Updated score after the round
    """
    print(f"Round {round_num}")
    
    # Generate random numbers for the user and the computer
    user_number: int = random.randint(1, 100)
    computer_number: int = random.randint(1, 100)
    
    # Show the user's number
    print(f"Your number is {user_number}")
    
    # Get the user's guess
    guess: str = get_user_guess()
    
    # Check if the guess is correct
    if (guess == 'higher' and user_number > computer_number) or (guess == 'lower' and user_number < computer_number):
        print("You were right!", end=" ")
        score += 1
    else:
        print("Aww, that's incorrect.", end=" ")
    
    # Reveal the computer's number
    print(f"The computer's number was {computer_number}")
    
    # Show current score
    print(f"Your score is now {score}\n")
    
    return score

def end_game(score: int) -> None:
    """
    Displays the end game message based on the player's score.
    :param score: Final score of the player
    """
    print("Thanks for playing!")
    print(f"Your final score is {score} out of {NUM_ROUNDS}")
    
    # Conditional ending messages
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

def high_low_game() -> None:
    """
    Main function to run the High-Low game.
    """
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score: int = 0
    
    # Play multiple rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        score = play_round(round_num, score)
    
    # End the game and show the result
    end_game(score)

# Run the game
if __name__ == "__main__":
    high_low_game()
