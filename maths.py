import math

""" Implementation of :
        /          - 1/    d   \ \     
r = xtan|180 - tan    |--------| | + p 
        \             \|c - p| / /  
Basically, find the projected coordinate of a point
"""

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

print(find_point(100, 20, 40, 30))
