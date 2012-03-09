"""
Class for argument parsing
"""


class Argument(object):

    def __init__(self, name, required=False,
                 help='', choices=None,
                 prefix='-', type=str,
                 default='', nargs=None):

        """
        Abstract the Argument data into a class so we can keep code tidy
        """

        self.name = prefix+name
        self.data = dict(
                         help=help,
                         choices=choices,
                         type=type,
                         required=required,
                         default=default,
                         nargs=nargs
                    )