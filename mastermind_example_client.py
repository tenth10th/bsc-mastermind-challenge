from example_player import Player

import sys
from urllib.parse import urljoin
import requests


# Create an account as per these instructions: http://code-challenge.org/
# and put your account_uuid in the quotes below...
account_uuid = ""
# Once you have an account_uuid, run this script with python to play Mastermind.

hostname = "http://code-challenge.org/"

base_api = urljoin(hostname, "api/")
accounts_api = urljoin(base_api, "account/")
my_account_api = urljoin(accounts_api, account_uuid)
mastermind_api = urljoin(base_api, "mastermind")

games_required_for_stats = 10


def play_n_times(n=1):
    """ Play N games of Mastermind """
    for i in range(n):
        play_mastermind()
    display_stats()


def play_mastermind():
    """Play Mastermind once (until game_over becomes True)"""
    guess_count = 0
    game_over = False
    while not game_over:
        guess_count += 1
        player = Player()
        current_guess = player.guess()
        json_response = mastermind_post(current_guess)
        correct_digits = json_response.get("correct_digits")
        misplaced_digits = json_response.get("misplaced_digits")
        game_over = json_response.get("game_over")
        print(
            f"Guess #{guess_count}: {current_guess} - "
            f"Result: {correct_digits} digits correct, "
            f"{misplaced_digits} misplaced"
        )
        player.process_results(current_guess, correct_digits, misplaced_digits)

    print(f"We won! (After {guess_count} guesses)")
    return guess_count


def mastermind_post(guess):
    """Post a guess to the Mastermind API, and decode the JSON response"""
    json_payload = {"account_uuid": account_uuid, "guess": guess}

    response = requests.post(mastermind_api, json=json_payload)
    try:
        response.raise_for_status()
    except Exception as e:
        print(e)
        print(f"Server Response: {response.json()}")
        sys.exit(1)
    return response.json()


def display_stats():
    """Request average guess statistics from the server (after 10+ games)"""
    response = requests.get(my_account_api)
    response.raise_for_status()

    response_json = response.json()
    total_games = response_json.get("total_games")
    average_guesses = response_json.get("average_guesses")

    if average_guesses is not None:
        print()
        print(
            f"Your solution won in an average of {average_guesses} guesses, "
            f"across {total_games} total games."
        )
        print()
    else:
        print(f"(Win {10-total_games} more games to see Average Guesses stats)")


HELP_TEXT = """
To get started, register an account for your Team, and record the resulting
account_uuid on line 10 of this script.

(See http://code-challenge.org/ for detailed instructions)
"""


if __name__ == "__main__":
    if not account_uuid:
        """Encourage users to create an account, if they haven't already"""
        print(HELP_TEXT)
        sys.exit(1)

    play_n_times(n=1)
