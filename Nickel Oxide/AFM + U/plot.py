import matplotlib.pyplot as plt
import numpy as np

# Load data
energy, dosup, dosdown, idos = np.loadtxt('Nio.dos.dat', unpack=True)

# Make plot
plt.figure(figsize=(12, 6))
plt.plot(energy, dosup, linewidth=1.5, color='red', label='Up')
plt.plot(energy,- dosdown, linewidth=1.5, color='green', label='Down')
plt.xlabel('Energy (eV)', fontsize=22)
plt.ylabel('DOS', fontsize=22)
plt.axhline(y=0, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.axvline(x=15.451, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.xlim(-10, 50)
plt.ylim(-max(abs(min(dosdown)), max(dosup)) - 1, max(max(dosup), abs(min(dosdown))) + 1)
plt.legend()
plt.show()
