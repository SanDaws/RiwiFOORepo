#programa para calcualr el descuento baasado en rango
print("bienvenido")
cantidadProductos=int(input('Cuantos productos desea comprar?:\t'))
preciocompra=int(input('total a pagar:\t'))
descuento=1
if cantidadProductos in range(1,4):#evalua si la cantidad de productos esta entre 1 y 4
    print('No se aplica descuento')
    #en caso de calcular se puede agregar una variable que almacene la cantidad de descuento
elif cantidadProductos in range(5,10):#eval uasi la cantidad de productos esta entre 5 y 10
    print('tienes un descuento del 5%')
    descuento=1.05
    #se puede realizar con una estructura diferente por medio de funciones
elif cantidadProductos in range(11,20):#evalua si la cantidad de productos esta entre 11 y 20
    print('tienes un descuento del 10%')
    descuento=1.10
elif cantidadProductos >20:#eval si la cantidad de productos esta entre 20 en adelante 
    print('tienes un descuento del 15%')
    descuento=1.15
preciocompra=preciocompra/descuento# almacenado por si toca hacer cambio o registro
print(f'el total a pagar es: {preciocompra:.2f}')#entrega el valor con 2 decimales de precision
print('Gracias por comprar con nosotros')#mensaje del final del programa
