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
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)

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
            y, x = stdscr.getyx()

            if curr_char_idx < TEST_STRING_LENGTH - 1:

                if key == ord(TEST_STRING[curr_char_idx]):
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y, x, TEST_STRING[curr_char_idx])
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.attron(curses.color_pair(2))
                    stdscr.addstr(y, x, TEST_STRING[curr_char_idx])
                    stdscr.attroff(curses.color_pair(2))

            else:
                sys.exit()


            curr_char_idx += 1
            stdscr.move(2, curr_char_idx)


curses.wrapper(main)
