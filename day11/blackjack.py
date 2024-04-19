import random
import clear
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return(card)
def calculate_score(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


users = []
computer = []

game_over = False

computer_score = 0
user_score = 0
for index in range(2):
    new_card = deal_card()
    users.append(new_card)
    computer.append(new_card)
while not game_over:
    user_score = calculate(users)
    computer_score = calculate(computer)

    print(f"   Your cards: {users}, current score: {user_score}")
    print(f"   Computer's first card: {computer[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        users_should_deal = input("if you want another card type 'yes' or for pass type 'no': ")
        if users_should_deal == "yes":
            users.append(deal_card())
        else:
            game_over = True
while computer_score != 0 and computer_score < 17:
    computer.append(deal_card())
    computer_score = calculate_score(computer)


print(f"   Your final hand: {users}, final score: {user_score}")
print(f"   Computer's final hand: {computer}, final score: {computer_score}")
print(compare(user_score, computer_score))

