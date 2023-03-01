# Render scene
import curses 
from maths import *

# Set up the screen
screen = curses.initscr()

try :
    # Set up the page
    screen.border(0)
    curses.start_color()
    # Set up the red color
    curses.init_color(10, 1000, 0, 0)
    # Set up the color pair
    curses.init_pair(1, curses.COLOR_WHITE, 10)

    screen.addstr(10, 10, '█')

    
    height, width = screen.getmaxyx()

    # Calculate slope and y-intercept
    m = height / width
    b = 0

    # Loop through x-coordinates
    for x in range(width):
        # Calculate y-coordinate
        y = int(m * x + b)
        # Print character at (x,y)
        screen.addch(y, x, "*")

    # Wait for user input
    screen.getch()
finally:
    # Restore the terminal
    curses.endwin()
