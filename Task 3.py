import random
def get_computer_choice():
    options=["rock","paper","scissors"]
    return random.choice(options)
def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return"It's a tie!"
    elif(user_choice=="rock" and computer_choice=="scissors") or (user_choice =="scissors" and computer_choice=="paper" or user_choice=="paper" and computer_choice=="rock"):
        return "You Win!"
    else:
        return "You lose!"
def play_game():
    user_score=0
    computer_score=0
    play_again=True
    while play_again:
        user_choice=input("Enter rock,paper or scissors:").lower()
        if user_choice not in ["rock","paper","scissors"]:
            print("Invalid Choice! Please enter rock,paper or scissors.")
            continue
        computer_choice=get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result=determine_winner(user_choice,computer_choice)
        print(result)
        if result=="You win!":
            user_score+=1
        elif result=="You lose!":
            computer_score+=1
            print(f"Score:You{user_score}-{computer_score}Computer")
            play_again_input=input("Do you want to play again?(yes/no):").lower()
            if play_again_input!="yes":
                play_again=False
        print("Thanks for playing!")
#if _name_=="_main_":
play_game()












        
            
            
        
        
