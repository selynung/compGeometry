# Make sure to run 
#  pip install matplotlib 
#  pip install scipy


import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from line import Line
from point import Point
from circle import Circle

points = np.array([[-7,8], [9,12], [9,0], [-3,-4], [-9,4]])
vor = Voronoi(points)

fig = voronoi_plot_2d(vor)
vert = vor.vertices
print(vert)
plt.show()
l_c = {}
for i in vert:
    mn = 1e9
    for j in points:
        l = Line(Point(i[0], i[1]), Point(j[0],j[1]))
        mn = min(mn, l.length())
    l_c[mn] = i
print(max(l_c, key=l_c.get))
maxLength = (max(l_c, key=l_c.get)).all()
print(maxLength)

# maxCircle = Circle()
# l = Line(Point(points[0][0], points[0][1]), Point(points[1][0], points[1][1]))
# print(lengths)
# print(max(lengths))