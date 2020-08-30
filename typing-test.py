import curses
import time
import sys

ENTER_KEYS = {10, 13}
ESCAPE = 27
BACKSPACE_KEYS = {8, 127}

CORRECT_COLOUR = 1
ERROR_COLOUR = 2

TEST_STRING = "Type these words"
TEST_STRING_LENGTH = len(TEST_STRING)

SCORE = 0


def print_char(scr, char, colour_profile):
    scr.attron(curses.color_pair(colour_profile))
    y, x = scr.getyx()
    scr.addstr(y, x, char)
    scr.attroff(curses.color_pair(colour_profile))


def wait_for_enter_pressed(scr):
    scr.nodelay(0)
    key = None
    while key not in ENTER_KEYS:
        key = scr.getch()
    return


def main(stdscr):
    stdscr.addstr(0, 0, "Welcome to Typing Test! Press Ctrl-C to quit.")
    stdscr.addstr(2, 0, TEST_STRING)
    stdscr.move(2, 0)

    curses.init_pair(CORRECT_COLOUR, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(ERROR_COLOUR, curses.COLOR_BLACK, curses.COLOR_RED)

    curr_char_idx = 0

    num_words_typed = 1

    start_time = time.time()

    while True:
        try:
            key = stdscr.getch()
        except KeyboardInterrupt:
            sys.exit()

        if key == ESCAPE:
            break
        elif key in BACKSPACE_KEYS:
            y, x = stdscr.getyx()
            if x > 0:
                stdscr.delch(y, x - 1)
        else:
            if curr_char_idx < TEST_STRING_LENGTH - 1:
                if TEST_STRING[curr_char_idx] == " ":
                    num_words_typed += 1
                colour_profile = CORRECT_COLOUR if key == ord(TEST_STRING[curr_char_idx]) else ERROR_COLOUR
                print_char(stdscr, TEST_STRING[curr_char_idx], colour_profile)
                curr_char_idx += 1
                stdscr.move(2, curr_char_idx)
            else:
                end_time = time.time()
                time_taken = end_time - start_time
                stdscr.clear()
                stdscr.addstr(0, 0, f"Your time is {round(time_taken, 3)}.")
                stdscr.addstr(1, 0, f"Your number of words typed is {num_words_typed}.")
                stdscr.addstr(2, 0, f"Your WPM is {round(num_words_typed / time_taken * 60, 3)}. Press Enter to quit.")
                wait_for_enter_pressed(stdscr)
                break


curses.wrapper(main)
