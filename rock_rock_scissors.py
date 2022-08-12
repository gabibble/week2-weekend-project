import random
from play_game import play

print("Welcome to Rock Paper Scissors!")

player1_score = 0
comp1_score = 0

while True:
    player1 = input("\nEnter 'Rock', 'Paper' or 'Scissors' When you are finished, enter 'I quit' ")
    if player1.lower() == "i quit":
        print("\nFinal score: \nYour Score: " + str(player1_score) + " Computer's Score: " + str(comp1_score))
        if player1_score > comp1_score:
            print("\n\nYou've won the game! You are the spiciest!")
        elif player1_score < comp1_score:
            print("\n\nComputer won! Computers will rule the world!!")
        else: 
            print("\n\nIt's a tie! Perhaps humans and computers can coexist in harmony!")
        print("\n\nThank You for playing!\n") 
        break

    if player1.lower() != "rock" and player1.lower() != "paper" and player1.lower() != "scissors":
        print("Sorry did not compute")
        continue

    comp1 = random.choice(['rock', 'paper', 'scissors'])
    print("computer chose: " +comp1)
    if player1.lower() == comp1:
        print("\tIt's a tie")
        print("\tCurrent score: You: " + str(player1_score) + " Comp: " + str(comp1_score))

    elif play(player1, comp1) == True:
        print("\tYou won!")
        player1_score += 1
        print("\tCurrent score: You: " + str(player1_score) + " Comp: " + str(comp1_score))
    else:
        print("\tYou lost!")
        comp1_score += 1
        print("\tCurrent score: You: " + str(player1_score) + " Comp: " + str(comp1_score))

    
        

