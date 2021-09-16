import matplotlib.pyplot as plt
import math

plt.style.use('seaborn')
plt.figure(figsize=(7,7))
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-50,150)
plt.ylim(-50,150)
plt.title("Translation")

def line(x1, y1, x2, y2, c) :

    xl = [x1, x2]
    yl = [y1, y2]

    plt.plot(xl, yl, color = c)

def polygon(x1, y1, x2, y2, x3, y3, x4, y4, c) :

    xl = [x1, x2, x3, x4, x1]
    yl = [y1, y2, y3, y4, y1]

    plt.plot(xl,yl, color = c)

def circle(xc, yc, r, c) :

    PI = math.pi
    sa = 0  * (PI / 180)
    ea = 360  * (PI / 180)

    # loop for all theta
    theta = sa 
    while theta <= ea :
        x = (r * math.cos(theta))
        y = (r * math.sin(theta))
        plt.scatter(xc + x , yc + y, color = c, s = 3)
        theta += 0.01

def ellipse(xc, yc, rx, ry, c) :

    PI = math.pi
    sa = 0  * (PI / 180)
    ea = 360  * (PI / 180)

    # loop for all theta
    theta = sa 
    while theta <= ea :
        x = (rx * math.cos(theta))
        y = (ry * math.sin(theta))
        plt.scatter(xc + x , yc + y, color = c, s = 3)
        theta += 0.01

line(2,5,9,10, "red")
polygon(2,5,10,8,20,30,7,9, "yellow")
circle(10,20,30, "blue")
ellipse(2,3,10,40, "green")

plt.show()