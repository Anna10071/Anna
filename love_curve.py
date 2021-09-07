import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(0 , 2 * np.pi, 1024)
ax = plt.subplot(111, projection='polar')
ax.plot(T, 1. - np.sin(T),color="r")
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  
ax.set_rlabel_position(45) 
ax.grid(True)
ax.set_title("Descartes' Love Curve")
plt.show()
