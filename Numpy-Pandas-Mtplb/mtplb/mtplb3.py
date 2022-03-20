import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,6)
y=np.arange(2,11,2)
fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(8,6))#axesi içinde grafikler olan bir array olarak da düşünebiliriz
plt.tight_layout()#Grafikler daha ayrı ve güzel gözükür
#for ax in axes:
#    ax.plot(x,y)#axisin içindeki grafiklerin üzerinde gezerek onlarda verilen işlemi yapar
axes[0].plot(x,y,color="red",label="x-y")
axes[0].plot(x,x**2,color="yellow",label="x kare")
axes[0].plot(x,x**0.5,color="green",label="x karekök")
axes[0].set_xlim(0,20)
axes[0].set_title("First Axes")
axes[0].legend()
axes[1].plot(x,x**3,color="blue",linewidth=10)
axes[1].plot(x,x*7,color="red",linestyle="--")
axes[1].plot(x,x*10,color="black",marker="o",markerfacecolor="red",markeredgecolor="blue")
axes[1].set_title("Second Axes")
#fig1=plt.figure(figsize=(4,4))
#axes2=fig1.add_axes([0,0,1,1])
#axes2.plot(x,y,color="green")
fig.savefig("Figure.png")
plt.show()