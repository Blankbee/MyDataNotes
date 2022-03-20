import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,6)
y=np.arange(2,11,2)
fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.5,0.2,0.3])

axes.plot(x,y)

axes.set_xlabel("Outer X")
axes.set_ylabel("Outer Y")
axes.set_title("Outer Graph")

axes2.plot(x,y)

axes2.set_xlabel("Inner X")
axes2.set_ylabel("Inner Y")
axes2.set_title("Inner Graph")
plt.show()