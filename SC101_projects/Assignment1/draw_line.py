"""
File: draw_line.py
Name: Sharon
-------------------------
This file shows drawing line with two clicks
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the GOval
SIZE = 5

# global variable
window = GWindow()
circle = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(first)


def first(event):
    global circle
    window.add(circle, x=event.x-SIZE/2, y=event.y-SIZE/2)
    onmouseclicked(second)


def second(event):
    line = GLine(circle.x+SIZE/2, circle.y+SIZE/2, event.x, event.y)
    window.add(line)
    window.remove(circle)     # remove the circle
    onmouseclicked(first)


if __name__ == "__main__":
    main()
