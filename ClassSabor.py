class Sabor:
    __idSabor = int
    __ingredientes = ''
    __nombreSabor = ''

    def __init__(self, id=0, nombre='', ingredientes=''):
        self.__idSabor = id
        self.__nombreSabor = nombre
        self.__ingredientes = ingredientes

    def __str__(self):
        return f'Id:{self.__idSabor}, Nombre: {self.__nombreSabor}, Ingredientes: {self.__ingredientes}'

    def get_nom(self):
        return self.__nombreSabor

    def get_id(self):
        return self.__idSabor
