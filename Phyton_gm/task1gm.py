import random
import time

def start_game():
    print("Привіт")
    print("You find yourself at the entrance of a mysterious forest.")
    print("You can choose your path:")
    print("1. Take the well-trodden path.")
    print("2. Venture into the dense undergrowth.")

    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        follow_path()
    elif choice == '2':
        explore_undergrowth()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        start_game()

def follow_path():
    print("You follow the well-trodden path deeper into the forest.")
    print("As you walk, you come across a fork in the road.")
    print("1. Go left.")
    print("2. Go right.")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        print("You encounter a friendly fairy who guides you safely out of the forest.")
        print("Congratulations, you've completed the adventure!")
    elif choice == '2':
        print("You stumble upon a hidden treasure chest!")
        print("You are now rich beyond your wildest dreams.")
        print("Congratulations, you've completed the adventure!")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        follow_path()

def explore_undergrowth():
    print("You venture into the dense undergrowth, and it starts to get dark.")
    print("Suddenly, you hear a growl behind you. A wild beast is approaching!")
    print("1. Try to climb a tree to escape.")
    print("2. Attempt to confront the beast.")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        print("You successfully climb a tree and wait for the beast to pass by.")
        print("Once it's safe, you climb down and continue your journey.")
        continue_journey()
    elif choice == '2':
        print("You bravely confront the beast, but it's too strong.")
        print("Unfortunately, you are defeated. Game over.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        explore_undergrowth()

def continue_journey():
    print("As you continue your journey, you encounter a talking rabbit.")
    print("The rabbit offers you a choice:")
    print("1. Follow the rabbit to a hidden meadow.")
    print("2. Ignore the rabbit and continue on your path.")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        print("You follow the rabbit to a beautiful meadow filled with magical creatures.")
        print("You've found a place of wonder and tranquility.")
        print("Congratulations, you've completed the adventure!")
    elif choice == '2':
        print("You continue on your path, and the forest becomes even more mysterious.")
        print("Who knows what adventures lie ahead?")
        print("Congratulations, you've completed the adventure!")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        continue_journey()

if __name__ == '__main__':
    start_game()
