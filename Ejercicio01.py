"""
Crear una Clase Producto con los siguientes atributos:
 - código
 - nombre
 - precio
Crea su constructor, getter y setter y una función llamada calcular_total, donde le pasaremos unas unidades y nos debe
calcular el precio final.

"""

class Producto:

   def __init__ (self, codigo, nombre, precio):
       self.__codigo = codigo
       self.__nombre = nombre
       self.__precio = precio

   @property
   def codigo(self):
       return self.__codigo

   @codigo.setter
   def codigo(self, valor):
       self.__codigo = valor

   @property
   def nombre(self):
       return self.__nombre

   @nombre.setter
   def nombre(self, valor):
       self.__nombre = valor

   @property
   def precio(self):
       return self.__precio

   @precio.setter
   def precio(self, valor):
       self.__precio = valor

   def calcular_total(self, unidades):
       return self.__precio * unidades

   def __str__(self):
       return "codigo:" + str(self.__codigo) + ",nombre:" + self.__nombre + ",precio:" + str(self.__precio)


p1 = Producto(1,"Producto1",12)
p1.calcular_total(8)
print(p1.__str__())

