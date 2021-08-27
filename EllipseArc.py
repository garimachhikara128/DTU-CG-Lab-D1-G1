import matplotlib.pyplot as plt
import math

# take input
sa = int(input("Start Angle : "))
ea = int(input("End Angle : "))
xc = int(input("X Center : "))
yc = int(input("Y Center : "))
rx = int(input("Radius on X : "))
ry = int(input("Radius on Y : "))

PI = math.pi

# convert sa ea to radians
sa = sa  * (PI / 180)
ea = ea  * (PI / 180)

plt.style.use('seaborn')
plt.figure(figsize=(7,7))

plt.scatter(xc , yc , color='red')

# loop for all theta
theta = sa 

while theta <= ea :

    x = (rx * math.cos(theta))
    y = (ry * math.sin(theta))

    plt.scatter(xc + x , yc + y , color = 'red')

    theta += 0.01

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.title("Ellipse Arc Drawing Algo")
plt.show()


