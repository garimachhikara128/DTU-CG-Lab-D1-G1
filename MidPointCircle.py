import matplotlib.pyplot as plt

r = int(input("r : "))
xc = int(input("x center : "))
yc = int(input("y center : "))

x = 0 
y = r

p = 5/4 - r

plt.style.use('seaborn')
plt.figure(figsize=(7,7))

while x <= y :

    plt.scatter(x+xc,y+yc,color='red')
    plt.scatter(y+xc,x+yc,color='red')
    plt.scatter(y+xc,-x+yc,color='red')
    plt.scatter(x+xc,-y+yc,color='red')
    plt.scatter(-x+xc,-y+yc,color='red')
    plt.scatter(-y+xc,-x+yc,color='red')
    plt.scatter(-y+xc,x+yc,color='red')
    plt.scatter(-x+xc,y+yc,color='red')

    if p < 0 :
        p = p + 2 * x - 3
    else :
        p = p + 2 * x - 2 * y + 5
        y -= 1

    x += 1


plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.title("Mid Point Circle Drawing Algo")
plt.show()
