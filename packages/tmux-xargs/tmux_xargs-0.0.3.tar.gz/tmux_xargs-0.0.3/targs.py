from argparse import Namespace
from math import ceil

import tmux
from arguments import ArgumentParser, parse_stdin


def split_and_execute(args: Namespace, cmds: list[str]):
    # Split widnow vertically first.
    tmux.split_window_evenly(args.height, vertical=True)

    # Iterate over panes newly created above
    cmd_idx: int = 0
    for _ in range(args.height):

        # Split window horizontally
        tmux.split_window_evenly(args.width, vertical=False)

        for _ in range(args.width):
            if len(cmds) == cmd_idx:
                # # of commands can be less than # of pane
                break

            # Execute a command and move right
            tmux.send_keys(cmds[cmd_idx], enter=True)
            tmux.select_pane("R", ntimes=1)
            cmd_idx += 1

        tmux.select_pane("D", ntimes=1)


def main():
    # Configure parser
    parser = ArgumentParser(usage="%(prog)s [options] [-- utility [argument ...]]")
    parser.add_argument("--width", type=int, default=2)
    parser.add_argument("--height", type=int, default=2)
    parser.add_argument("-I", metavar="replstr", dest="replstr", type=str)

    args: Namespace = parser.parse_args()

    inputs: list[str] = parse_stdin(delimiter="\n")
    cmd = " ".join(args.cmd)
    cmds = [cmd.replace(args.replstr, line) if args.replstr else args.cmd for line in inputs]

    # Iterate over windows
    num_panes: int = args.height * args.width
    num_windows: int = ceil(len(cmds) / num_panes)
    for i in range(num_windows):
        tmux.new_window(f"targs{i}")
        split_and_execute(args, cmds[num_panes * i: num_panes * (i + 1)])


if __name__ == "__main__":
    main()
