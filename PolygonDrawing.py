import matplotlib.pyplot as plt
import math

plt.style.use('seaborn')
plt.figure(figsize=(7,7))
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-50,150)
plt.ylim(-50,150)
plt.title("Polygon Drawing")

def line(x1, y1, x2, y2, c) :

    xl = [x1, x2]
    yl = [y1, y2]

    plt.plot(xl, yl, color = c)

n = int(input("no. of sides ?"))

xl = []
yl = []

i = 1 
while i <= n :

    x = int(input("x" + str(i) + " : "))
    y = int(input("y" + str(i) + " : "))

    xl.append(x)
    yl.append(y)

    i += 1

i = 0 
while i <= n-2 :
    line(xl[i],yl[i],xl[i+1],yl[i+1],"red")
    i += 1

line(xl[0],yl[0],xl[n-1],yl[n-1],"red")

plt.show()
