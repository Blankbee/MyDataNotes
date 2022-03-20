import numpy as np
import pandas as pd
from numpy.random import randn

a=np.array([[10,20,np.nan],[5,np.nan,np.nan],[21,np.nan,10]])
print(a)
df=pd.DataFrame(a,index=["Index1","Index2","Index3"],columns=["Column1","Column2","Column3"])
print(df)
print("****************")
print(df.dropna())#nan olan bozuk veya eksik veri olan sütunları siler
print("***********************")
print(df.dropna(axis=1))
print("***********************")
print(df.dropna(thresh=2))#fonsiyona threshold değeri veriyoruz yani 2 veya daha fazla düzgün veri varsa o veride nan olsa bile o satırı silmez
print("***********************")
print(df.fillna(100))#nan değerlerini verilern value ile değiştirir
print("***********************")
print(df.sum())#Her bir columndaki değerleri toplar
print("***********************")
print(df.sum().sum())#Birdaha kullanıldığında ilk kullanımda çıkan değerleri toplar
print("***********************")
print(df.size)
print("***********************")
print(df.isnull())
print("***********************")
print(df.isnull().sum().sum())
def calculateMean(df):
    totalSum=df.sum().sum()
    totalNum=df.size-df.isnull().sum().sum()
    return totalSum/totalNum
print(df.fillna(value=calculateMean(df)))
