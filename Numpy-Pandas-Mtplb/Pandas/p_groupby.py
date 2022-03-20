import numpy as np
import pandas as pd
from numpy.random import randn

dataset={"Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
         "Çalışan":["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],
         "Maaş":[3000,3500,2500,4500,4000,2000]
         }
df=pd.DataFrame(dataset)
print(df)
print("***************************")
DepGroup=df.groupby("Departman")
print(DepGroup.sum())
print("***************************")
print(df.groupby("Departman").sum().loc["Bilişim"])
print("***************************")
print(df.groupby("Departman").count())
print("***************************")
print(df.groupby("Departman").max())
print("***************************")
print(df.groupby("Departman").min())
print("***************************")
print(df.groupby("Departman").min()["Maaş"]["Bilişim"])
print("***************************")
print(df.groupby("Departman").mean())
