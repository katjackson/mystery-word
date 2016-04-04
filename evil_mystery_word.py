import re
import random


def wants_to_play(go_input):
    return go_input.lower() == 'y'


def get_words(difficulty):
    possible_winning_word_list = []

    if difficulty.lower() == 'e':
        winning_word_length = random.randint(4, 6)
    elif difficulty.lower() == 'h':
        winning_word_length = random.randint(8, 24)
    else:
        winning_word_length = random.randint(6, 8)

    with open('/usr/share/dict/words') as f:
        for word in f.readlines():
            stripped_word = re.sub('[^A-Za-z]', '', word)
            if len(stripped_word) == winning_word_length:
                possible_winning_word_list.append(stripped_word.lower())

    return possible_winning_word_list


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
        if guess_counter == 14:
            print("Last chance!\n")
        else:
            print("Careful, only {} more wrong guesses\n".format(15 - guess_counter))
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


def create_blanks_key(guess, word):
    blanks_key = ''
    for letter in word:
        if letter == guess:
            blanks_key += letter
        else:
            blanks_key += '_'
    return blanks_key


def find_longest_value(dictionary_of_word_lists):
    max_list_length = 0

    for key in dictionary_of_word_lists:
        if len(dictionary_of_word_lists[key]) > max_list_length:
            max_list_length = len(dictionary_of_word_lists[key])
            max_list_key = key

    return max_list_key


def narrow_word_list(guess, possible_winning_word_list):
    word_families = {}

    if len(possible_winning_word_list) == 1:
        return possible_winning_word_list

    for word in possible_winning_word_list:
        if guess in word:
            blanks_key = create_blanks_key(guess, word)
            try:
                word_families[blanks_key].append(word)
            except:
                word_families[blanks_key] = [word]
        else:
            try:
                word_families['guessless word family'].append(word)
            except:
                word_families['guessless word family'] = [word]

    max_list_key = find_longest_value(word_families)

    return(word_families[max_list_key])


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
        print("\nYou win!")
        return True



def main():

    print("\nOh hai!\n")

    go_input = input("Do you want to keep playing Mystery World? Y/n\n")
    if not wants_to_play(go_input):
        print("\nOk Goodbye!")
        return False

    difficulty = input("\nPlease select a difficulty level: (E)asy, Normal (default), or (H)ard\n")

    possible_winning_word_list = get_words(difficulty)

    sample_word = possible_winning_word_list[0]

    game_board = draw_new_board(sample_word)
    print("\n\nThere are {} letters in the word.".format(len(sample_word)))
    print("You get 15 guesses.")

    guess_counter = 0
    previous_guesses = []

    while guess_counter < 15:
        print('\n\n' + game_board + '\n')
        if previous_guesses:
            print("Previous guesses: ", " ".join(previous_guesses))

        guess = get_guess(guess_counter)

        if is_invalid(guess, previous_guesses):
            continue

        else:
            possible_winning_word_list = narrow_word_list(guess, possible_winning_word_list)
            sample_word = possible_winning_word_list[0]
            previous_guesses.append(guess)
            game_board = draw_board(sample_word, game_board, guess)

            if is_win(game_board):
                print("The word was", game_board)
                break

            if guess not in game_board:
                print("\nNope!")
                guess_counter += 1

    if guess_counter == 15:
        print("\nYou're all out of guesses.")
        sample_word = possible_winning_word_list[0]
        print("The word was {}.\n".format((''.join(sample_word)).upper()))

    main()

if __name__ == '__main__':
    main()
