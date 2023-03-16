#Diego Vargas Urzúa
#215901462
#Evaluación #1

#pre procesado de datos

#Importar el dataset
dataset = read.csv('Data.csv')
dataset = dataset[, 2:3]

#Dividir los datos en entrenamineto y conjunto de datos de test
#Usar librería "caTools"
library(caTools)
set.seed(123)

split= sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset,split == TRUE)
testing_set = subset(dataset,split == FALSE)