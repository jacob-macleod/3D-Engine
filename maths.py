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
    return (focal_length*point)/(focal_length+z)

# Draw a diagonal line between two points
"""
Use y-y1 = m(x-x1) and rearrange to find m and c from y = mx + c
m = (delta y)/delta x
From the equations, c = (-m*x1) + y1
x2 and y2 can also be used
"""
def draw_line(x1, y1, x2, y2, screen):
        gradient = (y2-y1)/(x2-x1)
        y_intercept = (-gradient*x1) + y1
        y_points = []

        # Get all x points in line
        if x1 > x2 :
                x_points = np.arange(x2, x1, 1)
        else :
                x_points = np.arange(x1, x2, 1)

        print (x_points)

        # Generate y points and plot
        # Y points are generated from y = mx + c
        for i in range(0, len(x_points)) :

                y_point = round((gradient*x_points[i]) + y_intercept)
                print ("Y: " + str(y_point))
                print("X: " + str(x_points[i]))

        print ("Y: " + str(y2))
        print("X: " + str(x2))      

draw_line(1,1, 3, 5, "screen")