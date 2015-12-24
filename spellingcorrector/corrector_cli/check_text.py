import logging
import re

from cliff.command import Command

from spellingcorrector.utils import check

class CheckText(Command):
    """check misspelling in the specified file."""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(CheckText, self).get_parser(prog_name)
        parser.add_argument('plan/text', help='input text')
        return parser

    def take_action(self, parsed_args):
        self.log.info('Starting check [%s]',parsed_args['URI'])
        return self.check_text(parsed_args)

    def check_text(self, line):

        for i in ( re.split(r'\s+|[.,/\\\[\]]+', line, flags=re.IGNORECASE) ):
            check.correct()


def check_text(line):
    for i in ( re.split(r'\s+|[.,/\\\[\]]+', line, flags=re.IGNORECASE) ):
        print check.correct(i)

if __name__ == '__main__':
    str = 'today is suday'
    check_text(str)