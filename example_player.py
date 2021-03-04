import random
import string


class Player:
    def guess(self):
        """Generate a random four-digit string guess for the Mastermind API"""
        guess_digits = list()
        for _ in range(4):
            guess_digits.append(random.choice(string.digits))

        return "".join(guess_digits)

    def process_results(self, current_guess, correct_digits, misplaced_digits):
        """Do something useful with the results of the current guess"""
        # TODO: More useful than this, maybe?
        pass


if __name__ == "__main__":
    player = Player()
    random_guess = player.guess()
    print(f"This Player provides random guesses: {random_guess}")
    print("Run mastermind_example_client.py to use it in the challenge!")
