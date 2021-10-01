import matplotlib.pyplot as plt
import math

plt.style.use('seaborn')
plt.figure(figsize=(7,7))
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-150,150)
plt.ylim(-150,150)
plt.title("Rotation")

def line(x1, y1, x2, y2, c, l) :

    xl = [x1, x2]
    yl = [y1, y2]

    plt.plot(xl, yl, color = c, label = l)

def polygon(x1, y1, x2, y2, x3, y3, x4, y4, c, l) :

    xl = [x1, x2, x3, x4, x1]
    yl = [y1, y2, y3, y4, y1]

    plt.plot(xl,yl, color = c, label = l)

def circle(xc, yc, r, c, l) :

    PI = math.pi
    sa = 0  * (PI / 180)
    ea = 360  * (PI / 180)

    xl = []
    yl = []

    # loop for all theta
    theta = sa 
    while theta <= ea :
        x = (r * math.cos(theta))
        y = (r * math.sin(theta))
        
        xl.append(xc+x)
        yl.append(yc+y)

        theta += 0.01

    plt.scatter(xl , yl, color = c, s = 3, label = l)

def ellipse(xc, yc, rx, ry, c, l) :

    PI = math.pi
    sa = 0  * (PI / 180)
    ea = 360  * (PI / 180)

    xl = []
    yl = []

    # loop for all theta
    theta = sa 
    while theta <= ea :
        x = (rx * math.cos(theta))
        y = (ry * math.sin(theta))

        xl.append(xc+x)
        yl.append(yc+y)

        theta += 0.01

    plt.scatter(xl , yl, color = c, s = 3, label = l)

print("------ ROTATION ------")
print("1. Line")
print("2. Polygon")
print("3. Circle")
print("4. Ellipse")

choice = int(input("Choice : "))

if choice == 1 :

    x1 = int(input("x1 : "))
    y1 = int(input("y1 : "))
    x2 = int(input("x2 : "))
    y2 = int(input("y2 : "))
    theta = int(input("theta : "))
    
    line(x1,y1,x2,y2,"red","Original Line")

    theta = theta * math.pi / 180

    x1_ = x1 * math.cos(theta) - y1 * math.sin(theta)
    y1_ = x1 * math.sin(theta) + y1 * math.cos(theta)
    x2_ = x2 * math.cos(theta) - y2 * math.sin(theta)
    y2_ = x2 * math.sin(theta) + y2 * math.cos(theta)

    line(x1_,y1_,x2_,y2_,"green", "Rotated Line")


elif choice == 2 :

    x1 = int(input("x1 : "))
    y1 = int(input("y1 : "))
    x2 = int(input("x2 : "))
    y2 = int(input("y2 : "))
    x3 = int(input("x3 : "))
    y3 = int(input("y3 : "))
    x4 = int(input("x4 : "))
    y4 = int(input("y4 : "))
    theta = int(input("theta : "))

    polygon(x1,y1,x2,y2,x3,y3,x4,y4,"red","Original Polygon")

    theta = theta * math.pi / 180

    x1_ = x1 * math.cos(theta) - y1 * math.sin(theta)
    y1_ = x1 * math.sin(theta) + y1 * math.cos(theta)
    x2_ = x2 * math.cos(theta) - y2 * math.sin(theta)
    y2_ = x2 * math.sin(theta) + y2 * math.cos(theta)
    x3_ = x3 * math.cos(theta) - y3 * math.sin(theta)
    y3_ = x3 * math.sin(theta) + y3 * math.cos(theta)
    x4_ = x4 * math.cos(theta) - y4 * math.sin(theta)
    y4_ = x4 * math.sin(theta) + y4 * math.cos(theta)

    polygon(x1_,y1_,x2_,y2_,x3_,y3_,x4_,y4_,"green","Rotated Polygon")

elif choice == 3 :

    x = int(input("x : "))
    y = int(input("y : "))
    r = int(input("r : "))
    theta = int(input("theta : "))

    circle(x,y,r,"red", "Original Circle")

    theta = theta * math.pi / 180

    x_ = x * math.cos(theta) - y * math.sin(theta)
    y_ = x * math.sin(theta) + y * math.cos(theta)

    circle(x_,y_,r,"green","Rotated Circle")


elif choice == 4 :

    x = int(input("x : "))
    y = int(input("y : "))
    rx = int(input("rx : "))
    ry = int(input("ry : "))
    theta = int(input("theta : "))

    ellipse(x,y,rx,ry,"red","Original Ellipse")

    theta = theta * math.pi / 180

    x_ = x * math.cos(theta) - y * math.sin(theta)
    y_ = x * math.sin(theta) + y * math.cos(theta)

    ellipse(x_,y_,rx,ry,"green","Rotated Ellipse")

plt.legend()
plt.show()