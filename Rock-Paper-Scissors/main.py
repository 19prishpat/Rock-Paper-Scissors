import random 

choice = ['rock', 'paper', 'scissors']

wins = 0
losses = 0
ties = 0

print('Game of rock, paper and scissors')

while True: 
    player_choice = input('Enter rock, paper or scissors: ')

    if player_choice not in choice:
        print('Invalid, enter again: ')
        continue

    computer = random.choice(choice)
    print('Computer played: ')

    if player_choice == computer:
        print('It is a tie')
        ties += 1

    elif (player_choice == "rock" and computer == "scissors") or (player_choice == "paper" and computer == "rock") or (player_choice == "scissors" and computer == "paper"):
        print('You win')
        wins += 1
    else: 
        print('You lose')
        losses += 1

    print('Wins: ', wins)
    print('Losses: ', losses)
    print('Ties: ', ties)

    again = input('Enter yes to play again and no if you want to exit: ')
    if again.lower()!= 'yes':
        break



