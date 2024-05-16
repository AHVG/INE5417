import unittest

from model.Player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(name="John Doe", id="123", symbol="X", is_turn=True, winner=False)

    def test_initialization(self):
        self.assertEqual(self.player.get_name(), "John Doe", "Name should be 'John Doe'")
        self.assertEqual(self.player.get_id(), "123", "ID should be '123'")
        self.assertEqual(self.player.get_symbol(), "X", "Symbol should be 'X'")
        self.assertTrue(self.player._is_turn, "is_turn should be True")
        self.assertFalse(self.player.get_winner(), "winner should be False")

    def test_setters(self):
        self.player.set_name("Jane Doe")
        self.assertEqual(self.player.get_name(), "Jane Doe", "Name should be updated to 'Jane Doe'")
        self.player.set_id("456")
        self.assertEqual(self.player.get_id(), "456", "ID should be updated to '456'")
        self.player.set_symbol("O")
        self.assertEqual(self.player.get_symbol(), "O", "Symbol should be updated to 'O'")
        self.player.set_winner(True)
        self.assertTrue(self.player.get_winner(), "winner should be updated to True")

    def test_reset(self):
        self.player.reset(name="New Player", id="789", symbol="Y", is_turn=False, winner=True)
        self.assertEqual(self.player.get_name(), "New Player", "Name should be reset to 'New Player'")
        self.assertEqual(self.player.get_id(), "789", "ID should be reset to '789'")
        self.assertEqual(self.player.get_symbol(), "Y", "Symbol should be reset to 'Y'")
        self.assertFalse(self.player._is_turn, "is_turn should be reset to False")
        self.assertTrue(self.player.get_winner(), "winner should be reset to True")

if __name__ == '__main__':
    unittest.main()
