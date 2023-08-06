import argparse
import os
import sys
from argparse import Namespace
from math import ceil


def split_window_evenly(splitnum: int, vertical: bool = True) -> int:
    tmux_cmd = "tmux "
    for idx, i in enumerate(reversed(range(splitnum))):
        if i == 0:
            break
        tmux_cmd += "split-window "
        tmux_cmd += f"{'-v' if vertical else '-h'} "
        tmux_cmd += f"-l {100 - int(100 * i / (splitnum - idx))}% "
        tmux_cmd += "-d \\; "
    return os.system(tmux_cmd)


def send_keys(cmd: str, enter: bool = True) -> int:
    tmux_cmd = f"tmux send-keys '{cmd}' {'Enter' if enter else ''}"
    return os.system(tmux_cmd)


def select_pane(direction: str, ntimes: int = 1) -> int:
    assert direction in ["U", "D", "R", "L"]

    tmux_cmd = "tmux "
    for _ in range(ntimes):
        tmux_cmd += f"select-pane -{direction}\\; "
    return os.system(tmux_cmd)


def new_window(name: str = "") -> int:
    tmux_cmd = "tmux new-window"
    if name:
        tmux_cmd += f" -n {name}"
    return os.system(tmux_cmd)


def split_and_execute(args: Namespace, cmds: list[str]):
    # Split widnow vertically first.
    split_window_evenly(args.height, vertical=True)

    # Iterate over panes newly created above
    cmd_idx: int = 0
    for _ in range(args.height):

        # Split window horizontally
        split_window_evenly(args.width, vertical=False)

        for _ in range(args.width):
            if len(cmds) == cmd_idx:
                # # of commands can be less than # of pane
                break

            # Execute a command and move right
            send_keys(cmds[cmd_idx], enter=True)
            select_pane("R", ntimes=1)
            cmd_idx += 1

        select_pane("D", ntimes=1)


def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=2)
    parser.add_argument("--height", type=int, default=2)
    args: Namespace = parser.parse_args()

    # Read commands, skipping blank lines
    cmds: list[str] = sys.stdin.read().split("\n")
    cmds = [cmd for cmd in cmds if cmd != ""]

    if len(cmds) == 0:
        print("Specify commands to execute")
        exit()

    # Iterate over windows
    num_panes: int = args.height * args.width
    num_windows: int = ceil(len(cmds) / num_panes)
    for i in range(num_windows):
        new_window(f"targs{i}")
        split_and_execute(args, cmds[num_panes * i: num_panes * (i + 1)])


if __name__ == "__main__":
    main()
