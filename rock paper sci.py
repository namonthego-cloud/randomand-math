import random #importing random module

while True: #itrate loop
    user_action = input("enter a choice(rock,paper,scissor):") #take input
    possible_actions = ["rock","paper","scissor"]
    #using random function
    computer_action = random.choice(possible_actions)
    print(f"\nyou chose {user_action},computerchose{computer_action}.\n") #display both out puts whata is selected by you and computer


    #conditions to check who won the game
    if user_action == computer_action:
        print(f"both playrs selected{user_action}. it's a tie !")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smases scissors! you win!")
        else:
            print("paper covers rock you lose.")
    elif user_action == "paper":
            if computer_action == "rock":
                print("paper covers rock! you win!")
            else:
                print("scissor cuts papper you lose.")
    elif user_action == "scisssor":
            if computer_action == "paper":
                print("scissor cuts paper! you win!")
            else:
                print("rock smashes scissor you lose.")
    play_again = input("play again? (y/n):")
    if play_again != "y":
         break
    


