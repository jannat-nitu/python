import random
print("welcome to the number guessing game")
print("i am thinking 1 to 100")
user_choice = input("choose a difficulty. type 'easy' or 'hard':")

num = random.randint(1, 100)
live = 1
live_1 = 5
def play_easy(live) :
    win = False
    while win == False:

        guess = int(input("guess a number between 1 and 100: "))
        if guess > num:
            print("too high")
        elif guess < num:
            print("too low")
        else:
            print("you win")
            win = True
        live = live - 1
        if live > 0 and win == False:
            print(f"you have {live} remaining")
        elif win == False and live == 0:
            print("you lost")
            win = True



if user_choice == "easy":
    play_easy(live)
if user_choice == "hard":
    play_easy(live_1)

