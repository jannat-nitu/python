import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dic = {row.letter: row.code for (letter, row) in data.iterrows()}
game_on = True
while game_on:
    user_choice = input("What is your name?").upper()
    try:
        word = [dic[letter] for letter in user_choice]
    except KeyError:
        print("Sorry only alphabet letters are allowed")
    else:
        print(word)
        game_on = False
