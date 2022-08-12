def play (player, computer):
    if player == 'rock' and computer == 'scissors':
        return True
    if player == 'rock' and computer == 'paper':
        return False
    if player == 'scissors' and computer == 'paper':
        return True
    if player == 'scissors' and computer == 'rock':
        return False
    if player == 'paper' and computer == 'rock':
        return True
    if player == 'paper' and computer == "scissors":
        return False