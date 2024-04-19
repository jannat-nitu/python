from random import randint

print("welcome to the number guessing game")
print("i am thinking 1 to 100")
choice = randint(1, 100)
user_choice = input("choose a difficulty. type 'easy' or 'hard':")
live = 10
live_hard = 5


def play_game(live):
    while live != 0:
        guess = int(input("guess a number"))
        if guess > choice:
            print("it's too high")
        elif guess < choice:
            print("it's too low")

        live -= 1
        if live == 0:
            print("you lost")
        elif guess == choice:
            live = 0
            print(f"you got it {choice}")
        else:
            print(f"you have {live} remaining")


if user_choice == "easy":
    play_game(live)
if user_choice == "hard":
    play_game(live_hard)

