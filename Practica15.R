#Regresion lineal simple
#DAVU Marzo6 de 2023
#Universidad de Guadalajara

#importar el datset
dataset = read.csv ('Salary_Datanew.csv')

#Dividir los datos en conjunto de entrenamiento y conjunto de test
#install.package("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary,SplitRatio = 2/3)
training_set = subset(dataset,split==TRUE)
testing_set = subset(dataset,split==FALSE)

# ajustamos el modelo de regresión

#Ajustar el modelo de regresión lineal simple con el conjunto de entrenamiento
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)
#predecir resultados con el conjunto de test
y_pred=predict(regressor,newdata = testing_set)

#VISUALIZAMOS LOS DATOS CON ggplot2

# Visualización de los resultados en el conjunto de entrenamiento 
#install.packages("ggplot2")

library(ggplot2)
ggplot()+
  geom_point(aes(x=training_set$YearsExperience, y = training_set$Salary),
             colour="red")+
  geom_line(aes(x=training_set$YearsExperience,
                y=predict(regressor,newdata = training_set)),
            colour="blue")+
  ggtitle("Suelo vs A?os de experiencia (Conjunto de entrenamiento)")+
  xlab("A?os de Experiencia Diego Vargas")+
  ylab("Sueldo (en$)")

#visualización de los resultados en el conjunto de testing
ggplot()+
  geom_point(aes(x=training_set$YearsExperience,y =training_set$Salary),
             colour="red")+
  geom_line(aes(x=training_set$YearsExperience,
                y=predict(regressor,newdata = training_set)),
            colour="blue")+
  ggtitle("Suelo vs A?os de experiencia  (Conjunto de entrenamiento)")+
  xlab("A?os de Experiencia Diego Vargas")+
  ylab("Sueldo (en$)")