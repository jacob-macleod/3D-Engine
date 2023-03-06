# Render scene
import curses 
from maths import *

# Set up the screen
screen = curses.initscr()

cube = [
    #x, y, z
    (1, 0, 0),   # Front bottom-left corner
    (4, 0, 0),   # Front bottom-right corner

    (4, 4, 0),   # Front top-right corner
    (1, 4, 0),   # Front top-left corner

    (4, 4, 0),   # Front top-right corner
    (4, 0, 0),   # Front bottom-right corner

    (1, 4, 0),   # Front top-left corner
    (1, 0, 0),   # Front bottom-left corner


    (1, 0, 4),   # Back bottom-left corner
    (4, 0, 4),   # Back bottom-right corner

    (4, 4, 4),   # Back top-right corner
    (1, 4, 4),   # Back top-left corner

    (4, 4, 4),   # Back top-right corner
    (4, 0, 4),   # Back bottom-right corner

    (1, 0, 4),   # Back bottom-left corner
    (1, 4, 4),   # Back top-left corner
]

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
            #print ("VALUES")
            #print (x1)
            #print (y1)
            #print (x2)
            #print (y2)
            #print ("--------")
            draw_line(x1, y1, x2, y2, screen)


    # Wait for user input
    screen.getch()
finally:
    # Restore the terminal
    curses.endwin()
