import matplotlib.pyplot as plt

x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))

dx = x2 - x1 
dy = y2 - y1

steps = max(abs(dx) , abs(dy))

xinc = dx / steps
yinc = dy / steps

x = x1 
y = y1 

xc = []
yc = []

i = 1
while i <= steps + 1:

    xc.append(x)
    yc.append(y)

    x += xinc
    y += yinc

    i += 1

plt.plot(xc, yc)
plt.xlim(0,40)
plt.ylim(0,40)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("DDA Algorithm")
plt.show()







