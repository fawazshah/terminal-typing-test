import curses
import time
import sys

from results import Results

ENTER_KEYS = {10, 13}
ESCAPE = 27
BACKSPACE_KEYS = {8, 127}

CORRECT_COLOUR = 1
ERROR_COLOUR = 2

with open("text/stocks-short.txt") as f:
    TEST_STRING = f.read()
    TEST_STRING_LENGTH = len(TEST_STRING)


def print_char(scr, char, colour_profile):
    scr.attron(curses.color_pair(colour_profile))
    y, x = scr.getyx()
    scr.addstr(y, x, char)
    scr.attroff(curses.color_pair(colour_profile))


def wait_for_enter_pressed(scr):
    scr.nodelay(False)
    key = None
    while key not in ENTER_KEYS:
        key = scr.getch()
    return


def print_time(scr, row, start_time, reset_cursor_pos):
    scr.addstr(row, 0, f"Time taken: {round(time.time() - start_time, 0)}s")
    scr.move(4, reset_cursor_pos)


def main(stdscr):
    curses.init_pair(CORRECT_COLOUR, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(ERROR_COLOUR, curses.COLOR_BLACK, curses.COLOR_RED)
    stdscr.nodelay(True)

    curr_char_idx = 0

    stdscr.addstr(0, 0, "Welcome to Typing Test! Press Ctrl-C to quit.")
    stdscr.addstr(4, 0, TEST_STRING)

    results = Results(1, time.time())
    print_time(stdscr, 2, results.start_time, curr_char_idx)

    stdscr.move(4, 0)

    while True:
        try:
            key = stdscr.getch()
            print_time(stdscr, 2, results.start_time, curr_char_idx)
        except KeyboardInterrupt:
            sys.exit()

        if key == curses.ERR:
            pass
        elif key == ESCAPE:
            break
        elif key in BACKSPACE_KEYS:
            y, x = stdscr.getyx()
            if x > 0:
                stdscr.delch(y, x - 1)
        else:
            if curr_char_idx < TEST_STRING_LENGTH - 1:
                if TEST_STRING[curr_char_idx] == " ":
                    results.num_words_typed += 1
                colour_profile = CORRECT_COLOUR if key == ord(TEST_STRING[curr_char_idx]) else ERROR_COLOUR
                print_char(stdscr, TEST_STRING[curr_char_idx], colour_profile)
                curr_char_idx += 1
                stdscr.move(4, curr_char_idx)
            else:
                results.end_time = time.time()
                stdscr.clear()
                results.print_results(stdscr, row=0)
                wait_for_enter_pressed(stdscr)
                break


curses.wrapper(main)
