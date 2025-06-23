from enum import nonmember
from random import randint

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too High")
        return turns -1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns -1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return None


def set_difficulty():
    level = input("choose a difficulty. Type easy or hard: ")
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN



def game():
    print("welcome to a guessing game")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"the correct answer is {answer}")
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        guess = int(input("Make a guess: "))
        print(f"You have {turns} attempts to guess the number")
        turns = check_answer(user_guess=guess, actual_answer=answer, turns = turns)
        if turns == 0:
            print("You lose because you ran out of attempts")
            return
        elif guess != answer:
            print("Guess again")
game()