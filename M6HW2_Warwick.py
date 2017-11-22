# CTI-110
# M6HW2 - Guessing Game
# Cameron Warwick
# 11/19/17

def main():
    keepPlaying = True
    while True:
        play_game()
        answer = input('Would you like to play again? y or n?: ')
        if answer == 'y':
            continue
        elif answer == 'n':
            print('Thanks for playing then. Goodbye')
            break
        else:
            print('All incorrect responses are assumed to be yes, have fun~')
            
        
    
        

def play_game():
    import random
    print('Welcome to the patented Number Guesser 9000!')
    print('--------------------------------------------')


    # Values
    MIN = 1
    MAX = 15

    # Values for fun! WIP!
    dialogue1 = 'Give it your best shot!: '
    dialogue2 = 'Have a go at it!: '
    dialogue3 = 'Your guess is as good as mine!: '
    dialogue4 = "We all have our guesses, it's just that mine is better than yours: "
    dialogue5 = "If you don't get it right this time, you're not praising the sun hard enough: "

    # Choosing a number
    print('Choosing a number...')
    number = random.randint(MIN, MAX)
    dialogue = [dialogue1, dialogue2, dialogue3, dialogue4, dialogue5]
    dialogueChoice = random.choice(dialogue)
    # print("I'M HELPING YOU CHEAT YOU UNLUCKY NERD, HERE: ",number)

    # Asking for, and manipulating input / dialogue choices
    print('Alright! I have a number between 1 and 15. Can you guess it? You only have 5 tries!')
    tries = 0
    while tries < 5:
        dialogue = [dialogue1, dialogue2, dialogue3, dialogue4, dialogue5]
        dialogueChoice = random.choice(dialogue)
        guess = input(dialogueChoice)
        guess = int(guess)
        tries = tries + 1
        if guess < number:
            print('Too low, try again')
        if guess > number:
            print('Too high, try again')
        if guess == number:
            print('Correct!')
            break
    # Determining win or loss/ try count
    if guess == number:
        print('You win! The prize is nothing')
        print('You made a total of',tries, 'guesses')
    else:
        print('Sorry! You lose, better luck next time')  


main()
    
    
    
    
    
    
