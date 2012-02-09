"""
Class for argument parsing
"""


class Argument(object):

    def __init__(self, name='', help='', choices=None, prefix='-', type=str):

        """
        Abstract the Argument data into a class so we can keep code tidy
        """

        self.name = prefix+name
        self.data = dict(help=help,
                         choices=choices,
                         type=str)