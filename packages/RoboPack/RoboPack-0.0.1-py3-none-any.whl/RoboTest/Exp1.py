from robot.api.deco import library
from robot.api.deco import keyword


@library
class Exp1:  # pylint: disable=too-many-public-methods
    """ Connection class """
    def __init__(self):
        self.log = None

    @keyword
    def list_to_dict(self, list1, list2):
        """Simple method to convert list to dict"""
        self.log = None
        dictionary = dict(zip(list1, list2))
        print(dictionary)
        return dictionary
