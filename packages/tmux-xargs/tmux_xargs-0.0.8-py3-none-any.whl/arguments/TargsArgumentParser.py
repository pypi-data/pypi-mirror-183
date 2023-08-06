import argparse
import sys
from argparse import Namespace


class TargsArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse_args(self, args=None, namespace=None):

        argv = args if args else sys.argv[1:]
        has_util: bool = True
        try:
            sep_idx = argv.index("--")
            if len(argv) == sep_idx + 1:
                has_util = False
                argv = argv[:sep_idx]
        except ValueError:
            has_util = False

        # Parse arguments
        ret_args: Namespace
        if has_util:
            ret_args = super().parse_args(argv[:sep_idx], namespace=namespace)
            setattr(ret_args, "cmd", argv[sep_idx + 1:])
        else:
            ret_args = super().parse_args(argv, namespace=namespace)
            setattr(ret_args, "cmd", ["echo", "{}"])
            setattr(ret_args, "replstr", "{}")

        return ret_args
