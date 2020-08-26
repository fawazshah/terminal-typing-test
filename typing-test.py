import curses
import time
import sys

ESCAPE = 27
BACKSPACE = 127

TEST_STRING = "Type these words"
TEST_STRING_LENGTH = len(TEST_STRING)

def main(stdscr):
    stdscr.addstr(0, 0, "Welcome to Typing Test! Press Ctrl-C to quit.")
    stdscr.addstr(2, 0, TEST_STRING)
    stdscr.move(2, 0)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

    current_char = 0

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
            y, x = stdscr.getyx()

            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, TEST_STRING[current_char])
            stdscr.attroff(curses.color_pair(1))


            current_char += 1
            stdscr.move(2, current_char)


curses.wrapper(main)
