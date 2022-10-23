"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This file shows a window with a line chart
that user can search for rankings by different names during 1900-2010.

"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    year_width = (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)  # distance between every vertical line(year)
    x = GRAPH_MARGIN_SIZE + year_width * year_index
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,                        # add upper horizontal line
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,        # add lower horizontal line
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0,                    # add vertical lines
                           get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX,             # add years
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        color = COLORS[i % len(COLORS)]
        name = lookup_names[i]
        for j in range(len(YEARS)-1):
            year = name_data[name]
            x1 = get_x_coordinate(CANVAS_WIDTH, j)          # start x-point
            x2 = get_x_coordinate(CANVAS_WIDTH, j+1)        # end x-point
            if str(YEARS[j]) in year:                       # when year <= 1000
                rank = year[str(YEARS[j])]
                y1 = GRAPH_MARGIN_SIZE+int(rank)*(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK   # start y-point
            else:                                           # when year > 1000
                rank = '*'
                y1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE        # start y-point(year > 1000)
            if str(YEARS[j+1]) in year:                     # when year <= 1000
                rank2 = year[str(YEARS[j+1])]
                y2 = GRAPH_MARGIN_SIZE+int(rank2)*(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK  # end y-point
            else:                                           # when year > 1000
                rank2 = '*'
                y2 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE        # end y-point(year > 1000)
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
            canvas.create_text(x1+TEXT_DX, y1, text=f"{name} {rank}", anchor=tkinter.SW, fill=color)
            if j == len(YEARS)-2:                               # print last year's name and rank
                canvas.create_text(x2+TEXT_DX, y2, text=f"{name} {rank2}", anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
