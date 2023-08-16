# #! python 3
# #multiplicationQuiz.py - a programm that quizzes the user a certain number of times, used to get a feel on how much work pyinputplus is doing (for input validation)

# // TODO timeout. 

import random
import time

numberOfQuestions = 10
correctAnswers = 0
incorrectAttempts = 0

for questionNumber in range(1, numberOfQuestions+1):
    numberOne = random.randint(0,10)
    numberTwo = random.randint(0,10)
    multiplicand = numberOne * numberTwo
    time.sleep(1)
    timer_start = int(time.perf_counter())
    userInput = input(f"{questionNumber}: What's {numberOne} x {numberTwo}? ")
    timer_end = int(time.perf_counter())
    #user gets 3 chances per question to input an integer
    while incorrectAttempts < 2 and userInput.isdigit() == False and timer_end - timer_start < 8:
        timer_end = int(time.perf_counter())
        incorrectAttempts += 1
        print(f"{userInput} is not a number!")
        userInput = input(f"{questionNumber}: Try again! Attempt: {incorrectAttempts+1}\nWhat's {numberOne} x {numberTwo}? ")
    #user gets 3 chances per question to answer correctly (math problem, not an input problem)
    while incorrectAttempts < 2 and int(userInput) != multiplicand:
        timer_end = int(time.perf_counter())
        incorrectAttempts += 1
        print("Incorrect! :(")
        userInput = input(f"{questionNumber}: Try again! Attempt: {incorrectAttempts+1}\nWhat's {numberOne} x {numberTwo}? ")
    #printing an incorrect message if user exceeded 3 attempts
    if incorrectAttempts == 2:
        incorrectAttempts = 0
        print("Still incorrect. Exceeded your 3 attempts. :(")
        time.sleep(1)
        continue
    timer_end = int(time.perf_counter())
    #printing timeout message if timeout is reached
    if timer_end - timer_start > 8:
        print("It took you longer than 8 seconds.")
        incorrectAttempts = 0
        time.sleep(1)
        continue
    #printing correct and keeping track of number of correct answers
    if int(userInput) == multiplicand:
        print("Correct!")
        correctAnswers += 1
        time.sleep(1)
    incorrectAttempts = 0
print(f"You answered {correctAnswers}/{numberOfQuestions} correctly.")

#if __name__ == '__main__':