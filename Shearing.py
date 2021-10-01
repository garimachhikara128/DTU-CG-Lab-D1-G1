import matplotlib.pyplot as plt
import math

plt.style.use('seaborn')
plt.figure(figsize=(7,7))
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-50,150)
plt.ylim(-50,150)
plt.title("Translation")

def polygon(x1, y1, x2, y2, x3, y3, x4, y4, c, l) :

    xl = [x1, x2, x3, x4, x1]
    yl = [y1, y2, y3, y4, y1]

    plt.plot(xl,yl, color = c, label = l)


print("------ SHEARING ------")


x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))
x3 = int(input("x3 : "))
y3 = int(input("y3 : "))
x4 = int(input("x4 : "))
y4 = int(input("y4 : "))
shx = int(input("shx : "))
shy = int(input("shy : "))

polygon(x1,y1,x2,y2,x3,y3,x4,y4,"red","Original")

x1_ = x1 + shx * y1
y1_ = y1
x2_ = x2 + shx * y2
y2_ = y2
x3_ = x3 + shx * y3
y3_ = y3
x4_ = x4 + shx * y4
y4_ = y4

polygon(x1_,y1_,x2_,y2_,x3_,y3_,x4_,y4_,"green","Shearing wrt X")

x1_ = x1
y1_ = y1 + shy * x1
x2_ = x2 
y2_ = y2 + shy * x2
x3_ = x3 
y3_ = y3 + shy * x3
x4_ = x4 
y4_ = y4 + shy * x4

polygon(x1_,y1_,x2_,y2_,x3_,y3_,x4_,y4_,"blue","Shearing wrt Y")

plt.legend()
plt.show()