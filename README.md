# Mastermind Challenge
## Example Client (Python)

An example client for the Mastermind Challenge, written in Python 3.

This client requires the `requests` library, which you can install manually, or via pip:
```
pip install requests
```

Or using Pipenv, if you prefer (and have it installed), which will also create and manage a virtual environment for this project:
```
pipenv install  # (to create an environment and install)

pipenv shell # (to open a shell in the new environment)
```

In order to participate in the challenge, please follow the instructions here to create an account:
And add the resulting account_uid to line 11 of your mastermind_example_client.py script.

Once you have the requirements installed, and your account_uuid in place, you should be able to run the script:
```
python mastermind_example_client.py
```
(This will play a single game by default, which may take a while...)

## About the Game

_(Inspired by [Allan Stewart](https://github.com/allan-stewart)'s REST Mastermind Kata)_

Mastermind is a classic "code breaking" board game from the 1970s - We have re-implemented it as a RESTful web API, so that you can write your own client to play it. (FWIW, I don't recommend googling it, unless you want to spoil your own exploration of the problem space.)

The "codemaster", in this case, the API server, randomly generates a four digit Secret Code:
* Each digit consists of a number between 0 and 9
* Each digit in a secret code is unique - no digits will be repeated
* Secret codes are represented as strings (and may have leading zeroes)

Some possible Secret Codes could be: `"1234"`, `"0213"`, and `"9082"`

These following code are not valid, and would not be used by the server:
* `"42"` _too short_
* `"54321"` _too long_
* `"0099"` _repeated digits are not allowed_

When you submit a guess using the API, the server will respond with three pieces of information:
* `game_over`: A boolean value indicating whether or not the game is over. (if it's True, then you've won!)
* `correct_digits`: How many digits of your guess were fully correct (i.e. the right number in the right position)
* `misplaced_digits`: How many of the digits were misplaced (i.e. a correct number but not in the right position)
These hints are helpful, but not very specific - they don't tell you _which_ digits were fully correct, or misplaced, just how many of them were in that state.

(It's worth noting that the original physical board game recommends having a piece of paper handy, so that you can record the hints that resulted from each guess, to help inform your following guesses.)

To get you started, we've provided a client that plays Mastermind completely at random: This is a simple and effective strategy, but probably one of the least efficient and lest consistent ones, in terms of how many attempts it needs in order to win. _(You can give it a shot if you want, but to save you some time, It takes about 7,500 attempts, on average, to guess a four digit code. And sometimes more than twice that number!)_

The Mastermind Challenge server tracks your attempts, and can provide statistics on your approach, after you've played at least 10 games. (You can also use the Account API to reset your stats, if you have changed your approach and want to contrast the results.)

The Mastermind Leaderboard initially ranks you based on your most recent number of guesses, but will put you in a higher tier once you've played at least 10 games, based on your Average Guesses per game. (A lower number of guesses is better.)

We've provided some hints and suggestions below, if you aren't sure how to get started. But if you enjoy exploring problem spaces, feel free to experiment on your own first! You might come up with a better solution of your own...

.

.

(scroll down for suggestions)

.

.

(and possible spoilers...)

.

.

##  Suggestions

### 1. The Human Element
If you aren't familiar with Mastermind, it might be helpful to play a game yourself - you could modify your client to allow you to manually enter guesses using the `input` function, and use your experience from playing a few games to come up with a strategy. How will you choose valid guesses? How can you make use of the hints that the game is providing to you?

### 2. Better Random Guessing
Guessing completely at random is slow for a few different reasons. Sometimes this approach requires more guesses than there are possible secret codes, which seems especially bad! What changes can we make to prevent that? How can we make our random guesses more efficient, and ensure that they're valid guesses?

### 3. Using the Hints
Similar to the classic Mastermind board game, the challenge is providing hints about how "close" we are to guessing the code, but those hints are not very specific. Are there any cases where the hints are clearer than others? How could we try to reach those cases in fewer guesses?

### 4. Elementary, My Dear Watson
To quote the fictional detective Sherlock Holmes:

> "When you have eliminated all that is impossible,
> then whatever remains, however improbable,
> must be the truth."

Is it possible to apply Sherlock's style of deductive reasoning to this problem? How can we get a computer (which is better at crunching numbers than it is at analytical reasoning) to help us apply this wisdom?
