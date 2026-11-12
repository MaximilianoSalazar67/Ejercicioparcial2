producto = []
precioProducto = []
unidadesExistencia = []
opcion = []

print("Bienvenido al inventario de articulos")
print("Inventario")
print("1.Dar de alta nuevo producto")
print("2.Eliminar informacion de un producto")
print("3.Modificar informacion de un producto")
print("4.Mostrar informacion de un producto")
print("5.Salir del inventario")
print("---------------------------------")
opcion = int(input("Selecciona una opcion: "))

match opcion:
    case 1: 
        print("Añadir nuevo producto al inventario")
        producto = input("Ingrese el nombre del producto: ")
        precioProducto = float(input("Ingrese el precio del producto: "))
        unidadesExistencia = int(input("Ingrese las unidades en existencia: "))
        print ("producto registrado exitosamente, con el ID: " + str(len(name) - 1))
    case 2: 
        print("Eliminar informacion de un producto")
        producto = input ("Ingrese el nombre del producto a eliminar: ")
    case 3: 
        print("Modificar informacion de un producto")
        producto = input("Ingrese el nombre del producto a modificar: ")
        producto = input("Ingrese el nuevo nombre del producto: ")
        precioProducto = float(input("Ingrese el nuevo precio del producto: "))
        unidadesExistencia = int(input("Ingrese las nuevas unidades en existencia: "))
    case 4:
        print("Mostrar informacion de un producto")
        producto = input("Ingrese el nombre del producto a mostrar: ")
    case 5:
        print("Salir del inventario")
        print("Saliendo del inventario...")
        
        