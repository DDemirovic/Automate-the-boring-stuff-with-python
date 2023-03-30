import random

def randomNumberGuesser():
    print('Try to guess the secret Number and become a wizard. You have 6 attempts in total.')
    guessedNumber = int(input())
    attempts = 1
    while attempts < 7:
        print('This is attempt', attempts, '.')
        if secretNumber == guessedNumber:
            print('Congratulations! You guessed the number correctly. It took you', attempts, ' attempts. Well done Wizard!')
            break
        elif secretNumber > guessedNumber:    
            if attempts == 6:                
                print('The game is over. You should go back to the wizard academy and come back once you got more experience!')
                break
            else:
                print('Nice try! The secret number is greater than your guessed number. Please enter a new number.')
                guessedNumber = int(input())
                attempts = attempts + 1
        else:
            if attempts == 6:
                print('The game is over. You should go back to the wizard academy and come back once you got more experience!')
                break
            else:
                print('Nice try! The secret number is smaller than your guessed number. Please enter a new number.')
                guessedNumber = int(input())
                attempts = attempts + 1

secretNumber = random.randint(1, 20)
print('The secret number is:', secretNumber)
randomNumberGuesser()
