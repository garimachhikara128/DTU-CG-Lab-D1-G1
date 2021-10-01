import matplotlib.pyplot as plt
import math

plt.style.use('seaborn')
plt.figure(figsize=(7,7))
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-150,150)
plt.ylim(-150,150)
plt.title("Reflection")

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

print("------ REFLECTION ------")
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

    line(x1,y1,x2,y2,"red","Original Line")
    line(x1,-y1,x2,-y2,"green", "Reflection X Axis")
    line(-x1,y1,-x2,y2,"blue", "Reflection Y Axis")


elif choice == 2 :

    x1 = int(input("x1 : "))
    y1 = int(input("y1 : "))
    x2 = int(input("x2 : "))
    y2 = int(input("y2 : "))
    x3 = int(input("x3 : "))
    y3 = int(input("y3 : "))
    x4 = int(input("x4 : "))
    y4 = int(input("y4 : "))
   
    polygon(x1,y1,x2,y2,x3,y3,x4,y4,"red","Original Polygon")
    polygon(x1,-y1,x2,-y2,x3,-y3,x4,-y4,"green","Reflection X Axis")
    polygon(-x1,y1,-x2,y2,-x3,y3,-x4,y4,"blue","Reflection Y Axis")

elif choice == 3 :

    x = int(input("x : "))
    y = int(input("y : "))
    r = int(input("r : "))

    circle(x,y,r,"red", "Original Circle")
    circle(x,-y,r,"green","Reflection X Axis")
    circle(-x,y,r,"blue","Reflection Y Axis")


elif choice == 4 :

    x = int(input("x : "))
    y = int(input("y : "))
    rx = int(input("rx : "))
    ry = int(input("ry : "))

    ellipse(x,y,rx,ry,"red","Original Ellipse")
    ellipse(x,-y,rx,ry,"green","Reflection X Axis")
    ellipse(-x,y,rx,ry,"blue","Reflection Y Axis")

plt.legend()
plt.show()