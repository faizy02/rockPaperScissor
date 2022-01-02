import random 

def play():
    user_input = input(f"Please do your move Rock(r), Paper(p) or Scissor(s)")
    computer_move = random.choice(['r','p','s']) # 1 => rock, 2 => paper, 3 => scissor

    if user_input == computer_move:
        print("No Result! Its a Tie")
    else:
        if user_input == 'r':
            print("You selected ROCK")
            if computer_move == 'p':
                print("Computer selected PAPERRRR")
                uWin = False
            elif computer_move == 's':
                print("Computer selected SCISSOR")
                uWin = True
        if user_input == 'p':
            print(f"You selected PAPER")
            if computer_move == 'r':
                print("Computer selected ROCK")
                uWin = True
            elif computer_move == 's':
                print("Computer selected SCISSOR")
                uWin = False
        if user_input == 's':
            print(f"You selected SCISSOR")
            if computer_move == 'r':
                print("Computer selected ROCK")
                uWin = False
            elif computer_move == 'p':
                print("Computer selected PAPERRRR")
                uWin = True
        
        if uWin == 1:
            print("Humain beats you compuneter")
        elif uWin == 0:
            print("Compunter beats you Humain")

play()
    

