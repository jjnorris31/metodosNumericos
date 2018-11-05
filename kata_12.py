import matplotlib.pyplot as plt
import math

x = [1, 2, 3, 4, 5]
y = [88.5, 87, 84, 82.5, 79]
n = 5
plt.plot(x, y, 'ro')
plt.show()

sumx = sum(x)
sumy = sum(y)
sumx2 = sum( xi * xi for xi in x  )
sumxy = sum ( xi * yi for xi, yi in zip(x,y) )

m = (sumxy - (sumx*sumy/n))/(sumx2 - (sumx*sumx/n))
b = (sumy/n) - (m * (sumx/n))

print(m,b)

x = [8, 16, 24, 32]
y = [4.1, 4.5, 5.1, 6.1]
n = 4
plt.plot(x, y, 1)
plt.show()

sumx = sum(x)
sumy = sum(y)
sumx2 = sum( xi * xi for xi in x  )
sumxy = sum ( xi * yi for xi, yi in zip(x,y) )

m = (sumxy - (sumx*sumy/n))/(sumx2 - (sumx*sumx/n))
b = (sumy/n) - (m * (sumx/n))

print(m,b)
