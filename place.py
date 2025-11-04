"""
Defines Places class
"""

class Place:

    def __init__(self, description):
        """
            Constructor method.
        :param description: Text description for this place
        """
        self.description = description
        self.exits = {}  # Dictionary
        self.philodendron_places = {}

    def set_exit(self, direction, neighbour):
        """
            Adds an exit for a place. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, place).
        :param direction: The direction leading out of this place
        :param neighbour: The place that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour

    def get_short_description(self):
        """
            Fetch a short text description.
        :return: text description
        """
        return self.description

    def get_long_description(self):
        """
            Fetch a longer description including available exits.
        :return: text description
        """
        return f'Location: {self.description}, Exits: {self.get_exits()}.'

    def get_exits(self):
        """
            Fetch all available exits as a list.
        :return: list of all available exits
        """
        all_exits = list(self.exits.keys())
        return all_exits

    def get_exit(self, direction):
        """
            Fetch an exit in a specified direction.
        :param direction: The direction that the player wishes to travel
        :return: Place object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None
