import re
import random
# request level of difficulty
# get word list
# choose word from word list(based on difficulty)
# display word w/blanks or and/or letters
# get user guess
# adjust display
# adjust guess #
# end game output
# ask to play again




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
        print('easy')
        return easy_word_list
    elif difficulty.lower() == 'h':
        print('hard')
        return hard_word_list
    else:
        print('normal')
        return normal_word_list


def get_winning_word(list):
    winning_word = random.choice(list)
    print(winning_word)
    return winning_word

def draw_new_board(winning_word):
    game_board = []
    for letter in winning_word:
        return game_board.append('_')

def draw_board(winning_word, game_board, guess):
    winning_word = list(winning_word)

    if guess == None:
        for letter in winning_word:
            game_board.append('_')
    elif guess in winning_word:
        game_board = game_board.split()
        count = winning_word.count(guess)

        while count > 0:
            guess_index = winning_word.index(guess)
            game_board[guess_index] = guess.upper()
            winning_word[guess_index] = 0
            count = winning_word.count(guess)
            print(game_board)

    else:
        print("Wrong. Guess again.")
        return False

    game_board = ' '.join(game_board)
    print(game_board)
    return game_board


def get_guess(guess_counter):
    if guess_counter == 0:
        return input("Guess a letter: ")
    else:
        print("You have {} guesses left.".format(8 - guess_counter))
        return input("Guess again:")




def main():

    print("Welcome to Mystery Word!")
    if (input("Do you want to play? Y/n\n")).lower() != 'y':
        print("Ok Goodbye!")
        return

    difficulty = input("Please select a difficulty level: (E)asy, Normal (default), or (H)ard\n>>")

    winning_word = get_winning_word(get_words(difficulty))

    game_board = draw_new_board(winning_word)
    print(game_board)
    print("There are {} letters in the word.".format(len(winning_word)))

    guess_counter = 0

    while guess_counter < 8:
        game_board = draw_board(winning_word, game_board, guess)
        guess = get_guess(guess_counter)
        guess_counter += 1

    print("\n")


if __name__ == '__main__':
    main()
