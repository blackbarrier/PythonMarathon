datos_alimentos = [
    {"nombre": "Manzana", "categoria": "Fruta", "proteina": 2, "carbohidrato": 7, "grasa": 0, "cantidad": 150},
    {"nombre": "Banana", "categoria": "Fruta", "proteina": 3, "carbohidrato": 10, "grasa": 0, "cantidad": 150},
    {"nombre": "Chocolate", "categoria": "Fruta", "proteina": 5, "carbohidrato": 15, "grasa": 15, "cantidad": 150},
    {"nombre": "Mani", "categoria": "Fruta", "proteina": 4, "carbohidrato": 9, "grasa": 10, "cantidad": 150},
]

class Alimento:
    def __init__(self, nombre, categoria, proteina, carbohidrato, grasa, caloriasTotales):
        self.nombre=nombre
        self.categoria=categoria
        self.proteina=proteina
        self.carbohidrato=carbohidrato
        self.grasa=grasa
        self.caloriasTotales=caloriasTotales

    def informacion(self):
        print("Nombre:",self.nombre)
        print("Categoria:",self.categoria)
        print("Proteina:",self.proteina)
        print("Carbohidratos:",self.carbohidrato)
        print("Grasa:",self.grasa)
        print("Calorias Totales:",self.caloriasTotales)



# print(*datos_alimentos[0].values())
alimento = Alimento(*datos_alimentos[1].values())

alimentosSeleccionados=[]
alimentosSeleccionados.appned(alimento)
alimento.informacion()