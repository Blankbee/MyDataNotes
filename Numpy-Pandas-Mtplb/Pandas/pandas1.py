import pandas as pd
import numpy as np

labels_list=["Python","Java","Cpp","Ruby","JS"]
data_list=[10,20,30,40,50]
s=pd.Series(data_list,labels_list)
print(s)
dataDict={"Data":1,"Machine":2,"Learning":3,"Django":4,"friend":5}
s1=pd.Series(dataDict)
print(s1)
s2=pd.Series([12,13,14,15,16],["Data","Machine","friend","Learning","Flask"])
print(s2)
s3=pd.Series([1,2,3,4,5],["friend","Machine","Data","Learning","Django"])
print("******************************")
total=s3+s2
print(total)
print("*****************")
print(total["friend"])
