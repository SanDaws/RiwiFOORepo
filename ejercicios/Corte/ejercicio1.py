productos={'pan':2500,'huevos':500}
def MenuTienda():
  #apratir de aca nos movilizaremos hacia todas las cciones
  print("""bienvenido
      escriba el numero de la opcion a la que se dirige:
      Revisar precio de producto: 1
      Nueva factura:2
      Salir: q""")

  respuesta=input("Opcion a la que se dirije: ")

  if respuesta == '1':#Revisar precio producto
    pass
  elif respuesta == '2':#Empezar proceso de facturacion
    RevisarProfuctos()# desarrollo pendiente
  elif respuesta == "q":
    quit()
def FormatoImpresionProducto(llave,valor):
  formatoImpresion = """ producto:
  nombre:{}
  Precio:{}""".format(llave,valor)
  return formatoImpresion
  

def FormatoImpresionProducto(llave,valor,unidades):
  FormatoImpresionProducto="""""".format(llave,valor,unidades)
  return formatoImpresion

def RevisarProfuctos():
  productoBuscado=input("nombre del producto: ")
  if productoBuscado is productos:
    print(FormatoImpresionProducto(productos.key(productoBuscado),productos.values(productoBuscado)))
  else:
    print("producto no encontrado")
  MenuTienda()

    

MenuTienda()