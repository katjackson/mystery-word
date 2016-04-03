import unittest
import evil_mystery_word

class EvilMysteryWordTest(unittest.TestCase):

    def test_wants_to_play(self):
        self.assertTrue(evil_mystery_word.wants_to_play('Y'))
        self.assertFalse(evil_mystery_word.wants_to_play(''))
        self.assertFalse(evil_mystery_word.wants_to_play('f'))

    def test_get_easy_words(self):
        resulting_list = evil_mystery_word.get_words('e')
        self.assertTrue(4 <= len(resulting_list[25]) <= 6 and len(max(resulting_list)) == len(min(resulting_list)))

    def test_get_hard_words(self):
        resulting_list = evil_mystery_word.get_words('h')
        self.assertTrue(8 <= len(resulting_list[0]) and len(max(resulting_list)) == len(min(resulting_list)))

    def test_get_normal_words(self):
        resulting_list = evil_mystery_word.get_words('')
        self.assertTrue(6 <= len(resulting_list[25]) <= 8 and len(max(resulting_list)) == len(min(resulting_list)))

    def test_draw_new_board(self):
        game_board = evil_mystery_word.draw_new_board('wingman')
        self.assertEqual(game_board, '_ _ _ _ _ _ _')

    def test_get_guess(self):
        pass

    def test_create_blanks_key(self):
        self.assertEqual((evil_mystery_word.create_blanks_key('a', 'banana')), '_a_a_a')

    def test_narrow_word_list(self):
        fake_word_list = [list('axxx'), list('abxx'), list('xabx'), list('xbax'), list('xbxx'), list('xbxx'), list('xxxx')]
        self.assertEqual(evil_mystery_word.narrow_word_list('a', fake_word_list), [list('xbxx'), list('xbxx'), list('xxxx')])
        self.assertEqual(evil_mystery_word.narrow_word_list('b', fake_word_list), [list('abxx'), list('xbax'), list('xbxx'), list('xbxx')])

    def test_draw_board(self):
        game_board = evil_mystery_word.draw_board('lanceman', 'L _ _ C _ _ A _', 'n')
        self.assertEqual(game_board, 'L _ N C _ _ A N')

    def test_is_invalid(self):
        self.assertTrue(evil_mystery_word.is_invalid('bro', ['a', 'b', 'c']))
        self.assertFalse(evil_mystery_word.is_invalid('f', ['a', 'b', 'c']))
        self.assertTrue(evil_mystery_word.is_invalid('b', ['a', 'b', 'c']))
        self.assertTrue(evil_mystery_word.is_invalid('4', list('abcdef')))
        self.assertTrue(evil_mystery_word.is_invalid('$', list('abcdef')))

    def test_is_win(self):
        self.assertTrue(evil_mystery_word.is_win('E N V I A B L E'))
        self.assertFalse(evil_mystery_word.is_win('P _ P _ R E _ N'))

if __name__ == '__main__':
    unittest.main()
