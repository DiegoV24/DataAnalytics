#!/usr/bin/env python
# coding: utf-8

# Diego Vargas Urzua
# 215901462
# Fecha: 20/02/23
# Actividad 11 Analítica de Datos 2023-A LTIN

# <h1>HOLA Mundo</h1>

# In[2]:


print("Hola Mundo")


# <h1>Tipos de datos</h1>

# In[3]:


# la función type nos permite ver el tipo de dato de un objeto
type(2)


# In[4]:


type(5.5)


# <h1>Operaciónes</h1>

# In[5]:


1+5


# In[6]:


10-3


# In[7]:


3**4


# In[8]:


5*9


# <h1>Boolean</h1>

# In[10]:


type(True)


# In[11]:


type(False)


# <h1>String, cadena de texto</h1>

# In[12]:


type("Que onda")


# <h1>String métodos</h1>

# In[13]:


# Cambiar mayusculas,minusculas etc
print("Que onda".upper())
print("Que onda".lower())
print("Que onda".title())


# In[14]:


#Contar letras
print("Que onda".count('a'))


# In[15]:


#Reemplazar letras de cadenas de texto
print("Que onda".replace('a','i'))


# <h1>Variables</h1>

# In[19]:


mensaje_1= "No me gusta hacer tarea"


# In[20]:


mensaje_1


# In[21]:


mensaje_2="porque es mucha"


# In[22]:


mensaje_2


# In[23]:


mensaje_1+mensaje_2


# In[24]:


mensaje_1+" "+ mensaje_2


# In[26]:


mensaje=f'{mensaje_1} {mensaje_2}'
mensaje


# <h1>Listas</h1>

# In[27]:


paises=['Mexico','USA','Canada','Japon']


# In[28]:


paises


# In[29]:


paises[0]


# In[31]:


paises[3]


# <h1>Rebanada/Slicing</h1>

# In[32]:


paises


# In[33]:


paises[0:2]


# In[34]:


paises[2:]


# <h1>Operaciones/Metodos</h1>

# In[35]:


paises


# In[36]:


paises.append('Italia')


# In[37]:


paises


# In[38]:


paises.insert(0,'España')


# In[39]:


paises


# In[40]:


paises2=['Francia','Alemania','Colombia']


# In[41]:


paises+paises2


# In[42]:


listanueva=[paises,paises2]


# In[43]:


listanueva


# <h1>Eliminar elementos</h1>

# In[44]:


paises.remove('USA')


# In[45]:


paises


# In[46]:


paises.pop(3)


# In[47]:


paises


# In[48]:


del paises[2]


# In[49]:


paises


# <h1>Ordenar una lista</h1>

# In[50]:


num=[5,4,9,1,10,2]


# In[51]:


num


# In[52]:


num.sort()


# In[53]:


num


# In[54]:


num.sort(reverse=True)


# In[55]:


num


# In[56]:


num[1]=900


# In[57]:


num


# <h1>Ordenar una lista</h1>

# In[58]:


paises.append('Brazil')


# In[59]:


paises


# In[60]:


newlist=paises


# In[61]:


newlist


# In[62]:


newlist=paises.copy()


# In[63]:


newlist


# In[64]:


newlist2=paises[:]


# In[65]:


newlist2


# <h1>Diccionarios</h1>

# In[66]:


midicc={'Key1':'value1', 'Key2':'value2'}


# In[67]:


data={'Nombre':'Diego', 'Edad':23}


# In[68]:


data


# In[69]:


data['Nombre']


# In[70]:


data.keys()


# In[71]:


data.values()


# In[72]:


data.items()


# <h1>Agregar/actualizar elementos</h1>

# In[73]:


data={'Nombre':'Diego', 'Edad':23}


# In[74]:


data['Estatura']=1.80


# In[75]:


data


# In[77]:


data.update({'Estatura':2.0, 'Idioma':['Inglés']})


# In[78]:


data


# <h1>Copiar un diccionario</h1>

# In[79]:


newdicc=data.copy()


# In[80]:


newdicc


# <h1>Eliminar elementos</h1>

# In[81]:


data


# In[82]:


data.pop('Idioma')


# In[83]:


data


# In[84]:


del data['Edad']


# In[85]:


data


# In[86]:


data.clear()


# In[87]:


data


# <h1>Condicional IF </h1>

# In[88]:


edad=25

if edad>=18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolecente")
else:
    print("Eres un bebe")


# In[89]:


paises=['Mexico','Francia','Colombia','España']


# In[90]:


if "Alemania"in paises:
    print("País esta en la lista")
else:
    print("País no REGISTRADO!!!")


# <h1>For loop, bucle FOR</h1>

# In[91]:


for pais in paises:
    print(pais)


# In[92]:


for pais in paises:
    if pais=="Francia":
        print(pais)


# In[93]:


for numero, pais in enumerate(paises):
    print(numero)
    print(pais)


# In[94]:


data={'Nombre':'Diego', 'Edad':23}


# In[95]:


data


# In[96]:


data.items()


# In[97]:


for key, value in data.items():
    print(key)
    print(value)


# <h1>Funciones pre fabricadas</h1>

# In[98]:


paises


# In[99]:


len(paises)


# In[100]:


max(34,70,89,33)


# In[101]:


min(66,22,33,12)


# In[102]:


type(paises)


# In[103]:


round(3.555,2)


# In[106]:


for i in range(1,10,2):
    print(i)


# <h1>Crear una funcion</h1>

# In[107]:


def sumar_numeros(a,b):
    suma_final= a+b
    return suma_final


# In[108]:


sumar_numeros(14,6)


# <h1>Modulos</h1>

# In[109]:


import os


# In[110]:


os.getcwd()


# In[111]:


os.listdir()


# In[112]:


os.makedirs("Nueva Carpeta")


# In[113]:


os.listdir()


# In[ ]:




