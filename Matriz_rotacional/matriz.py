import numpy as np

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

print("Punto original:", p)
print("Rotado 90° sobre eje Y:", rotado_y)
print("Rotado 90° sobre eje Z:", rotado_z)
