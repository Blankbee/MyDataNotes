import pandas as pd

ex=pd.read_html("https://www.rockpapershotgun.com/apex-legends-best-guns-tier-list-weapon-stats")
for i in range(7):
    df=ex[i]
    print(df.head(5))
    print("****************************")
print("*****************************************************************************************")
print("*****************************************************************************************")
df=pd.concat([ex[0],ex[1],ex[2],ex[3],ex[4],ex[5]])
df.reset_index(drop=True,inplace=True)
print(df)
print("**********************")
print(len(df.index))
print("**********************")
print(df["RPM"].mean())
print("**********************")
print(df["Damage"].max())
print("**********************")
print(df["Damage"].min())
print("**********************")
print(df[df["Damage"]==df["Damage"].max()])
print("**********************")
print(df[df["Damage"]==df["Damage"].max()]["Name"])
print("**********************")
print(df[df["Name"]=="L-Star"]["DPS"])
print(df.groupby("Ammo").mean()["RPM"])
print(df["Ammo"].nunique())
print(df["Ammo"].value_counts())
def last_er(name):
    if "er" in name.lower():
        return True
    return False
print(df[df["Name"].apply(last_er)])



