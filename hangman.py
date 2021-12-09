from replit import clear
import hangman_art
import hangman_words
import random

stages = hangman_art.stages
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
past_guesses = []
end_of_game = False
lives = 6

print(hangman_art.logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  clear()
  print(hangman_art.logo)
    
  if guess in past_guesses:
    print(f'You have already chosen "{guess.upper()}". Please guess again.\n')
  else:
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f'You chose "{guess.upper()}", which is not in the word.\n')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"\nYou lose.\nThe word was {chosen_word}.\n")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
  past_guesses += guess
