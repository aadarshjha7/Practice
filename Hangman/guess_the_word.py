import random
with open('wordlist.txt', 'r') as file:
    word_list = file.read()
    word_list = word_list.split()

chosen_word = random.choice(word_list)
life = 10


display = []
for letter in chosen_word:
    display += "_"
print(display)

while True:
    guess = input("Guess a letter: ")
    guess = guess.lower()

    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    print(display)
    if "_" not in display:
        print("You win")
        break
    if guess not in chosen_word:
        life -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(f"You have {life} lives left.")
        if life == 0:
            print("You lose")
            break

    if "_" not in display:
        break
print(f"The word was {chosen_word}.")
