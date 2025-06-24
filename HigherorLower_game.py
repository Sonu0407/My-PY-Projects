import HigherandLower_art
from game_data import data
import random

# display art
print(HigherandLower_art.logo)
score = 0

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# generate a random account from the game data
should_game_continue = True
account_b = random.choice(data)

while should_game_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    # format the account data into printable format
    account_name = account_a["name"]
    account_description = account_a["description"]
    account_country = account_a["country"]
    print(f"Compare A: {account_name}, a {account_description}, from {account_country}")
    print(HigherandLower_art.vs)
    account_name = account_b["name"]
    account_description = account_b["description"]
    account_country = account_b["country"]
    print(f"Against B: {account_name}, a {account_description}, from {account_country}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_game_continue = False
    # score keeping

    # making account at position b become the next account at position a.