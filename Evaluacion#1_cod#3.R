#Diego Vargas Urzúa
#215901462

# Plantilla para pre procesado de datos - DATOS FALTANTES

#importar el data set

dataset= read.csv('Data.csv')

#tratamiento de valores N/A

dataset$Age=ifelse(is.na(dataset$Age),
                   ave(dataset$Age,FUN = function(x) mean(x,na.rm=TRUE)),
                   dataset$Age)

dataset$Salary=ifelse(is.na(dataset$Salary),
                   ave(dataset$Salary,FUN = function(x) mean(x,na.rm=TRUE)),
                   dataset$Salary)