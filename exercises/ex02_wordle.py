"""Let's play Wordle!"""

__author__: str = "730569281"


def contains_char(word: str, char: str) -> bool:
    """Check if given character (char) is found in given word"""
    assert len(char) == 1, f"len('{char}') is not 1"

    for letter in word:
        if letter == char:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    """Return box representing correctness of guess"""
    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    result = ""

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX

    return result


def input_guess(expected_length: int) -> str:
    """Prompts guess of expected word length."""
    guess = input(f"Enter a {expected_length} character word:")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 0
    max_turns = 6
    won = False

    while turns < max_turns and not won:
        turns += 1
        print(f"=== Turn {turns}/{max_turns} ===")

        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)

        if guess == secret:
            won = True
            print(f"You won in {turns}/{max_turns} turns!")
    if not won:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")

    if __name__ == "__main__":
        main("codes")
