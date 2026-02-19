import random
words = ["python", "java", "hangman", "coding", "college"]

word = random.choice(words)
display = ["_"] * len(word)

lives = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game")

while lives > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct guess ✅")
    else:
        lives -= 1
        print("Wrong guess ❌ Lives left:", lives)

# Result
if "_" not in display:
    print("\n🎉 You Win! Word was:", word)
else:
    print("\n💀 You Lose! Word was:", word)
