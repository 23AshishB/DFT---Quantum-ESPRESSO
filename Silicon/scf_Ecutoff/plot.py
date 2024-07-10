import matplotlib.pyplot as plt
import numpy as np

# Load data
energy, E_cutoff = np.loadtxt('etot_vs_ecut.dat', unpack=True)

# Make plot
plt.figure(figsize=(12, 6))
plt.plot(energy, E_cutoff, linewidth=1.5, color='blue')
plt.xlabel('E_Cutoff (eV)', fontsize=22)
plt.ylabel('Total_Energy', fontsize=22)
plt.show()
