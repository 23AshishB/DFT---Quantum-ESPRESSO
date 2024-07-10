import matplotlib.pyplot as plt
import numpy as np



data = np.loadtxt('NiO.bandsup.dat.gnu')

k = np.unique(data[:, 0])
bands = np.reshape(data[:, 1], (-1, len(k)))

for band in range(len(bands)):
    plt.plot(k, bands[band, :]-15.451, linewidth=1, alpha=0.5, color='k')
plt.ylim(-22, 15)
plt.xlim(min(k), max(k))
plt.axvline(1.0155, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(1.3747, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(2.3111, linewidth=0.75, color='k', alpha=0.5)

plt.xticks(ticks= [0, 1.0155, 1.3747, 2.3111, 2.8415], \
           labels=['$\Gamma$', 'L', 'X','T', '$\Gamma$'])

plt.axhline(0, linestyle=(0, (5, 5)), linewidth=0.75, color='k', alpha=0.5)
plt.ylabel("E-E_Fermi (ev)")
plt.show()
