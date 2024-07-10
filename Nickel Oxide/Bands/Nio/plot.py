import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt('Nio.bands.dat.gnu')

k = np.unique(data[:, 0])
bands = np.reshape(data[:, 1], (-1, len(k)))

for band in range(len(bands)):
    plt.plot(k, bands[band, :]-13.874, linewidth=1, alpha=0.5, color='k')
plt.ylim(-22, 15)
plt.xlim(min(k), max(k))

plt.axvline(1.8708, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(4.2160, linewidth=0.75, color='k', alpha=0.5)

plt.xticks(ticks= [0, 1.8708, 4.2160, 5.2160], \
           labels=['$\Gamma$', 'W', 'X', '$\Gamma$'])

plt.axhline(0, linestyle=(0, (5, 5)), linewidth=0.75, color='k', alpha=0.5)


plt.ylabel("E-E_Fermi (ev)")
plt.show()
