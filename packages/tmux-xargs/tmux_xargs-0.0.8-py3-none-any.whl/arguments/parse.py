import sys
from argparse import Namespace

from arguments.TargsArgumentParser import TargsArgumentParser


class Parser:
    @staticmethod
    def parse_args() -> Namespace:
        # Configure parser
        parser = TargsArgumentParser(add_help=False, allow_abbrev=False)
        parser.add_argument("--help", action="store_true", help="show this help message and exit")
        parser.add_argument("-h", dest="horizontal", metavar="N", type=int, default=2, help="# of windows in horizontal")
        parser.add_argument("-v", dest="vertical", metavar="N", type=int, default=2, help="# of windows in vertical")
        parser.add_argument("-I", metavar="replstr", dest="replstr", type=str)

        # Modify usage (add " [-- utility [argument ...]]")
        """
        e.g.
        "usage: args.py [--help] [-h N] [-v N] [-I replstr]\n"
        ->
        "args.py [--help] [-h N] [-v N] [-I replstr] [-- utility [argument ...]]\n"
        """
        usage = parser.format_usage().strip()[8:]
        parser.usage = usage + " [-- utility [argument ...]]\n"

        args: Namespace = parser.parse_args()
        if args.help:
            parser.print_help()
            exit()
        return args

    @staticmethod
    def parse_stdin(delimiter="\n") -> list[str]:
        # Read stdin, skipping blank lines
        inputs: list[str] = sys.stdin.read().split(delimiter)
        inputs = [cmd for cmd in inputs if cmd != ""]

        if len(inputs) == 0:
            exit()

        return inputs
