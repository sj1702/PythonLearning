#Solution1

import random
# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
# Main game loop
while True:
    # Get user's choice
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue
    # Generate computer's choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    # Print choices
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    # Determine the winner and print result
    result = determine_winner(player_choice, computer_choice)
    print(result)
    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break



#Solution 2

import random
# Dictionary to map choices to their corresponding numbers
choices_map = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors'
}
# Ask the user for their choice
user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
# Generate a random choice for the computer
computer_choice_num = random.randint(1, 3)
computer_choice = choices_map[computer_choice_num]
# Display the choices
print(f"\nYour choice: {user_choice}")
print(f"Computer's choice: {computer_choice}\n")
# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
     (user_choice == 'Paper' and computer_choice == 'Rock') or \
     (user_choice == 'Scissors' and computer_choice == 'Paper'):
    print("Congratulations! You win!")
else:
    print("Sorry, you lose. Better luck next time!")



#Solution 3

import random
# Ask the user for their choice
user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
# Generate a random choice for the computer
computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
# Display the choices
print(f"\nYour choice: {user_choice}")
print(f"Computer's choice: {computer_choice}\n")
# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
else:
    if user_choice == 'Rock':
        if computer_choice == 'Scissors':
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose. Better luck next time!")
    elif user_choice == 'Paper':
        if computer_choice == 'Rock':
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose. Better luck next time!")
    elif user_choice == 'Scissors':
        if computer_choice == 'Paper':
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose. Better luck next time!")



#Solution 4

import random
# Dictionary to determine the winner
winner_map = {
    ('Rock', 'Rock'): 'Tie',
    ('Rock', 'Paper'): 'Computer',
    ('Rock', 'Scissors'): 'User',
    ('Paper', 'Rock'): 'User',
    ('Paper', 'Paper'): 'Tie',
    ('Paper', 'Scissors'): 'Computer',
    ('Scissors', 'Rock'): 'Computer',
    ('Scissors', 'Paper'): 'User',
    ('Scissors', 'Scissors'): 'Tie'
}
# Ask the user for their choice
user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
# Generate a random choice for the computer
computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
# Display the choices
print(f"\nYour choice: {user_choice}")
print(f"Computer's choice: {computer_choice}\n")
# Determine the winner
result = winner_map[(user_choice, computer_choice)]
if result == 'Tie':
    print("It's a tie!")
else:
    print(f"Congratulations! {result} wins!")



#Solution 5

import random
# List of tuples to determine the winner
winner_rules = [
    ('Rock', 'Scissors'),  # Rock beats Scissors
    ('Scissors', 'Paper'), # Scissors beats Paper
    ('Paper', 'Rock')      # Paper beats Rock
]
# Ask the user for their choice
user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
# Generate a random choice for the computer
computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
# Display the choices
print(f"\nYour choice: {user_choice}")
print(f"Computer's choice: {computer_choice}\n")
# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice, computer_choice) in winner_rules:
    print("Congratulations! You win!")
else:
    print("Sorry, you lose. Better luck next time!"