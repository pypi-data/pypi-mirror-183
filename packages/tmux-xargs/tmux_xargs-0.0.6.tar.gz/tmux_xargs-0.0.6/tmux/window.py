import os


def split_window_evenly(splitnum: int, vertical: bool = True) -> int:
    tmux_cmd = "tmux "
    for idx, i in enumerate(reversed(range(splitnum))):
        if i == 0:
            break
        tmux_cmd += "split-window "
        tmux_cmd += f"{'-v' if vertical else '-h'} "
        tmux_cmd += f"-p {100 - int(100 * i / (splitnum - idx))} "
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
