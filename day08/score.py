alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, amount, direction):
    if direction == "decode":
        amount *= -1
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + amount
            new_position = new_position % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char

    print(f"the encode test {cipher_text}")


cont = True
while cont == True:
    direction = input("type 'encode' to encrypt, type 'decode' \n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    opinion = input("if you want continue type 'yes' if not type no").lower()
    if opinion == "no":
        cont = False
        print("good bye")