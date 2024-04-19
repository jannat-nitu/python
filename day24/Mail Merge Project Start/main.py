PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    starting_letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = starting_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as complete_file:
            complete_file.write(new_letter)





