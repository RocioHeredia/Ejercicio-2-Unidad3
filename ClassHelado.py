class Helado:
    __sabores = list

    def __init__(self, gramos=0, precio=0.0):
        self.__gramos = gramos
        self.__precio = precio
        self.__sabores = []

    def mostrar_Todo(self):
        print(f"Gramos: {self.__gramos}  Precio: {self.__precio}")
        print('Sabores: ')
        for sabor in self.__sabores:
            print(sabor)

    def add_Sabor(self, sabor):
        self.__sabores.append(sabor)

    def get_Sabores(self):
        return self.__sabores

    def get_gramos(self):
        return self.__gramos

    def getPrecio(self):
        return self.__precio
