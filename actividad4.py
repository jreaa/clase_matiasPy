"""Estimado(a) estudiante:
Han transcurridos algunos años y en la radio suena Barbie Girl tanto como suena la POO entre sus colegas.
Es por esto que su jefe le ha encargado el desarrollo de un sistema para gestionar una concesionaria de vehículos – cabe
señalar que su jefe aspiraba a cambiar su viejo Kia Pop y esperaba que este cliente le diera un buen descuento -. Los vehículos
se clasifican en: autos, camionetas y motocicletas. 

° Todos los vehículos tienen código único, su marca, tipo (auto, camioneta,
etc.), modelo (nombre del modelo), año, kilometraje y patente.

La concesionaria lleva un registro de las ventas realizadas, y cada registro considera la siguiente información: monto de venta,
fecha de la transacción, vehículo vendido (código), nombre y apellido del comprador, así como su rut.

Utilice clases, sobrecarga y por último, incluya el control de excepciones try-catch de acuerdo a lo aprendido durante la
unidad."""

class Conecesionario():
    def registro(montoVenta, fechaTrans, vehiculoVendido, nombreComprador, apellidoComprador, rutComprador):
        self.montoVenta = montoVenta
        self.fechaTrans = fechaTrans
        self.vehiculoVendido = vehiculoVendido
        self.nombreComprador = nombreComprador
        self.apellidoComprador = apellidoComprador
        self.rutComprador = rutComprador

    def suma(self, a, b):
        resultado = a+b
        return resultado
    
    def suma(self, a, b, c):
        resultado = a+b+c
        return resultado

class Vehiculo():
    def __init__(self, codigo_unique, marca, tipo, modelo, año, kilometraje, patente):
        self.codigo_unique = codigo_unique
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo 
        self.año = año
        self.kilometraje = kilometraje
        self.patente = patente


if __name__ == "__main__" :
    #ejecutcion codigo 
    conecesionario = Conecesionario()
    print(f"La suma es de : {conecesionario.suma(4,5)}")
