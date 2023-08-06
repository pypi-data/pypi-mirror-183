# PgTTY

A terminal for Python using Pygame.

To install, run `pip3 install pgtty`

Note: If you are using Python3.11, you need to run `pip3 install pygame --pre` first.

## Usage

To initialise pgtty, run `display = pgtty.PgTTY()`

There is an example program in `main.py` in the github repository.

The main functions are:

#### `display.print(text)`

This prints to the screen based on where the pointer is. Optional arguments are foreground and background in the form (r, g, b) to add color. This function automatically runs `display.update()` after.

#### `display.set((y, x), char)`

This sets a certain character on the screen at `x, y` to `char`. It also supports foreground and background colors as mentioned above.

Note: This does not update the screen, you have to run `display.update()` after.

#### `display.update()`

This updates the screen. 

#### `display.foreground = (127, 127, 127)`

This is a variable set to grey as default. This is the default foreground color of the text you print or set, unless specified in keyword arguments.

#### `display.background = (0, 0, 0)`

Same as foreground, but in the background

#### `display.pointer = (y, x)`

This defines where the pointer is for `display.print()`