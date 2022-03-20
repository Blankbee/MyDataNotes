import numpy as np
import pandas as pd
from numpy.random import randn
df=pd.DataFrame(randn(4,3),["A","B","C","D"],["Column1","Column2","Column3"])
print(df)
print(df>-1)
print(df[df>0])
print("**********************************")
print(df["Column1"]>0)
print(df[df["Column1"]>0])
print(df["Column2"]>0)
print(df[(df["Column1"]>0) & (df["Column2"]>0)])
print("***************************")
print(df[(df["Column1"]>0) | (df["Column2"]>0)])
print("*******************************")
df["Column4"]=pd.Series(randn(4),["A","B","C","D"])
df["Column5"]=randn(4)#Bu şekilde column eklemek daha kolay
print(df)
print("************************************")
df["Column6"]=["newValue1","newValue2","newValue3","newValue4"]
print(df)
df.set_index("Column6",inplace=True)
print(df)
print(df.index.names)