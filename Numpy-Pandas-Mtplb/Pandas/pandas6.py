import numpy as np
import pandas as pd

df=pd.DataFrame({
   "Column1":[1,2,3,4,5,6],
   "Column2":[100,100,200,300,300,100],
   "Column3":["Mustafa","Tarık","Bahadır","Burak","Kerem","Emre"]  
})
print(df)
print("******************")
print(df.head(n=3))#ilk 3 indexi basar
print("********************")
print(df["Column2"].unique())#unique değerleri basar
print("**********************")
print(df["Column3"].nunique())#unique değerlerin adetini basar
print("************************")
print(df["Column2"].value_counts())#bir değerden kaç tane var
print("*************************")
print(df[(df["Column1"]>=4) & (df["Column2"]==300)])
print("***************************")
def times3(x):
    return x*3
print(df["Column2"].apply(times3))#Her değere ayrı ayrı fonsiyonu uygular
print("*******************************")
print(df["Column2"].apply(lambda x: x*2))
print("**********************************")
print(df["Column3"].apply(len))
print("**********************************")
print(df.drop("Column3",axis=1))
print("**********************************")
print(len(df.index))
print("**********************************")
print(df.sort_values("Column2"))#Küçükten büyüğe
print("**********************************")
print(df.sort_values("Column2",ascending=False))#Büyükten küçüğe


