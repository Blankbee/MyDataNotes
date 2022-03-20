import numpy as np
from numpy.core.function_base import linspace
data_list=[1,2,3]
arr=np.array(data_list)
data_list2=[[1,2,3],[4,5,6],[7,8,9]]
arr2=np.array(data_list2)
print(data_list2)
a=np.arange(10,20)
print(a)
b=np.arange(0,100,3)
print(b)
a=np.ones(10)
b=np.zeros(10)
print(b)
print(a)
print("**********************")
print(np.ones((3,4)))
print(np.linspace(0,20,4))#20 yi 4 parçaya bölüp parçaları yaz
print(np.random.randint(15))
print(np.random.rand(5))#0la 1 arasında rastgele 5 sayı üretir
a=np.arange(25)
print(a.reshape(5,5))#arreyi 5 e 5 bir arrey olarak tekrar düzenler
print("**************************")
c=np.random.randint(0,100,10)
print(c)
print(c.max())
print(c.min())
print(c.sum())#Değerlerin toplamı
print(c.mean())#Değerlerin ortalaması
print(c.argmax())#Max değer hangi argümanda onu döndürür
print(c.argmin())
det=np.random.randint(0,100,25)
det=det.reshape(5,5)
print(det)
d=np.linalg.det(det)#Matrisin determinantını bulur
print(d)
print(round(d))#Yuvarlama
a=[1,2,3,4,5]
print[a[1:3]]
a[:2]=25
print(a)