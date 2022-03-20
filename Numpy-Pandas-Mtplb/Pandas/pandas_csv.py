import pandas as pd
import xlrd

dataset=pd.read_csv("USvideos.csv")
ds=dataset.drop(["video_id","trending_date"],axis=1)
print(ds)
print("*********************************")
ds.to_csv("UsVideosNew.csv")
ex=pd.read_excel("excelfile.xlsx")
print(ex)
print("*********************************")
ex["Column5"]=["Mustafa","Tarık","Burak","Bahadır"]
print(ex)
print("*********************************")
ex.to_excel("excelfilenew.xlsx")
ex1=pd.read_html("https://www.contextures.com/xlsampledata01.html")
print(ex1)
print("*********************************")

