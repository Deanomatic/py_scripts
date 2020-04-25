import random
def main():
    user_input = "y"
    while user_input != "n":
        user_input = ""
        new_user_input = intro(user_input)

        comp_choice = 0
        new_comp_choice = get_comp_choice(comp_choice)

        user_input = new_user_input
        get_user_choice(user_input)

        comp_choice = new_comp_choice
        display_choices(comp_choice, new_user_input)

        user_input = keep_going(user_input)

def intro(user_input):
    # displays the description of game
    user_input = input("rock, paper, or scissors? ")
    return user_input

def get_comp_choice(comp_choice):
    # calls randint() function, returns an int (computer choice)
    comp_choice = random.randint(0, 2)
    return comp_choice

def get_user_choice(user_input):
    # gets user choice, implements an input validation loop, calls
    # choice_to_num(), and returns an int (user choice)
    # print(user_input)  
    if user_input != user_input.lower():
        print("Invalid input. Please enter all lowercase.")
    else:
        choice_to_num(user_input)

def choice_to_num(user_input):
    # accepts a string (“rock”, “paper”, or “scissors”) and   
    #returns an int (1, 2, or 3)	
    if user_input == "rock":
        rock = 1
        user_input = rock
    elif user_input == "paper":
        paper = 2
        user_input = paper
    elif user_input == "scissors":
        scissors = 3
        user_input = scissors
    return user_input

    pass
def num_to_choice(comp_choice):
    # accepts an int (1, 2, or 3) and returns a string (“rock”, 
    #“paper”, or “scissors”)
    if comp_choice == 0:
        rock = "rock"
        comp_choice = rock
    elif comp_choice == 1:
        paper = "paper"
        comp_choice = paper
    elif comp_choice == 2:
        scissors = "scissors"
        comp_choice = scissors
    return comp_choice

def display_choices(comp_choice, new_user_input):
    # accepts two ints (1, 2, or 3), calls 
    #num_to_choice() and display choices
    new_computer_choice = num_to_choice(comp_choice)
    print("I chose", new_computer_choice)
    print("you chose", new_user_input)
    if new_user_input == new_computer_choice:
        print("We tied. Much wow")
    elif new_user_input == "rock":
        if new_computer_choice == "paper":
            print("You lose you bastard")
        else:
            print("You win! F computers!")
    elif new_user_input == "paper":
        if new_computer_choice == "scissors":
            print("You lose you bastard")
        else:
            print("You win! F computers!")
    elif new_user_input == "scissors":
        if new_computer_choice == "rock":
            print("You lose you bastard")
        else:
            print("You win! F me!")

    return new_computer_choice
def keep_going(user_input):
    #gets users response and returns True if user wants to play more
    user_input = input("Do you want to play another game? y/n ")
    if user_input == "n":
        print("Thanks for playing jackweed")
    return user_input

main()