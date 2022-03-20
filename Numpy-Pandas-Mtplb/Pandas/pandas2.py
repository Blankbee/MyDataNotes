import pandas as pd
import numpy as np
from numpy.random import randn
print(randn(3,3))
print("***********************")
df=pd.DataFrame(data=randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])
print(df)
print(df["Column2"])
print(df.loc["A"])
df["Column4"]=pd.Series(randn(3),["A","B","C"])
print(df)
df["Column5"]=df["Column1"]+df["Column2"]+df["Column3"]+df["Column4"]
print("*********************************************")
print(df)
df.drop("Column5",axis=1,inplace=True)#inplace değişkenini True yaptığımızda dataframemizizde yaptığımız değişiklik kalıcı olur
#axis değişkeni eğer sıfırsa işlem satırlar üzerinde,1 ise işlem sütunlar üzerinde uygulanır.
print(df)
print("*************************************")
df.iloc(0)#index arrayinde 0.indexin gösterdiği değerler
print(df.loc["A","Column1"])
print(df.loc[["A","B"],["Column1","Column2"]])
