import re
import random


def wants_to_play(go_input):
    return go_input.lower() == 'y'

def get_words(difficulty):
    easy_word_list = []
    normal_word_list = []
    hard_word_list = []
    with open('/usr/share/dict/words') as f:
        for word in f.readlines():
            stripped_word = re.sub('[^A-Za-z]', '', word)
            if 4 <= len(stripped_word) <= 6:
                easy_word_list.append(stripped_word)
            if 6 <= len(stripped_word) <= 8:
                normal_word_list.append(stripped_word)
            if 8 <= len(stripped_word):
                hard_word_list.append(stripped_word)
    if difficulty.lower() == 'e':
        return easy_word_list
    elif difficulty.lower() == 'h':
        return hard_word_list
    else:
        return normal_word_list


def get_winning_word(list):
    winning_word = random.choice(list)
    print(winning_word)
    return winning_word.lower()


def draw_new_board(winning_word):
    game_board = []
    for letter in winning_word:
            game_board.append('_')
    game_board = ' '.join(game_board)
    return game_board


def get_guess(guess_counter):
    if guess_counter == 0:
        return (input("Guess a letter: ")).lower()
    else:
        if guess_counter == 7:
            print("Last chance!\n")
        else:
            print("Careful, only {} more wrong guesses\n".format(8 - guess_counter))
        return (input("Guess again: ")).lower()


def is_invalid(guess, previous_guesses):
    if not guess.isalpha() or len(guess) != 1:
        print("\nTry guessing just one letter.")
        return True
    elif guess in previous_guesses:
        print("\nYou already guessed {}.".format(guess))
        return True
    else:
        return False


def is_good_guess(winning_word, guess):
    if guess in winning_word:
        return True


def draw_board(winning_word, game_board, guess):
    winning_word = list(winning_word)

    game_board = game_board.split()
    count = winning_word.count(guess)

    while count > 0:
        guess_index = winning_word.index(guess)
        game_board[guess_index] = guess.upper()
        winning_word[guess_index] = 0
        count = winning_word.count(guess)

    game_board = ' '.join(game_board)
    return game_board


def is_win(game_board):
    if '_' not in game_board:
        print("You win!")
        return True



def main():

    print("\nOh hai!\n")

    go_input = input("Do you want to keep playing Mystery World? Y/n\n")
    if not wants_to_play(go_input):
        print("\nOk Goodbye!")
        return False

    difficulty = input("\nPlease select a difficulty level: (E)asy, Normal (default), or (H)ard\n")

    winning_word = get_winning_word(get_words(difficulty))

    game_board = draw_new_board(winning_word)
    print("\n\nThere are {} letters in the word.".format(len(winning_word)))
    print("You get 8 guesses.")

    guess_counter = 0
    previous_guesses = []

    while guess_counter < 8:
        print('\n\n' + game_board + '\n')
        if previous_guesses:
            print("Previous guesses: ", " ".join(previous_guesses))
        guess = get_guess(guess_counter)
        if is_invalid(guess, previous_guesses):
            continue
        elif is_good_guess(winning_word, guess):
            previous_guesses.append(guess)
            game_board = draw_board(winning_word, game_board, guess)
            if is_win(game_board):
                break
        else:
            previous_guesses.append(guess)
            print("\nNope!")
            guess_counter += 1

    if guess_counter == 8:
        print("\nYou're all out of guesses.")
        print("The word was {}.\n".format(winning_word.upper()))

    main()

if __name__ == '__main__':
    main()
