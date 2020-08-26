import curses
import time
import sys

ESCAPE = 27
BACKSPACE = 127

CORRECT_COLOUR = 1
ERROR_COLOUR = 2

TEST_STRING = "Type these words"
TEST_STRING_LENGTH = len(TEST_STRING)


def main(stdscr):
    stdscr.addstr(0, 0, "Welcome to Typing Test! Press Ctrl-C to quit.")
    stdscr.addstr(2, 0, TEST_STRING)
    stdscr.move(2, 0)

    curses.init_pair(CORRECT_COLOUR, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(ERROR_COLOUR, curses.COLOR_BLACK, curses.COLOR_RED)

    curr_char_idx = 0

    while True:
        try:
            key = stdscr.getch()
        except KeyboardInterrupt:
            sys.exit()

        if key == ESCAPE:
            break
        elif key == BACKSPACE:
            y, x = stdscr.getyx()
            if x > 0:
                stdscr.delch(y, x - 1)
        else:
            if curr_char_idx >= TEST_STRING_LENGTH - 1:
                sys.exit()

            colour_profile = CORRECT_COLOUR if key == ord(TEST_STRING[curr_char_idx]) else ERROR_COLOUR

            stdscr.attron(curses.color_pair(colour_profile))
            y, x = stdscr.getyx()
            stdscr.addstr(y, x, TEST_STRING[curr_char_idx])
            stdscr.attroff(curses.color_pair(colour_profile))

            curr_char_idx += 1
            stdscr.move(2, curr_char_idx)


curses.wrapper(main)
