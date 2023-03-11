# Regresión lineal simple modelo de entrenamiento
# DAVU
#10 de Marzo 2023
# Analitica de datos Ltin


# Importación de librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importar el data set

dataset = pd.read_csv('Salary_Datanew.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


#Dividir el data set en un conjunto de entrenamiento y conjunto de testing

from sklearn.model_selection import train_test_split
x_train, x_test, y_train,y_test= train_test_split(x, y, test_size=1/3,random_state = 0)

#Creación de modelo de Rrgresión lineal simple con el conjunto de entrenamiento

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train, y_train)

#predecir el conjunto de test

y_pred=regression.predict(x_test)

#Visualizar los resultados de entrenamiento

plt.scatter(x_train,y_train,color="red")
plt.plot(x_train,regression.predict(x_train),color="blue")
plt.title("Sueldo vs Años de experiencia (conjunto de entrenamiento)")
plt.xlabel("Años de experiencia Diego Vargas")
plt.ylabel("Sueldo en $")
plt.show()

# Visualizar los resultados de test
plt.scatter(x_train,y_train,color="red")
plt.plot(x_train,regression.predict(x_train),color="blue")
plt.title("Sueldo vs Años de experiencia (conjunto de testing)")
plt.xlabel("Años de experiencia Diego Vargas")
plt.ylabel("Sueldo en $")
plt.show()


