import pandas as pd
import matplotlib.pyplot as plt


# 1. Cargar el archivo.
data = pd.read_csv('credit_card (2).csv')

# 2. Visualizar los primeros 7 registros del conjunto de datos
print(data.head(7))

# 3. Visualizar los últimos 6 registros del conjunto de datos
print(data.tail(6))

# 4. Generar los estadísticos básicos
print(data.describe())

# 5. Completar todos los datos vacíos (na) con ceros (0)
print(data.fillna(0))

# 6. Generar un gráfico de tipo 'scatter' utilizando la variable "hora" en el eje X y la variable "fecha" en el Eje Y.



a = data.plot(x = "hora", y = "fecha", kind = 'scatter', color = "blue")

plt.show()




