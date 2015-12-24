import logging
import re

from cliff.command import Command

from spellingcorrector.utils import check

class CheckFile(Command):
    """check misspelling in the specified file."""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(CheckFile, self).get_parser(prog_name)
        parser.add_argument('URI', help='The location of the file')
        return parser

    def take_action(self, parsed_args):
        self.log.info('Starting check [%s]',parsed_args['URI'])
        self.check_file()

    def check_file(self, file_uri):
        error = []
        with open(file_uri, 'r') as f:
            for i,line in enumerate(f):
                for word in re.split(r'\s+|[.,/\\\[\]]+', line, flags=re.IGNORECASE):
                    corrected = check.correct(word)
                    if word != corrected:
                        error.append((i,word,corrected))
        self.report(error)

    def report(self, error):
        for tup in error:
            print "in line %d\t %s ==> %s\n" % (tup[0],tup[1],tup[2])

# def report(error):
#     for tup in error:
#         print "in line %d\t %s ==> %s\n" % (tup[0],tup[1],tup[2])
#
# error = [(1,'wor','word')]
# report(error)
