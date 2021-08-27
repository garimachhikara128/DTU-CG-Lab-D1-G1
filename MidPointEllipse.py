import matplotlib.pyplot as plt

rx = int(input("radius on x : "))
ry = int(input("radius on y : "))

xc = int(input("x center : "))
yc = int(input("y center : "))

plt.style.use('seaborn')
plt.figure(figsize=(7,7))

plt.scatter(xc , yc , color='red')

# Region 1
x = 0 
y = ry 

p1 = (ry**2) + (0.25 * (rx ** 2)) - (ry * (rx**2))

while (2 * x * (ry ** 2)) < (2 * y * (rx ** 2)) :

    plt.scatter(x+xc , y+yc , color='red')
    plt.scatter(x+xc , -y+yc , color='red')
    plt.scatter(-x+xc , y+yc , color='red')
    plt.scatter(-x+xc , -y+yc , color='red')

    if p1 < 0 :
        x += 1
        p1 = p1 + (2 * (ry ** 2) * x) + (ry ** 2)

    else :
        x += 1
        y -= 1 
        p1 = p1 + (2 * (ry ** 2) * x) + (ry ** 2) - (2 * (rx ** 2) * y)

# Region 2
p2 = (((x+0.5)**2) * (ry ** 2)) + (((y-1)**2) * (rx**2)) - ((rx**2) * (ry**2))

while y >=0 :

    plt.scatter(x+xc , y+yc , color='red')
    plt.scatter(x+xc , -y+yc , color='red')
    plt.scatter(-x+xc , y+yc , color='red')
    plt.scatter(-x+xc , -y+yc , color='red')

    if p2 > 0 :
        y -= 1
        p2 = p2 + ((rx**2) * (1-2*y))

    else :
        x += 1
        y -= 1
        p2 = p2 + (2 * (ry ** 2) * x) - (2 * (rx ** 2) * y) + (rx**2)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.title("Mid Point Ellipse Drawing Algo")
plt.show()