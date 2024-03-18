# 3rd Text based RPG
# player health = 100
# enemy_health = random.randint (50,100)
# import random
# while
# damage = random.randint(10,25)
# enemy_health+= damage

#Solution 1

import random
def text_based_rpg():
    player_health = 100
    enemy_health = random.randint(50, 100)

    print("Welcome to the Text-Based RPG!")
    print("Player Health:", player_health)
    print("Enemy Health:", enemy_health)

    while player_health > 0 and enemy_health > 0:
        input("\nPress Enter to attack!")

        player_damage = random.randint(10, 25)
        enemy_damage = random.randint(5, 20)

        enemy_health -= player_damage
        player_health -= enemy_damage

        print("\nPlayer attacks and deals", player_damage, "damage!")
        print("Enemy attacks and deals", enemy_damage, "damage!")

        print("\nPlayer Health:", player_health)
        print("Enemy Health:", enemy_health)

    if player_health <= 0:
        print("\nYou have been defeated! Game Over.")
    else:
        print("\nCongratulations! You have defeated the enemy!")

if __name__ == "__main__":
    text_based_rpg()



#Solution 2
import random

def text_based_rpg():
    player_health = 100
    enemy_health = random.randint(50, 100)

    while True:
        print("\n1. Attack Enemy\n2. Exit RPG")
        choice = input("Enter your choice:\n")

        if choice == "1":
            player_damage = random.randint(10, 25)
            enemy_damage = random.randint(5, 20)
            enemy_health -= player_damage
            player_health -= enemy_damage

            print("\nPlayer attacks and deals", player_damage, "damage!")
            print("Enemy attacks and deals", enemy_damage, "damage!")

            print("\nPlayer Health:", player_health)
            print("Enemy Health:", enemy_health)

            if player_health <= 0:
                print("\nYou have been defeated! Game Over.")
                break
            elif enemy_health <= 0:
                print("\nCongratulations! You have defeated the enemy!")
                break

        elif choice == "2":
            print("Exiting RPG. Goodbye!")
            break
        else:
            print("Invalid Input")

text_based_rpg()
print("You are out of RPG")
consent = input("Want to access the RPG again? Y/N\n").upper()
if consent == "Y":
    text_based_rpg()
else:
    print("Thanks for playing..!!")



#Solution 3
# Pseudo-random number generator function
def pseudo_random(seed):
    # Simple mathematical operations to generate pseudo-random numbers
    seed = (seed * 1103515245 + 12345) % 2 ** 31
    return seed
# Initialize player and enemy health
player_health = 100
enemy_seed = 123  # Seed for enemy health generation
enemy_health = enemy_seed % 51 + 50  # Generate enemy health between 50 and 100
while True:
    print("\n1. Attack Enemy\n2. Exit RPG")
    choice = input("Enter your choice:\n")
    if choice == "1":
        # Generate pseudo-random numbers for player and enemy damage
        player_damage_seed = pseudo_random(enemy_seed)
        enemy_damage_seed = pseudo_random(player_damage_seed)
        player_damage = player_damage_seed % 16 + 10  # Player damage between 10 and 25
        enemy_damage = enemy_damage_seed % 16 + 5  # Enemy damage between 5 and 20
        enemy_health -= player_damage
        player_health -= enemy_damage
        print("\nPlayer attacks and deals", player_damage, "damage!")
        print("Enemy attacks and deals", enemy_damage, "damage!")
        print("\nPlayer Health:", player_health)
        print("Enemy Health:", enemy_health)
        if player_health <= 0:
            print("\nYou have been defeated! Game Over.")
            break
        elif enemy_health <= 0:
            print("\nCongratulations! You have defeated the enemy!")
            break
    elif choice == "2":
        print("Exiting RPG. Goodbye!")
        break
    else:
        print("Invalid Input")
print("You are out of RPG")
consent = input("Want to access the RPG again? Y/N\n").upper()
if consent == "Y":
    # Reset enemy seed for replay
    enemy_seed += 1
    enemy_health = enemy_seed % 51 + 50
    player_health = 100
    while True:
        print("\n1. Attack Enemy\n2. Exit RPG")
        choice = input("Enter your choice:\n")
        if choice == "1":
            player_damage_seed = pseudo_random(enemy_seed)
            enemy_damage_seed = pseudo_random(player_damage_seed)
            player_damage = player_damage_seed % 16 + 10
            enemy_damage = enemy_damage_seed % 16 + 5
            enemy_health -= player_damage
            player_health -= enemy_damage
            print("\nPlayer attacks and deals", player_damage, "damage!")
            print("Enemy attacks and deals", enemy_damage, "damage!")
            print("\nPlayer Health:", player_health)
            print("Enemy Health:", enemy_health)
            if player_health <= 0:
                print("\nYou have been defeated! Game Over.")
                break
            elif enemy_health <= 0:
                print("\nCongratulations! You have defeated the enemy!")
                break
        elif choice == "2":
            print("Exiting RPG. Goodbye!")
            break
        else:
            print("Invalid Input")
else:
    print("Thanks for playing..!!")



#Solution 4
import time
def generate_random_seed():
    # Using current system time to generate a pseudo-random seed
    seed = int(time.time() * 1000)
    return seed % 100
def text_based_rpg():
    player_health = 100
    enemy_health = generate_random_seed() % 51 + 50  # Generate a random number between 50 and 100 for enemy health
    while True:
        print("\n1. Attack Enemy\n2. Exit RPG")
        choice = input("Enter your choice:\n")
        if choice == "1":
            player_damage = generate_random_seed() % 16 + 10  # Generate a random number between 10 and 25 for player damage
            enemy_damage = generate_random_seed() % 16 + 5    # Generate a random number between 5 and 20 for enemy damage
            enemy_health -= player_damage
            player_health -= enemy_damage
            print("\nPlayer attacks and deals", player_damage, "damage!")
            print("Enemy attacks and deals", enemy_damage, "damage!")
            print("\nPlayer Health:", player_health)
            print("Enemy Health:", enemy_health)
            if player_health <= 0:
                print("\nYou have been defeated! Game Over.")
                break
            elif enemy_health <= 0:
                print("\nCongratulations! You have defeated the enemy!")
                break
        elif choice == "2":
            print("Exiting RPG. Goodbye!")
            break
        else:
            print("Invalid Input")
text_based_rpg()
print("You are out of RPG")
consent = input("Want to access the RPG again? Y/N\n").upper()
if consent == "Y":
    text_based_rpg()
else:
    print("Thanks for playing..!!")
In this version, the generate_random_seed() fu