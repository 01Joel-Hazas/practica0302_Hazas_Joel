"""
Añadir una clase Pedido que tiene como atributos:
    - lista de productos
    - lista de cantidades
Añade las siguientes funcionalidades:
    - total_pedido: muestra el precio final del pedido
    - mostrar_productos: muestra los productos del pedido

"""
from Ejercicio01 import Producto

p = Producto(1,"Producto",12)
p2 = Producto(2,"Producto1",13)
p3 = Producto(3,"Producto2",14)

class Pedido:

   def __init__(self, productos, cantidades):
       self.__productos = productos
       self.__cantidades = cantidades

   def total_pedido(self):
       total = 0

       for (p,c) in zip(self.__productos, self.__cantidades):
           total = total + p.calcular_total(c)

       return total


   def __str__(self):
       for (p, c) in zip(self.__productos, self.__cantidades):
           print("Producto:", p, "Cantidad:" + str(c))



print(p.calcular_total(5))
print(p2.calcular_total(6))
print(p3.calcular_total(7))

productos = [p, p2, p3]
cantidades = [6, 12, 1]

pedido = Pedido(productos, cantidades)

print("Total Pedido: " + str(pedido.total_pedido()))

pedido.__str__()