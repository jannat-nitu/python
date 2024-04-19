logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
import random
def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
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
user_card = []
computer_card = []


for i in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
process = False
while not process:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)

    print(f"   Your cards: {user_card}, current score: {user_score}")
    print(f"   Computer's first card: {computer_card[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True

    users_should_deal = input("if you want another card type 'yes' or for pass type 'no': ")
    if users_should_deal == "yes":
        user_card.append(deal_card())
    else:
        game_over = True


while computer_score != 0 or computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)

print(compare(user_score, computer_score))
print(f"   Your final hand: {user_card}, final score: {user_score}")
print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")

