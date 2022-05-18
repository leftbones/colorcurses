# colortest.py
# Evan J Parker (@leftbones)
# github.com/leftbones/colorcurses

import curses
from colorcurses import *

def main(stdscr):
    stdscr.clear()
    cc = Colorizer(stdscr, warnings=False)

    # Rainbow with custom colors (fg+bg and just fg)
    cc.add_color("Black", 0, 0, 0)
    cc.add_color("White", 255, 255, 255)
    cc.add_color("Red", 246, 0, 0)
    cc.add_color("Orange", 255, 140, 0)
    cc.add_color("Yellow", 255, 238, 0)
    cc.add_color("Green", 77, 233,76)
    cc.add_color("Blue", 55, 131, 255)
    cc.add_color("Violet", 72, 21, 170)

    cc.add_pair("WhiteOnRed", "White", "Red")
    cc.add_pair("BlackOnOrange", "Black", "Orange")
    cc.add_pair("BlackOnYellow", "Black", "Yellow")
    cc.add_pair("BlackOnGreen", "Black", "Green")
    cc.add_pair("WhiteOnBlue", "White", "Blue")
    cc.add_pair("WhiteOnViolet", "White", "Violet")

    cc.add_pair("JustRed", "Red", "None")
    cc.add_pair("JustOrange", "Orange", "None")
    cc.add_pair("JustYellow", "Yellow", "None")
    cc.add_pair("JustGreen", "Green", "None")
    cc.add_pair("JustBlue", "Blue", "None")
    cc.add_pair("JustViolet", "Violet", "None")

    stdscr.addstr(0, 0, "Using foreground and background colors:")
    cc.addstr(1, 0, "white on red", "WhiteOnRed")
    cc.addstr(2, 0, "black on orange", "BlackOnOrange")
    cc.addstr(3, 0, "black on yellow", "BlackOnYellow")
    cc.addstr(4, 0, "black on green", "BlackOnGreen")
    cc.addstr(5, 0, "white on blue", "WhiteOnBlue")
    cc.addstr(6, 0, "white on violet", "WhiteOnViolet")

    stdscr.addstr(8, 0, "Using foreground colors with the default background color:")
    cc.addstr(9, 0, "just red", "JustRed")
    cc.addstr(10, 0, "just orange", "JustOrange")
    cc.addstr(11, 0, "just yellow", "JustYellow")
    cc.addstr(12, 0, "just green", "JustGreen")
    cc.addstr(13, 0, "just blue", "JustBlue")
    cc.addstr(14, 0, "just violet", "JustViolet")


    # Per-character coloring
    cc.add_color("AppleGreen", 94, 189, 62)
    cc.add_color("AppleYellow", 255, 185, 0)
    cc.add_color("AppleOrange", 247, 130, 0)
    cc.add_color("AppleRed", 226, 56, 56)
    cc.add_color("AppleViolet", 151, 57, 153)
    cc.add_color("AppleBlue", 0, 156, 223)

    cc.add_pair("A1", "AppleGreen", "None")
    cc.add_pair("A2", "AppleYellow", "None")
    cc.add_pair("A3", "AppleOrange", "None")
    cc.add_pair("A4", "AppleRed", "None")
    cc.add_pair("A5", "AppleViolet", "None")
    cc.add_pair("A6", "AppleBlue", "None")

    stdscr.addstr(16, 0, "Per character coloring:")
    cc.addch(17, 0, 'C', "A1")
    cc.addch(17, 1, 'O', "A2")
    cc.addch(17, 2, 'L', "A3")
    cc.addch(17, 3, 'O', "A4")
    cc.addch(17, 4, 'R', "A5")
    cc.addch(17, 5, 'S', "A6")

    # Per-character coloring in a loop
    stdscr.addstr(19, 0, "Per character coloring in a for loop:")

    colors = ["A1", "A2", "A3", "A4", "A5", "A6"]
    string = "This colorful string was printed character by character with a for loop, in six colors!"
    idx = 0

    for i, c in enumerate(string):
        if idx > len(colors) - 1: idx = 0
        cc.addch(20, i, c, colors[idx])
        if c != ' ': idx += 1


    stdscr.getkey()
    curses.endwin()

if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.cbreak()
    main(stdscr)
