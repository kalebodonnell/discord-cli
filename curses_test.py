import curses
from curses import wrapper
import discord


def main(screen):
    screen.clear()
    currMsg = ''

    while True:
        c = screen.getchw()
        currMsg += c
        screen.addstr(c)


wrapper(main)
