
import matplotlib.pyplot as plt
import numpy as np
from qutip import *

theta = np.linspace(0,     np.pi, 90)
phi   = np.linspace(0, 2 * np.pi, 60)

fig = plt.figure(figsize=(16,4))
ax = fig.add_subplot(1, 3, 1, projection='3d')
sphereplot(theta, phi, orbital(theta, phi, basis(3, 0)), fig, ax);

ax = fig.add_subplot(1, 3, 2, projection='3d')
sphereplot(theta, phi, orbital(theta, phi, basis(3, 1)), fig, ax);

ax = fig.add_subplot(1, 3, 3, projection='3d')
sphereplot(theta, phi, orbital(theta, phi, basis(3, 2)), fig, ax);

plt.show()

