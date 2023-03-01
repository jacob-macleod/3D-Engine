# 3D-Engine
A custom 3D engine made with python

## Mathematics
This 3D engine was originally based on some mathematics which I derived. Below, you can see the main equation, to find where a point should be based on a number of variables:

* l = distance between screen and camera

* z = z position of point to plot

* d = l-z = distance from point to camera

* x = d-l = distance from point to screen

* c = x or y position of camera

* p = x or y position of point

* r = resultant x or y position of point



`         /          - 1/    d   \ \` 


`r = xtan|180 - tan    |--------| | + p ` 

`         \             \|c - p| / / `  

However, this approach had a number of problems:
* The equation was producing difficult numbers like negative numbers, and it was hard to understand ow to produce nicer numbers
* The equation was complicated, requiring more processing power
* The equation was not completely working

As a result, I did some research, and switched it to the following equation, which solved all these issues:

`point_projected = (focal_length*point)/(focal_length+z)`

This required some changes in the program's visualisation of the 3D scene - it now considers the object, screen and camera in a slightly different order
