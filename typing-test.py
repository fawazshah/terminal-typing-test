import curses
import time
import sys

ESCAPE = 27
BACKSPACE = 127

def main(stdscr):
    stdscr.addstr(0, 0, "Welcome to Typing Test! Press q to quit.")
    stdscr.move(1, 0)

    while True:
        try:
            key = stdscr.getch()
        except KeyboardInterrupt:
            sys.exit()

        if key == ord('q') or key == ESCAPE:
            break
        elif key == BACKSPACE:
            y, x = stdscr.getyx()
            if x > 0:
                stdscr.delch(y, x-1)
        else:
            y, x = stdscr.getyx()
            stdscr.addstr(y, x, chr(key))


curses.wrapper(main)
