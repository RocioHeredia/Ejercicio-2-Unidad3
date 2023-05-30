import csv
from ClassSabor import Sabor

class ManejaSabores:

    def __init__(self):
        self.__lista_sabores = []

    def Cargar_Arch(self):
        archivo = open('sabores.csv', encoding='utf-8-sig')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            id_cod = int(fila[0])
            nom = fila[1]
            ingredientes = fila[2]
            sabor = Sabor(id_cod, nom, ingredientes)
            self.__lista_sabores.append(sabor)

        return self.__lista_sabores
