alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(text, shifts):
        cipher_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shifts
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")

    def decrypt(text, shifts):
        cipher_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shifts
            cipher_text += alphabet[new_position]
        print(f"The decoded text is {cipher_text}")

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid input")

    again = input("Do you want to use again? Type 'yes' or 'no'.\n")
    if again == "no":
        print("Thank you for using the program.")
        break
