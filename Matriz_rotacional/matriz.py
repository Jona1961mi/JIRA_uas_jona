import numpy as np
import matplotlib.pyplot as plt

def rotacion_3d(punto, theta, eje='z'):
    if eje == 'x':
        R = np.array([[1, 0, 0],
                      [0, np.cos(theta), -np.sin(theta)],
                      [0, np.sin(theta),  np.cos(theta)]])
    elif eje == 'y':
        R = np.array([[np.cos(theta), 0, np.sin(theta)],
                      [0, 1, 0],
                      [-np.sin(theta), 0, np.cos(theta)]])
    else:  # eje z
        R = np.array([[np.cos(theta), -np.sin(theta), 0],
                      [np.sin(theta),  np.cos(theta), 0],
                      [0, 0, 1]])
    return R @ punto

# Punto inicial
p = np.array([1, 0, 0])

# Rotar 90° (pi/2 rad) sobre Y
rotado_y = rotacion_3d(p, np.pi/2, eje='y')

# Rotar 90° sobre Z
rotado_z = rotacion_3d(p, np.pi/2, eje='z')

# Dibujar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origen
ax.quiver(0, 0, 0, p[0], p[1], p[2], color='r', label="Original")
ax.quiver(0, 0, 0, rotado_y[0], rotado_y[1], rotado_y[2], color='g', label="Rotado eje Y")
ax.quiver(0, 0, 0, rotado_z[0], rotado_z[1], rotado_z[2], color='b', label="Rotado eje Z")

# Configuración gráfica
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()