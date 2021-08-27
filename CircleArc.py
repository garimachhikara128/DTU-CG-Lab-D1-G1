import matplotlib.pyplot as plt
import math

# take input
sa = int(input("Start Angle : "))
ea = int(input("End Angle : "))
xc = int(input("x center : "))
yc = int(input("y center : "))
r = int(input("r : "))

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

    x = (r * math.cos(theta))
    y = (r * math.sin(theta))

    plt.scatter(xc + x , yc + y , color = 'red')

    theta += 0.01

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.title("Circle Arc Drawing Algo")
plt.show()


