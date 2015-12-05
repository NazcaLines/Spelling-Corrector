import logging

from cliff.command import Command

from spellingcorrector.utils import check

class CheckText(Command):
    """check misspelling in the specified file."""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(CheckText, self).get_parser(prog_name)
        parser.add_argument('URI', help='The location of the file')
        return parser

    def take_action(self, parsed_args):
        self.log.info('Starting check [%s]',parsed_args['URI'])
        return check.check()
