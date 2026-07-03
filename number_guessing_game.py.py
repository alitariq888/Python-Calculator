import random

def number_guessing_game():
    print("=" * 40)
    print("🎮 Welcome to the Number Guessing Game!")
    print("=" * 40)

    while True:
        number = random.randint(1, 100)
        attempts = 0

        print("\nI have selected a number between 1 and 100.")
        print("Can you guess it?")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue

                if guess < number:
                    print("📉 Too low! Try again.")

                elif guess > number:
                    print("📈 Too high! Try again.")

                else:
                    print(f"\n🎉 Congratulations!")
                    print(f"You guessed the number in {attempts} attempts.")
                    break

            except ValueError:
                print("❌ Please enter a valid whole number.")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    number_guessing_game()