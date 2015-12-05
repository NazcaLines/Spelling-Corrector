import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class Corrector(App):

    def __init__(self):
        super(Corrector, self).__init__(
            description='spelling-corrector',
            version='0.1',
            command_manager=CommandManager('corrector'),
            deferred_help=True
        )


def main(argv=sys.argv[1:]):
    corrector = Corrector()
    return corrector.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
