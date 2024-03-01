#simulacion de base de datos de productos
productos={'pan':2500,'huevos':500,'leche':3000,'ajo':700,'pimenton':1000}
productosFacturados={}
#menu inicial
def MenuTienda():
  #apratir de aca nos movilizaremos hacia todas las cciones
  print("""
      Bienvenido
      Escriba el numero de la opcion a la que se dirige:
      Nueva factura:1
      Revisar precio de producto:2
      Salir: S""")
  respuesta=input("Opcion a la que se dirije: ")
  if respuesta == '1':#Empezar proceso de facturacion
    Facturacion()#inica el proceso de facturacion de productos
  elif respuesta == '2':#Revisar precio producto
    RevisarProfuctos()
  elif respuesta == "S":
    quit()
##########################################################################
#Este espacio esta hecho como una utilidad adicional para el proyecto
    
def RevisarProfuctos():
  #imprime el haber encotnrado un producto
  productoBuscado=input("nombre del producto: ").lower()
  if productoBuscado in productos:
    print(FormatoImpresionProductoValor(productoBuscado,productos[productoBuscado]))
  else:
    print("producto no encontrado")
    VolverMenuprincipal()
    
###################################################################################
#espacio para los formatos de impresion usados
def FormatoImpresionProductoValor(llave,valor):#recibe 2 cadenas de datos
  #Retorna un string con el nombre de un producto y su valor
  formatoImpresion = """ 
  producto:
  nombre:{}
  Precio:{}""".format(llave,valor)

  return formatoImpresion
  

def FormatoImpresionProducto(llave,valor,unidades):
  #retorna una cadena que muestra el valor total a pagar por un producto
  FormatoImpresionProducto="{}\t{}\t{}\t{}".format(llave,valor,unidades)
  return FormatoImpresionProducto

def FormatoImpresionPersona(nombre, cedula):
  formatoImpresionPersona="""Cedula: {}
  Nombre: {}""".format(cedula,nombre)
  return formatoImpresionPersona

def VolverMenuprincipal():
  print("""Volviendo a menu principal...""")
  productosFacturados.clear()
  MenuTienda()


###################################################################################
#esta seccion es para el apartado de facturacion
def DatosPersonalesUsuario(nombre,cedula):
  #Para evitar usar classes, usare una funcion para que este encapsulada la informacion y sea especifica
  nombrecompleto=nombre
  cedula=int(cedula)
def RecoleccionDatosPersonales():
  #indicamos documento pensando que en una tienda no solo compran personas con cedula
  DatosPersonalesUsuario(input("Nombre completo: "),input("numero de documento: "))
def IngresoProductosFacturados():
  #se puede optimizar con recursividad para evitar el while
  #
  print("Escriba S para acabar la facuracion:")
  while(True):
    #inicializacion de variables
    producto=input("nombre del producto: ")
    if producto== 's'or producto=='S': break#terminador del ciclo
    precio=0
    cantidad=0
    if producto in productos:
      precio=productos[producto]
      cantidad= int(input("cantidad a llevar: "))
      productosFacturados[producto]=[precio,cantidad]

    elif producto not in productos:
      #si no hay un producto dentro de la lista
      productos[producto]=input("precio del producto: ")
      precio=productos[producto]
      cantidad= int(input("cantidad a llevar: "))
      productosFacturados[producto]=[precio,cantidad]

def Facturacion():
#aqui correremos todo el proceso de faturacion
  print("""--------------------------------------------
          iniciando Facturacion:""")
  RecoleccionDatosPersonales()
  IngresoProductosFacturados()
  CheckCompra()

#######################################################################
#proceso de check final antes de pagar
def CheckCompra():
  print("""-------------------------------
        Check in
  """)
  



def descuentos(compra,elementos):#entra el tamaño del diccionario(elementos) y el valor calculado del total(compra)
  #supongamos que no medimos la cantidad de productos por cantidad de productos diferentes y no por cantidad de unidades compradas
 sing=''
 if elementos==1 and compra<=500000:
    sing='19%'
    return compra/(1.19),sing

  if elementos>=3 and elementos<5:
    sing='5%'
    return compra/(1.05),sing
  elif elementos>=5 and elementos<7:
    sing='10%'
    return compra/(1.10),sing
  elif elementos>7:
    sing='cupon por $100.000'
    return compra*1,sing
  
  
def SumatoriaTotal(ProductosComprados:dict):#recibe el diccionario con todos los elementos comprados
  #multiplica unidades * precio y suma y envia a revisar el descuento
  total=0
  for item in ProductosComprados.values():
    total+=CantidadPorPrecio(item[0],item[1])
  return total
def SumatoriaSubtotal(precio,cantidad):
  total=0
  total+=CantidadPorPrecio(cantidad,precio)
  #recibe un diccionario de la siguiente forma: dic[key][punto del arreglo]
  total,descuento=descuentos(total,len(productosFacturados))
  return total,descuento
def CantidadPorPrecio(cantidad,precio):
  #retorna la multiplicacion de todo
  return cantidad*precio

def ImprimirFactura():
  #formato simple, se puede hacer mas optimo haciendo una funcion de recorrido de sumatoria y total pero ya estoy cansado
  factura="""--Riwimercado--
{info}
""".format(info=FormatoImpresionPersona(DatosPersonalesUsuario.nombrecompleto,DatosPersonalesUsuario.cedula))
  print(factura)
  # ex: pan  5000 2 
  factura="""{producto}   subtotal{subtotal}"""
  for item in productosFacturados:
    print(factura.format(FormatoImpresionProducto(item,productosFacturados[item][0],productosFacturados[item][1])), SumatoriaSubtotal(productosFacturados[item][0],productosFacturados[item][1]))
    total,descuento=SumatoriaTotal(productosFacturados)
  factura="""Descuento................................:{}
  Total................................:{}""".format(total, descuento)
  print(factura)
  print("gracias por su compra")
  MenuTienda()


  



#iniciando
MenuTienda()