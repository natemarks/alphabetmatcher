# -*- coding: utf-8 -*-


class Matcher(object):
    """
    Instantiate the object with an input string. Matcher.success() returns True if the input string contains at least
    one of each letter of the alphabet.  I assume case doesn't matter.

    # ex.
    this_matcher = Matcher('111 some string to be tested')

    # use success() to see if the match is successful.  success() returns a boolean value
    status = this_matcher.success()

    """
    def __init__(self, matcher_input):
        """
            :param matcher_input: Some string of characters
            :type matcher_input: str
        """
        # matching without case sensitivity.  normalize to lower in __find_characters()
        self.__interesting_characters = 'abcdefghijklmnopqrstuvwxyz'

        self.__found_characters = []
        """:type : list[str]"""

        self.__find_characters(matcher_input)

    def success(self):
        '''

        :return:
        '''
        for this_char in 'abcdefghijklmnopqrstuvwxyz':
            if this_char not in self.__found_characters:
                return False
        return True

    def __find_characters(self, input):
        # interate through the input
        for this_char in input:
            # if the character is interest and not yet stored in found_characters
            if this_char.lower() in self.__interesting_characters and this_char.lower() not in self.__found_characters:
                self.__found_characters.append(this_char.lower())



