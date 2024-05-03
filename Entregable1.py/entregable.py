id=input("Ingrese su ID para validar su compra")
Nombre=input("Ingrese el nombre del producto seleccionado")
Descripcion=input("Ingrese descripcion de su producto")
Costo=int(input("ingrese costo de el producto"))
pv=Costo/(1-0.3)
Precio=pv
Cantidad=int(input("Ingrese la cantidad del producto"))
Estado=input("ingrese de este (true or false)")

print(f"Nombre: {Nombre}\n Description:  {Descripcion}  \n costo:  {Costo}  \n cantidad: {Cantidad} \n estado: {Estado} ")
print(f"El precio total es: {pv}")
  