# targs
tmux + xargs

## Install

```bash
pip install git+https://github.com/ucchiee/targs.git
```

## Usage

`targs` reads newline delimited strings from the standard input and executes each of them in the automatically created panes.

e.g.:

```bash
$ cat scripts
# echo 1
# echo 2
# echo 3
# echo 4

$ tmux
$ cat scripts | targs
```
