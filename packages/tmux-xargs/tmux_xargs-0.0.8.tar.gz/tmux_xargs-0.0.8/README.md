# targs
tmux + xargs = targs

## Install

```bash
pip install git+https://github.com/ucchiee/targs.git
# or
pip install tmux-xargs
```

## Usage

`targs` reads newline delimited strings from the standard input and executes utility with the strings as arguments.

e.g.:

```bash
$ cat ./etc/domains.txt
# google.com
# apple.com
# facebook.com
# amazon.com

$ tmux
$ cat ./etc/domains.txt | targs -I {} -- ping {}
```
