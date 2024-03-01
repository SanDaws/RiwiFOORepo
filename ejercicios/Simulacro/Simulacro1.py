#lugar de almacenamiento de datos del inventario
inventario={'pan':[2,1000],'queso':[5,200]}
#formato: {'nombre':[unidades,precio],...}
def MenuInicial():
    print("""Riwinventario:
          Escriba una de las siguientes opciones:
          Agregar un nuevo producto: 1
          eliminar un producto: 2
          actualizar informacion de un producto: 3
          buscar  un producto: 4
          imprimir todo el inventario: 5
          salir: S""")
    decision=input("Opcion a la que se dirije: ")
    if decision == '1':#Agregar un nuevo producto
      agregarProduct()
    elif decision == '2':#eliminar un producto
      EliminarProducto()
    elif decision == '3':#actualizar informacion de un producto
      ActualizarProducto()
    elif decision == '4':#buscar un producto
      BuscarElemento()
    elif decision == '5':#imprimir todo el inventario
      ImprimirInventario()
    elif decision == 'S' or decision=='s':#salir
      quit()
    else:
      print("Opcion no valida")
      MenuInicial()
######################################################################
#utilidades

#volver la menu
def volverAMenu():
  #vuelve alla funcion menu inicial
  print("""volviendo al menu principal
        --------------------------
        """)
  MenuInicial()
  
def RevisarEnInventario(nombreProducto):
  #revisa si un numero pertenece a ese espacio
    if nombreProducto in inventario:#revision si el producto ya existe
      return 1
    else:
      return 0
    

def IngresoNombreProducto():
  #busqueda del producto retorna el mismo nombre para almacenarlo
  #permite tambien regresar a la funcion menu inicio al escribir r o R
  nombreProducto=input("Nombre del producto: ")#ingreso del primer prompt
  if nombreProducto== 'R' or nombreProducto=='r':#instruccion para volver
    volverAMenu()
  else:
    return nombreProducto
  
def formatoImpresionElemento(item,unidades,precio):
  #retorna un formato estructurado de impresion de un producto
  formatoImpresion="""{}\t{}\t\t{}""".format(item,unidades,precio)
  return formatoImpresion
  
########################################################################3
#agregar productos
def agregarProduct():
  #permite agregar un producto nuevo
  print("""ingresar producto:  para volver al menu escriba R
        una vez iniciado el proceso debe completarlo""")
  nombreProducto=IngresoNombreProducto()# ingreso nombre generico
  if RevisarEnInventario(nombreProducto)==1:
    print("producto Existente")
    agregarProduct()# revision generica
  unidades=int(input("Unidades del producto: "))
  precio=int(input("Precio por unidad: "))
  inventario[nombreProducto]=[unidades,precio]#nuevo elemento
  print("Producto ingresado exitosa mente")
  agregarProduct()

######################################################################
#Eliminar producto
def EliminarProducto():
  print("""Eliminacionde producto:  para volver al menu escriba R
una vez iniciado el proceso debe completarlo""")
  nombreProducto=IngresoNombreProducto()
  if RevisarEnInventario(nombreProducto)==0:
    print("404:Product Not Found")
    EliminarProducto()
  inventario.pop(nombreProducto)
  print('producto eliminado Satisfactoriamente')
  EliminarProducto()
##############################################################################
#actualizar producto
def ActualizarProducto():
  print("""Actualizacion de producto:  para volver al menu escriba R
una vez iniciado el proceso debe completarlo""")
  nombreProducto=IngresoNombreProducto()
  if RevisarEnInventario(nombreProducto)==0:ActualizarProducto()#producto no encontrado busca otro producto
  print('escriba "=" en la casilla si algo permanece igual')
  unidades=input("Unidades del producto: ")
  unidades=inventario[nombreProducto][0] if unidades== '=' else int(unidades)# ayuda para hacer mas rapido el inventario en caso que algo permanezca igual
  precio=input("Precio por unidad: ")
  precio=inventario[nombreProducto][1] if precio== '=' else int(precio)# ayuda para hacer mas rapido el inventario en caso que precio permanezca igual
  inventario[nombreProducto]=[unidades,precio]
  print('actualizacion exitosa')
  ActualizarProducto()
  
#############################################################################
#buscar
def BuscarElemento():
  print("""Actualizacion de producto:  para volver al menu escriba R
una vez iniciado el proceso debe completarlo""")
  nombreProducto=IngresoNombreProducto()
  if RevisarEnInventario(nombreProducto)==0:
    print("404:Product Not Found")#mensaje de no encontrado
    BuscarElemento()
  print("Nombre\tunidades\tprecio($)")
  print(formatoImpresionElemento(nombreProducto,inventario[nombreProducto][0],inventario[nombreProducto][1]),'\n')
  BuscarElemento()
###############################################################################
#imprimir
def ImprimirInventario():
  print("Nombre\tunidades\tprecio($)")
  for item in inventario:
    print(formatoImpresionElemento(item,inventario[item][0],inventario[item][1]))#impresion bajo formato
  print(' para volver al menu escriba R')
  IngresoNombreProducto()
#main
MenuInicial()