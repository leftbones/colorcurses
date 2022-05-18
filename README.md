# ColorCurses

I got fed up with how janky the highlighting system in curses was, so I wrote this to help make it easier. Or at least, more organized. It's only about 150 lines, all there is is the Colorizer class that manages all colors and color pairs with a few simple commands. The Colorizer also contains wrappers for a few of the printing functions from curses. Not all of them are implemented yet, so far I've just added the most important few: addch, insch, and addstr.

## Planned Updates
* Finish wrapping the rest of the character/string functions
* Implement curses attributes (bold, underline, dim, etc.)
* Colorizing regex matches within strings (syntax highlighting?)

## Installation

Install using pip, like you would any other package. This is only verified to work with Python 3.

``````
pip install colorcurses
``````

## Usage

Using this is dead simple, if you're at all familiar with curses, you should be able to figure out how to use it based on the following example.

```
import curses
import colorcurses

def main(stdscr):
    stdscr.clear()
    cc = colorcurses.Colorizer(stdscr) # create a new Colorizer instance

    cc.add_color("yellow", 255, 0, 0) # add new named colors by rgb values
    cc.add_color("blue", 0, 0, 255)

    cc.add_pair("yellow on blue", "yellow", "blue") # create a foreground/background color pair

    cc.addstr(0, 0, "Coloring text in curses is no longer painful!", "yellow on blue") # call the standard curses print functions through the Colorizer instead of curses

    stdscr.getch()

if __name__ == '__main__':
    stdscr = curses.initscr()
    curses.cbreak()
    main(stdscr)
    curses.endwin()
```

There are a few more things not covered in the example, I'll explain those here.

* Though you are required to pass in a curses window when initializing the Colorizer, you can print to any curses window you want by passing it in to the printing functions, such as `cc.addstr(0, 0, "Colors!", window)`, if a window isn't passed in, the functions automatically fall back to whatever window you passed in when setting up the Colorizer.
* Once added, colors and color pairs can be updated via the `update_color()` and `update_pair()` functions. These also allow updating only specific values. For example, if you call `update_color("myColor", r=255)`, only the `r` value of `myColor` will be changed. The same goes for changing only the foreground or background color of a pair using `update_pair()`.
* Colors and color pairs can also be deleted using `delete_color()` and `delete_pair()`, though I don't really think this will ever be useful to anyone. I mostly implemented it just in case someone *does* find a use for it. Colors and color pairs are stored in a dictionary, so deleting them leaves an empty space in the dictionary, which can't ever be filled in again, at least for now.
* The default colors present in curses are still available in the Colorizer, they are under their original names, only prefixed with `c`, such as `cRed`. I did this so you can reuse the names for your own colors without overwriting the defaults.
* Speaking of overwriting the defaults, the indexing of new colors added with `add_color()` starts at 8, again to avoid overwriting the default colors. The indexing for color pairs starts at 1, because index 0 is hard-coded to be white on black, and can't be overwritten.
* The Colorizer automatically calls `curses.use_default_colors()`, which allows you to use the color `None` built into the Colorizer as a way to tell curses to use the default foreground or background color of your terminal, depending on where in a color pair it's placed.
* Lastly, I added a check for `curses.can_change_color()` and `curses.has_extended_color_support()` to show warning message if either one returns false, but I'm not confident that they work properly, as the latter returns false in iTerm2, which has no issues with extended color support as far as I know. If you're sick of the warnings, you can set `warnings=False` on the Colorizer to suppress them.

That's it! If I forgot something, or something is broken, or maybe you want to request features, I encourage you to open an issue. Thanks!
