# Render scene
import curses 
from maths import *

# Set up the screen
screen = curses.initscr()

cube = [
    #x, y, z
    (6, 2, 2),   # Front bottom-left corner
    (9, 2, 2),   # Front bottom-right corner

    (9, 6, 2),   # Front top-right corner
    (8, 6, 2),   # Front top-left corner

    (9, 6, 2),   # Front top-right corner
    (9, 2, 2),   # Front bottom-right corner

    (6, 6, 2),   # Front top-left corner
    (6, 2, 2),   # Front bottom-left corner

    (6, 2, 6),   # Back bottom-left corner
    (9, 2, 6),   # Back bottom-right corner

    (9, 6, 6),   # Back top-right corner
    (6, 6, 6),   # Back top-left corner

    (9, 6, 6),   # Back top-right corner
    (9, 2, 6),   # Back bottom-right corner

    (6, 6, 6),   # Back top-left corner
    (6, 2, 6),   # Back bottom-left corner
]



focal_length = 10

try :
    # Set up the page
    screen.border(0)
    curses.start_color()
    # Set up the red color
    curses.init_color(10, 1000, 0, 0)
    # Set up the color pair
    curses.init_pair(1, curses.COLOR_WHITE, 10)

    screen.addstr(10, 10, '█')

    
    #draw_line(1,1, 1, 5, screen)
    # Draw the cube
    for i in range(0, len(cube)) :
        # If i = 0, 2, 4, 6, etc
        if ((i%2) == 0):
            # Draw the line
            x1, y1, z1 = cube[i]
            x2, y2, z2 = cube[i+1]

            x1 = find_point(focal_length, x1, z1)
            y1 = find_point(focal_length, y1, z1)
            x2 = find_point(focal_length, x2, z2)
            y2 = find_point(focal_length, y2, z2)
            draw_line_in_terminal(x1, y1, x2, y2, screen)


    # Wait for user input
    screen.getch()
finally:
    # Restore the terminal
    curses.endwin()
