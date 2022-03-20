import numpy as np
import pandas as pd
from numpy.random import randn

outerIndex=["Group1","Group1","Group1","Group2","Group2","Group2","Group3","Group3","Group3"]
innerIndex=["Index1","Index2","Index3","Index1","Index2","Index3","Index1","Index2","Index3"]
a=list(zip(outerIndex,innerIndex))
print(a)
a=pd.MultiIndex.from_tuples(a)
print("********************************************************************")
print(a)
df=pd.DataFrame(randn(9,3),a,columns=["Column1","Column2","Column3"])
print("***************************************")
print(df)
print("***************************************")
print(df.loc["Group2"])#Grup2'yi bastırma yöntemi
print("***************************************")
print(df.loc["Group1"].loc["Index1"])
print("***************************************")
print(df.loc["Group1"].loc["Index1"].loc["Column1"])
df.index.names=["Groups","Indexes"]
print(df)
print("***********************")
print(df.xs("Group1"))
print("**********************")
print(df.xs("Group2").xs("Index1"))
print("********************")
print(df.xs("Index1",level="Indexes"))#Her gruptaki index1 değerlerini bastırır

