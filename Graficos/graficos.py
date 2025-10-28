import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear la gráfica
plt.plot(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de Seno')
plt.xlabel('X')
plt.ylabel('sin(X)')

# Mostrar la gráfica
plt.show()

import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [10, 12, 25, 30, 45]

# Crear la gráfica de dispersión
plt.scatter(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de Dispersión')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')

# Mostrar la gráfica
plt.show()

