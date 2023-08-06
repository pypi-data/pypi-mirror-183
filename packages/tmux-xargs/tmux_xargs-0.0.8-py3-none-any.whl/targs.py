from argparse import Namespace
from math import ceil

import tmux
from arguments import Parser


def split_and_execute(args: Namespace, cmds: list[str]):
    # Split widnow vertically first.
    tmux.split_window_evenly(args.vertical, vertical=True)

    # Iterate over panes newly created above
    cmd_idx: int = 0
    for _ in range(args.vertical):

        # Split window horizontally
        tmux.split_window_evenly(args.horizontal, vertical=False)

        for _ in range(args.horizontal):
            if len(cmds) == cmd_idx:
                # # of commands can be less than # of pane
                break

            # Execute a command and move right
            tmux.send_keys(cmds[cmd_idx], enter=True)
            tmux.select_pane("R", ntimes=1)
            cmd_idx += 1

        tmux.select_pane("D", ntimes=1)


def main():

    args: Namespace = Parser.parse_args()

    inputs: list[str] = Parser.parse_stdin(delimiter="\n")

    """
    e.g.
    ["ping", "{}"] -> "ping {}"
    """
    cmd = " ".join(args.cmd)

    """
    e.g.
    "ping {}" -> ["ping google.com", "ping github.com"]
    """
    cmds = [cmd.replace(args.replstr, line) if args.replstr else cmd for line in inputs]

    # Iterate over windows
    num_panes: int = args.vertical * args.horizontal
    num_windows: int = ceil(len(cmds) / num_panes)
    for i in range(num_windows):
        tmux.new_window(f"targs{i}")
        split_and_execute(args, cmds[num_panes * i: num_panes * (i + 1)])


if __name__ == "__main__":
    main()
