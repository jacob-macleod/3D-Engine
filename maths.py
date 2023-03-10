import math
import curses
import numpy as np

""" Implementation of :
        /          - 1/    d   \ \     
r = xtan|180 - tan    |--------| | + p 
        \             \|c - p| / /  
Basically, find the projected coordinate of a point
This is the old version of the function

def find_point(distance_between_screen_and_camera, point, z, camera_position) :
    d = distance_between_screen_and_camera - z
    x = distance_between_screen_and_camera - d
    print (d)
    print (x)
    
    theta = d/(abs(camera_position-point))
    tan_theta = math.degrees(math.atan(theta))
    print (tan_theta)

    tan_theta_2 = math.tan((180-tan_theta/360)*(2*3.141592654))
    print (tan_theta_2)
    print((x * tan_theta_2))
    return (x * tan_theta_2) + point
"""

"""
New version of the function - much simpler!
The logic can be seen from the code
"""

def find_point(focal_length, point, z) :
    new_point = int(focal_length*point)/(focal_length+z)
    return int(new_point)

# Draw a diagonal line between two points
"""
Use y-y1 = m(x-x1) and rearrange to find m and c from y = mx + c
m = (delta y)/delta x
From the equations, c = (-m*x1) + y1
x2 and y2 can also be used
"""
def draw_line_in_terminal(x1, y1, x2, y2, screen):
        lineDrawn = False
        # If the gradient is not 0
        if (x2-x1) != 0:
                gradient = (y2-y1)/(x2-x1)
        if (x2-x1) == 0:
                # If the gradient is 0, just draw a vertical line
                if y2 > y1:
                        for i in range(y2-y1):
                                screen.addch(x2+i, y2, "█")

                else:
                        for i in range(y1-y2):
                                screen.addch(y2+i, x2, "█")
               
                lineDrawn = True
               
        if lineDrawn == False:
                y_intercept = (-gradient*x1) + y1
                y_points = []

                # Get all x points in line
                if x1 > x2 :
                        x_points = np.arange(x2, x1, 1)
                else :
                        x_points = np.arange(x1, x2, 1)

                # Generate y points and plot
                # Y points are generated from y = mx + c
                for i in range(0, len(x_points)) :

                        y_point = round((gradient*x_points[i]) + y_intercept)
                        screen.addch(y_point, x_points[i], "█")

                screen.addch(y2, x2, '█')  
