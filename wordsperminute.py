import time
import os
import random
import curses
from curses import wrapper


def display_text(stdscr, target, current, wpm=0, correctness=0):
    stdscr.addstr(target)
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(3)
        if char != correct_char:
            color = curses.color_pair(5)
        stdscr.addstr(0, i, char, color)
    stdscr.addstr(5, 5, f"WPM : {wpm}", curses.color_pair(6))


def load_text():
    with open("words.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    accuracy = 0
    while True:
        stdscr.clear()
        elapsed_time = max(time.time() - start_time, 1)
        display_text(stdscr, target_text, current_text, wpm, accuracy)
        stdscr.refresh()
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
                continue
        elif len(current_text) < len(target_text):
            current_text.append(key)


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 9, "TYPE MONKEY", curses.color_pair(1))
    stdscr.addstr("\nPRESS ANY KEY TO START", curses.color_pair(2))
    stdscr.refresh()
    key = stdscr.getkey()


def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_CYAN)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(
            "\n You have finished the game ,press any key to continue")
        stdscr.refresh()
        key = stdscr.getkey()
        if ord(key) == 27:
            break
        else:
            continue


wrapper(main)
