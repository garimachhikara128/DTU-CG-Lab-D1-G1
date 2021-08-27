import matplotlib.pyplot as plt

x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))

dx = abs(x2-x1)
dy = abs(y2-y1)

p = 2 * dy - dx

x = x1
y = y1

plt.style.use('seaborn')

while x <= x2 :

    plt.scatter(x,y,color = 'red')

    if p < 0 :
        p = p + 2 * dy
    else :
        p = p + 2*dy - 2*dx
        y += 1

    x += 1

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(0,300)
plt.ylim(0,300)
plt.title("Breshnam's Line Drawing Algo")
plt.show()