# 3D-Engine
A custom 3D engine made with python

## Mathematics
This 3D engine is based on some mathematics which I have derived. Below, you can see the main equation, to find where a point should be based on a number of variables:

* l = distance between screen and camera

* z = z position of point to plot

* d = l-z = distance from point to camera

* x = d-l = distance from point to screen

* c = x or y position of camera

* p = x or y position of point

* r = resultant x or y position of point



        '/          - 1'/    d   '\ '\     
r = xtan|180 - tan    |--------| | + p 
        \             \|c - p| / /     


