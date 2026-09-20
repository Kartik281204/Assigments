import time
import random
import turtle
import curses
import queue
from curses import wrapper

maze = [[1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 0, 1]]


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_BROWN, curses.COLOR_BLACK)

    stdscr.clear()
    black_and_blue = curses.color_pair(1)
    stdscr.addstr()
    stdscr.refresh()
    stdscr.getch()


if __name__ == "__main__":
    wrapper(main)
