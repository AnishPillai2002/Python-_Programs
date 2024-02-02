""".Area of the circle given center point (x1,y1) and one point on the perimeter (x2,y2)."""

import math
x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))
radius=math.sqrt((x2-x1)**2+(y2-y1)**2)
area=math.pi*radius**2
print("Area of the circle is: ",area)
