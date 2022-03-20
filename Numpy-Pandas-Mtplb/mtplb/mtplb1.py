import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,6)
print(x)
y=np.arange(2,11,2)
print(y)
#plt.plot(x,y,"red")
#plt.show()
plt.subplot(2,2,1)
plt.plot(x,y,"blue")
plt.subplot(2,2,2)
plt.plot(y,x,"blue")
plt.subplot(2,2,3)
plt.plot(y,x,"blue")
plt.subplot(2,2,4)
plt.plot(x,x**2,"blue")
plt.show()