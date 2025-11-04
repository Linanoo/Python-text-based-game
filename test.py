import unittest

from backpack import Backpack
from game import Game

class Test(unittest.TestCase):

    def setUp(self):  # Method called by unittest to prepare the test fixture.
        """Runs prior to each unit test """
        self.backpack = Backpack(capacity=5)
        self.game = Game()

    def tearDown(self):  # Method called by unittest to after the test runs.
        """Runs after each unit test """
        self.backpack.contents.clear()

    def test_add_item(self):
        #test adding some items to the backpack
        self.backpack.add_item("cat")
        self.assertTrue(self.backpack.add_item('Philodendron White Wizard'))
        self.assertTrue(self.backpack.add_item('Philodendron Joeppii'))
        self.assertTrue(self.backpack.add_item('Philodendron Giganteum'))

    def test_remove_item(self):
        ##test removing some items from the backpack
        self.backpack.add_item('Philodendron Joeppii')
        self.assertFalse(self.backpack.remove_item('Philodendron Joeppii'))

    def test_check_item(self):
        ##test checking if some items tare in the backpack
        self.backpack.add_item('Philodendron White Wizard')
        self.assertTrue(self.backpack.check_item('Philodendron White Wizard'))
        self.assertFalse(self.backpack.check_item('Philodendron Joeppii'))

    def test_full_backpack(self):
        # Test the case where the backpack is full
        # Set backpack capacity to 1 for testing
        self.game.backpack = Backpack(capacity=1)
        self.game.philodendron_places = {
            self.game.one: "philodendron subhastatum"}  # Assign a philodendron to the location
        self.game.philodendron_function()  # First collection should be successful
        self.assertFalse(self.game.philodendron_function(), "Should not be able to collect when backpack is full")

    def test_remove_philodendron(self):
        # Check if the player can remove a philodendron from the backpack
        philodendron_name = "philodendron subhastatum"
        self.game.backpack.add_item(philodendron_name)
        initial_backpack_size = len(self.game.backpack.contents)
        self.game.remove_philodendron_from_backpack(philodendron_name)
        self.assertTrue(len(self.game.backpack.contents) < initial_backpack_size, "Failed to remove philodendron")


    def test_player_quit(self):
        # Verify the outcome when the player decides to quit
        command = ('quit', None)
        self.assertTrue(self.game.process_command(command), "Failed to quit the game")

if __name__ == '__main__':
    unittest.main()
