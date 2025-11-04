
from place import Place
from text_ui import TextUI
from backpack import Backpack
import logging

logging.basicConfig(filename='game_log.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        # attributes
        self.philodendron_places = {}
        self.create_places()
        self.current_place = self.zero
        self.textUI = TextUI()
        self.fuel = 100
        self.backpack = Backpack(capacity=5)

    def create_places(self):
        """
            Sets up all place assets.
        :return: None
        """
        self.zero = Place("You are at Heathrow Airport")
        self.one = Place("You are in Amazon Rainforest")
        self.two = Place("You are in Congo Rainforest")
        self.three = Place("You are in Australiasian Realm")
        self.four = Place("You are in Sundaland Region")
        self.five = Place("You are in Indo Burma Region")
        self.six = Place("You are in Mesoamerica Rainforest")
        self.seven = Place("You are in Wallacea Rainforest")
        self.eight = Place("You are in Guinean Forest")
        self.nine = Place("You are in Atlantic Forest")
        self.ten = Place("You are in Choco Darien Forest")

        self.zero.set_exit("east", self.five)
        self.zero.set_exit("south", self.eight)
        self.zero.set_exit("west", self.six)
        self.one.set_exit("north", self.ten)
        self.one.set_exit("east", self.two)
        self.one.set_exit("south", self.nine)
        self.two.set_exit("east", self.seven)
        self.two.set_exit("west", self.one)
        self.two.set_exit("north", self.eight)
        self.three.set_exit("west", self.nine)
        self.three.set_exit("north", self.seven)
        self.four.set_exit("west", self.eight)
        self.four.set_exit("south", self.seven)
        self.four.set_exit("north", self.five)
        self.five.set_exit("west", self.zero)
        self.five.set_exit("south", self.four)
        self.six.set_exit("east", self.zero)
        self.six.set_exit("south", self.ten)
        self.seven.set_exit("north", self.four)
        self.seven.set_exit("south", self.three)
        self.seven.set_exit("west", self.two)
        self.eight.set_exit("north", self.zero)
        self.eight.set_exit("south", self.two)
        self.eight.set_exit("east", self.four)
        self.eight.set_exit("west", self.ten)
        self.nine.set_exit("east", self.three)
        self.nine.set_exit("north", self.one)
        self.ten.set_exit("north", self.six)
        self.ten.set_exit("south", self.one)
        self.ten.set_exit("east", self.eight)

        self.philodendron_places[self.one] = "philodendron subhastatum"
        self.philodendron_places[self.two] = "philodendron blizzard"
        self.philodendron_places[self.three] = "philodendron white wizard"
        self.philodendron_places[self.four] = "philodendron joeppii"
        self.philodendron_places[self.five] = "philodendron majesty"
        self.philodendron_places[self.six] = "philodendron jose buono"
        self.philodendron_places[self.seven] = "philodendron tortum"
        self.philodendron_places[self.eight] = "philodendron jungle fever"
        self.philodendron_places[self.nine] = "philodendron giganteum"
        self.philodendron_places[self.ten] = "philodendron pink princess"

    def play(self):
        """
            The main play loop.
        :return: None
        """
        self.print_welcome()
        logging.info('We are playing!')
        finished = False
        while not finished:
            command = self.textUI.get_command()  # Returns a 2-tuple
            finished = self.process_command(command)
        print("Thank you for playing!")

    def print_welcome(self):
        """
            Displays a welcome message.
        :return: None
        """
        self.textUI.print_to_textUI(" ")
        self.textUI.print_to_textUI("Spiritus Sancti is The Holy Grail of Philodendron, one of the species of Aroids 🌿🌱")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI("You take off from Heathrow airport to find the rarest Philodendron in the world.")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI("While on your way you can collect other philodendrons from various jungles.")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI("Exits: [east, south, west]")
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}')

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'fly', 'search', 'quit']

    def process_command(self, command):
        """
            Process a command from the TextUI.
            :return: True if the game has been quit, False otherwise
        """
        command_word, second_word = command
        if command_word != None:
            command_word = command_word.upper()

        want_to_quit = False
        if command_word == "HELP":
            self.print_help()
        elif command_word == "FLY":
            self.do_go_command(second_word)
        elif command_word == "SEARCH":
            self.philodendron_function()
        elif command_word == "QUIT":
            want_to_quit = True
        else:

            self.textUI.print_to_textUI("Don't know what you mean.")
        return want_to_quit

    def print_help(self):
        """
            Displaying useful help text.
        :return: None
        """
        self.textUI.print_to_textUI("You are well known botanist in the world looking to expand your collection of aroids.")
        self.textUI.print_to_textUI("Choose from directions shown next to each location.")
        self.textUI.print_to_textUI("'Search' command is part of the side quest letting you find other philodendrons.")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')

    def do_go_command(self, second_word):
        """
            Performs the GO command.
        :param second_word: the direction the player wishes to travel in
        :return: None
        """
        if second_word == None:
            # if missing second word...
            self.textUI.print_to_textUI("Fly where?")
            return

        next_place = self.current_place.get_exit(second_word)

        if next_place == None:
            # if the destination does not exist, prints a message
            self.textUI.print_to_textUI('Destination does not exist!')
            # prints the current place description and available command words
            self.textUI.print_to_textUI(self.current_place.get_long_description())
            self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')
        else:
            # updating the current place
            self.current_place = next_place
            # printing description of the new place
            self.textUI.print_to_textUI(self.current_place.get_long_description())
            # decreasing fuel every move
            self.fuel -= 25
            # asking if player wants to go deeper into the jungle
            if self.current_place != self.zero:
                go_deep = input('Do you want to go deeper into the jungle? y/n')
                if go_deep == 'y':
                    self.next_place_func(self.current_place)
#
                if go_deep == 'n':  # if not, prints the current place description and available command words
                    self.textUI.print_to_textUI(self.current_place.get_long_description())
                    self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')
                    self.textUI.print_to_textUI(f"Fuel left: {self.fuel}%")  # prints remaining fuel percentage
                else:

                    self.textUI.print_to_textUI(f"Fuel left: {self.fuel}%")  # prints remaining fuel percentage

            if self.current_place == self.zero:  # if at Heathrow, resets fuel to 100
                self.textUI.print_to_textUI("Fuel is full.")
                self.fuel = 100

            if self.fuel == 0:  # if fuel is 0, prints a message and returns to place 0.
                self.textUI.print_to_textUI(
                    "You've run out of fuel and returned to Heathrow Airport to fill up.")
                self.textUI.print_to_textUI("Fuel is full.")
                self.game_on()

    def philodendron_function(self):
        if self.current_place in self.philodendron_places:  # if the current place has a philodendron rints information about the found philodendron
            philodendron_name = self.philodendron_places[self.current_place]
            print(f'You have found a {philodendron_name} at this location.')
            response = input(f'Do you want to add {philodendron_name} in your backpack? y/n')  # asks the player if he wants to add the philodendron to the backpack
            if response == 'y':
                # attempting to add Philodendron
                while not self.backpack.add_item(philodendron_name):
                    print("Backpack is full!")  # if the backpack is full, asks the player if he wants to remove another philodendron
                    self.display_backpack_contents()
                    philodendron_to_remove = input("Type what Philodendron you want to remove so you can fit a new one in: ").lower()
                    self.remove_philodendron_from_backpack(philodendron_to_remove)
                else:
                    self.backpack.add_item(philodendron_name)
                    logging.info('Philodendron added')
                    print(f'+ {philodendron_name} has now been added to your backpack')  # if added successfully, prints a message and the current place description
                    self.textUI.print_to_textUI(self.current_place.get_long_description())
                    self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')

            elif response == 'n':  # if player chooses not to add the philodendron, prints the current place description
                print(" \n")
                self.textUI.print_to_textUI(self.current_place.get_long_description())
                self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')
            else:
                self.textUI.print_to_textUI("Don't know what you mean.")  # if the response is not recognized, prints a message and the current place description
                self.textUI.print_to_textUI(self.current_place.get_long_description())
                self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')
        else:
            self.textUI.print_to_textUI("You look around, but can not find anything.")  # if no philodendron is found, prints a message and the current place description
            print(" \n")
            self.textUI.print_to_textUI(self.current_place.get_long_description())
            self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')

    def next_place_func(self, current_place):
            if current_place == self.zero:  # if current place is Heathrow, reset fuel to 100
                self.textUI.print_to_textUI("Fuel is full.")
                self.fuel = 100

            if current_place == self.one:  # if current place is 'Amazon Rainforest', initiates the last_game method
                self.textUI.print_to_textUI("Going deeper into the jungle!\n")
                self.last_game()
            # if current place is two to ten, initiates the mini_game method
            if current_place == self.two:
                self.textUI.print_to_textUI("Going deeper into the jungle!\n")
                self.mini_game()

            if current_place == self.three:
                self.textUI.print_to_textUI("Going deeper into the jungle!\n")
                self.mini_game()

            if current_place == self.four:
                self.textUI.print_to_textUI("Going deeper into the jungle!\n")
                self.mini_game()

            if current_place == self.five:
                self.textUI.print_to_textUI("Going deeper into the jungle!\n")
                self.mini_game()

            if current_place == self.six:
                self.textUI.print_to_textUI("Going deeper into the jungle!\n")
                self.mini_game()

            if current_place == self.seven:
                self.textUI.print_to_textUI("Going deeper into the jungle!\n")
                self.mini_game()

            if current_place == self.eight:
                self.textUI.print_to_textUI("Going deeper into the jungle!\n")
                self.mini_game()

            if current_place == self.nine:
                self.textUI.print_to_textUI("Going deeper into the jungle!\n")
                self.mini_game()

            if current_place == self.ten:
                self.textUI.print_to_textUI("Going deeper into the jungle!\n")
                self.mini_game()

            # checking if player run out of fuel
            if self.fuel == 0:
                self.textUI.print_to_textUI("You've run out of fuel and returned to Heathrow Airport to fill up.\n")
                self.game_on()

    def game_on(self):
        # resetting the game
        self.current_place = self.zero
        self.fuel = 100
        print("You are again at Heathrow Airport. Where do you want to fly? Exits: [east, south, west]")

    def last_game(self):
        # special game when player reaches winning place
        import random
        aroid = "Congratulations you found a huge🌿 Spiritus Sancti and your mission is now complete!"
        babyaroid = "Congratulations you found a baby🌱 Spiritus Sancti and your mission is now complete!"

        # randomly choosing between two outcomes
        babyaroid_or_aroid = [babyaroid, aroid]

        # asking the player if he wants to search
        player_input = input("You've just found area of dense vegetation, do you want to search it? (y/n)\n")
        if player_input == 'y':
            outcomes = random.choice(babyaroid_or_aroid)
            print(outcomes)
            self.play_again()
        elif player_input == "n":
            self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')
            self.textUI.print_to_textUI(f"Fuel left: {self.fuel}%")

    def mini_game(self):
        # mini_game when player reaches any other place
        import random
        Snake = "You've been bitten by a poisonous snake🐍 and returned to Heathrow to get some medicine.\n"
        Fuel = "You found can of fuel⛽ and your fuel tank is now full. Where do you want to fly?\n"

        # randomly choosing between two outcomes
        snake_or_fuel = [Snake, Fuel]

        # asking the player if he wants to search
        while input("You've just found area of dense vegetation, do you want to search it? (y/n):\n") == 'y':
            outcome = random.choice(snake_or_fuel)
            print(outcome)

            # handling outcomes
            if outcome == Snake:
                # if snake - player is returned to Heathrow
                self.current_place = self.zero
                self.fuel = 100
                print("You are feeling better now. Where do you want to fly?(east, south, west)\n")
                break

            if outcome == Fuel:
                # if fuel found - players fuel filled
                self.fuel = 100
                self.textUI.print_to_textUI(self.current_place.get_long_description())
                self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')
                break

        else:
            print(" \n")
            self.textUI.print_to_textUI(self.current_place.get_long_description())
            self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')

    def play_again(self):
        # asking if player wants to play again
        answer = input("Do you want to play again? (y/n):\n").lower(). strip()
        if answer == 'y':
            self.game_on()

        else:
            print("Thank you for playing!\n")
            exit()

    def remove_philodendron_from_backpack(self, philodendron_name):
        # removing specific philodendron from backpack
        if self.backpack.check_item(philodendron_name):
            self.backpack.remove_item(philodendron_name)
            print(f'{philodendron_name} removed from backpack.')

        else:
            print(f'You do not have {philodendron_name} in your backpack.')

    def display_backpack_contents(self):
        # displaying contents of backpack
        if not self.backpack.contents:
            print("Your backpack is empty.")
        else:
            print("Collected Philodendrons: ")
            for philodendron in self.backpack.contents:
                print(f' - {philodendron}')


# main function to start the game
def main():
    game = Game()
    game.play()


# running the main function
if __name__ == "__main__":
    main()
