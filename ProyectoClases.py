class Producto:
    def __init__(self, codigoBarras, nombre, proovedor, precio, stock) -> None:
        self.codigoBarras=codigoBarras
        self.nombre=nombre
        self.proovedor=proovedor
        self.precio=precio
        self.stock=stock


    def info(self):
        print("Cod.------",self.codigoBarras)
        print("Nombre----",self.nombre)
        print("Proovedor-",self.proovedor)
        print("Precio----",self.precio)
        print("Stock-----",self.stock)


def lectura():
    carrito=[]
    while cod==999:
        cod=int(input())
        producto=4 #Search in DataBase by codigoBarras
        carrito.append(producto)

def main():
    lectura()
    

main()





producto = Producto(100001,"Arroz gallo","fazzio", 395,199)

