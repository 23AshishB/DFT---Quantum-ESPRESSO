import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

# loading data
energy, dos, idos = np.loadtxt('Nio.dos.dat', unpack=True)

#Plot
plt.figure(figsize = (12, 6))
plt.plot(energy, dos, linewidth=0.75, color='red')
plt.xlabel('Energy (eV)',fontsize = 22)
plt.ylabel('DOS',fontsize = 22)
plt.axvline(x=13.874, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.xlim(1, 16)
plt.ylim(0, )
plt.fill_between(energy, 0, dos, where=(energy < 13.874), facecolor='red', alpha=0.25)
plt.show()
