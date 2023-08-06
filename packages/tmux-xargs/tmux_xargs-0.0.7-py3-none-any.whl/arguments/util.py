import sys


def parse_stdin(delimiter="\n") -> list[str]:
    # Read commands, skipping blank lines
    inputs: list[str] = sys.stdin.read().split(delimiter)
    inputs = [cmd for cmd in inputs if cmd != ""]

    if len(inputs) == 0:
        exit()

    return inputs
