import unittest
import mystery_word

class MysteryWordTest(unittest.TestCase):

    def test_get_easy_words(self):
        resulting_list = mystery_word.get_words('e')
        self.assertTrue(4 <= len(resulting_list[25]) <= 6)

    def test_get_hard_words(self):
        resulting_list = mystery_word.get_words('h')
        self.assertTrue(8 <= len(resulting_list[25]))

    def test_get_normal_words(self):
        resulting_list = mystery_word.get_words('')
        self.assertTrue(6 <= len(resulting_list[25]) <= 8)

    def test_get_winning_word(self):
        winning_word = mystery_word.get_winning_word(['a', 'list', 'of', 'words'])
        self.assertTrue(winning_word in ['a', 'list', 'of', 'words'])

    def test_draw_new_board(self):
        game_board = mystery_word.draw_new_board('wingman')
        self.assertEqual(game_board, '_ _ _ _ _ _ _ ')

if __name__ == '__main__':
    unittest.main()
