# colorcurses.py
# Evan J Parker (@leftbones)
# github.com/leftbones/colorcurses

import curses

class Colorizer:
    def __init__(self, stdscr, warnings=True):
        curses.start_color()
        curses.use_default_colors()

        self.stdscr = stdscr
        self.warnings = warnings

        if self.warnings:
            if not curses.can_change_color():
                print("Your terminal does not support color modification, ColorCurses will not work properly. Suppress this message by setting 'warnings=False' on Colorizer()")
            
            if not curses.has_extended_color_support(): # FIXME reports iTerm2 as not having extended colors for some reason?
                print("If you see this message, your terminal may not have extended color support. If you know it does, you can ignore this message, suppress this message by setting 'warnings=False' on Colorizer()")

        self.colors = {
            "None":    -1, # Using this matches the default foreground/background color of your terminal, depending where it's used in a color pair
            "cBlack":   0, # The default curses colors are prefixed with "c" so the names can be reused by the user
            "cRed":     1,
            "cGreen":   2,
            "cYellow":  3,
            "cBlue":    4,
            "cMagenta": 5,
            "cCyan":    6,
            "cWhite":    7
        }

        self.pairs = {}

        self.color_idx = 8 # Start adding new colors at 8 to avoid overriding the curses defaults
        self.pair_idx = 1 # 0 is hard-coded to be white on black and can't be changed, index from 1 instead


    # Color Management
    # --------------------

    # Add a new color to the colors dictionary using standard RGB, converted to the 0-1000 values used in curses
    def add_color(self, name, r, g, b):
        if name in self.colors:
            print(f"Failed to add color '{name}' as it already exists. To modify an existing color, use UpdateColor()")
            return
        curses.init_color(self.color_idx, int(r/0.255), int(g/0.255), int(b/0.255))
        self.colors.update({name: self.color_idx})
        self.color_idx += 1

    # Remove a color from the colors dictionary by name, leaving the index empty (probably never worth using, honestly)
    def delete_color(self, name):
        self.colors.pop(name)

    # Replace a color in the colors dictionary, overwriting the existing values, allows changing some values while keeping others
    def update_color(self, name, r=None, g=None, b=None):
        if not name in self.colors:
            print(f"Failed to update color '{name}', color was not found.")
            return
        idx = self.colors.get(name)
        values = curses.color_content(idx)
        if not r: r = values[0]
        if not g: g = values[1]
        if not b: b = values[2]
        curses.init_color(idx, int(r/0.255), int(g/0.255), int(b/0.255))


    # Pair Management
    # --------------------

    # Add a new color pair to the pairs dictionary with a name, foreground color, and background color
    def add_pair(self, name, fg, bg):
        if name in self.pairs:
            print(f"Failed to add pair '{name}', it already exists! To modify an existing pair, use UpdatePair()")
            return
        fg_color = self.colors.get(fg)
        bg_color = self.colors.get(bg)
        curses.init_pair(self.pair_idx, fg_color, bg_color)
        self.pairs.update({name: self.pair_idx})
        self.pair_idx += 1

    # Remove a pair from the pairs dictionary by name, leaving the index empty (also probably never worth using)
    def delete_pair(self, name):
        self.pairs.pop(name)

    # Replace a pair in the pairs dictionary, overwriting the existing values, allows changing one value while keeping the other
    def update_pair(self, name, fg=None, bg=None):
        if not name in self.pairs:
            print(f"Failed to update pair '{name}', pair was not found.")
            return
        idx = self.pairs.get(name)
        values = curses.pair_content(idx)
        if not fg: fg_color = values[0]
        else: fg_color = self.colors.get(fg)
        if not bg: bg_color = values[1]
        else: bg_color = self.colors.get(bg)
        curses.init_pair(idx, fg_color, bg_color)


    # Char Function Wrappers
    # -------------------------
    # [-] addch()
    # [-] insch()

    def addch(self, y, x, ch, color_pair, window=None):
        if not window: window = self.stdscr
        pair = self.pairs.get(color_pair)
        window.addch(y, x, ch, curses.color_pair(pair))

    def insch(self, y, x, ch, color_pair, window=None):
        if not window: window = self.stdscr
        pair = self.pairs.get(color_pair)
        window.insch(y, x, ch, curses.color_pair(pair))


    # Str Function Wrappers
    # -------------------------
    # [-] addstr()
    # [ ] addnstr()
    # [ ] insstr()
    # [ ] insnstr()

    def addstr(self, y, x, string, color_pair, window=None):
        if not window: window = self.stdscr
        pair = self.pairs.get(color_pair)
        window.addstr(y, x, string, curses.color_pair(pair))

    def addnstr(self, window=None):
        if not window: window = self.stdscr
        pass

    def insstr(self, window=None):
        if not window: window = self.stdscr
        pass

    def insnstr(self, window=None):
        if not window: window = self.stdscr
        pass
