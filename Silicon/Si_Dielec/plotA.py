import matplotlib.pyplot as plt
import numpy as np

c = 3e8  # m/s
hbar = 6.6e-16  # eV.s

energy, real_epsilon_x, _, _ = np.loadtxt('epsr_silicon.dat', unpack=True)
energy, imag_epsilon_x, _, _ = np.loadtxt('epsi_silicon.dat', unpack=True)

alpha_x = (2*energy)/(c*hbar) * np.sqrt((np.sqrt((real_epsilon_x)**2 + (imag_epsilon_x)**2) - real_epsilon_x) / 2)

# absorbance = alpha_x * thickness

plt.plot(energy, alpha_x)
plt.xlabel('Energy (eV)')
plt.ylabel('Absorption coefficient')
plt.show()
