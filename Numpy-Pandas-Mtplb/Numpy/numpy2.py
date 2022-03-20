import numpy as np
a=np.arange(1,10)
b=a
b[:3]=100
print(b)
print(a)
#numpy arraylerinde bir arrayi diğerine eşitlediğimizde bellekte aynı yeri tutarlar 
#dolayısıyla birini değiştirdiğimizde ikiside değişmiş olur
#bunu önlemek için copy() fonksiyonu kullanılır
c=np.arange(1,10)
d=c.copy()
d[:3]=50
print("********************")
print(d)
print(c)