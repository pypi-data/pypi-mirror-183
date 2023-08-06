import argparse
import sys
from argparse import Namespace


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse_args(self, args=None, namespace=None):

        argv = sys.argv if not args else args
        has_util: bool = True
        try:
            sep_idx = argv.index("--")
            has_util = len(argv) > sep_idx + 1  # Check `utility` is given
        except ValueError:
            has_util = False

        # Parse arguments
        ret_args: Namespace
        if has_util:
            ret_args = super().parse_args(sys.argv[1:sep_idx], namespace=namespace)
            setattr(ret_args, "cmd", sys.argv[sep_idx + 1:])
        else:
            ret_args = super().parse_args(namespace=namespace)
            setattr(ret_args, "cmd", ["echo", "{}"])
            setattr(ret_args, "replstr", "{}")

        return ret_args
