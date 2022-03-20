import numpy as np

a=np.arange(1,21)
a=a.reshape(5,4)
b=a[:,:2]
print(a)
print("*********************")
print(b)
c=np.arange(1,11)
print(c>4)
print(c[c>4])
print("******************************")
x=np.array([5,6,7,8,9])
y=np.array([50,60,70,80,90])
print(x+y)
print(x*y)
print(x/3)
print(np.sqrt(y))

