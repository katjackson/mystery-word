import re
import random


def wants_to_play(go_input):
    return go_input.lower() == 'y'

def get_words(difficulty):
    possible_winning_word_list = []

    if difficulty.lower() == 'e':
        winning_word_length = random.randint(4, 6)
    elif difficulty.lower() == 'h':
        winning_word_length = random.randint(6, 24)
    else:
        winning_word_length = random.randint(6, 8)

    with open('/usr/share/dict/words') as f:
        for word in f.readlines():
            stripped_word = re.sub('[^A-Za-z]', '', word)
            if len(stripped_word) == winning_word_length:
                possible_winning_word_list.append(list(stripped_word.lower()))

    return possible_winning_word_list



def narrow_word_list(guess, possible_winning_word_list):
    possibly_useless_dictionary = {}
    for word in possible_winning_word_list:
        if guess in word:
            indices = [i for i, x in enumerate(word) if x == guess]
            for index in indices:
                try:
                    possibly_useless_dictionary[index] = possibly_useless_dictionary[index] + [word]
                except:
                    possibly_useless_dictionary[index] = word
            continue
    print(possibly_useless_dictionary)
    # return possibly_useless_dictionary[max(possibly_useless_dictionary)]



# def get_winning_word(list):
#     winning_word = random.choice(list)
#     print(winning_word)
#     return winning_word


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

    possible_winning_word_list = get_words(difficulty)
    guess = 'a'
    narrow_word_list(guess, possible_winning_word_list)


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

# take user guess, adjust board, adjust list of winning words
# name list the new board structure?
