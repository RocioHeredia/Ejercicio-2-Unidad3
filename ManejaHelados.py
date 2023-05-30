from ClassHelado import Helado

class ManejaHelados:

    def __init__(self):
        self.__lista_Helados = []

    def Cargar_datos_Helados(self, lista_sabores):
        gramos = int(input('Ingrese Gramos: '))
        precio = float(input('Ingrese Precio: '))
        sabor = str(input('Ingrese Sabor: '))
        helado = Helado(gramos, precio)
        while sabor.lower() != 'salir':
            i = 0
            band = False
            while i < len(lista_sabores) and not band:
                if sabor == lista_sabores[i].get_nom():
                    helado.add_Sabor(lista_sabores[i])
                    band = True
                    print('Sabor REGISTRADO')
                else:
                    i += 1
            sabor = input("Ingresar Sabor (finalizar con 'salir'): ")
        self.__lista_Helados.append(helado)
        print("Helado regitrado con exito")

    def Helados_mas_vendidos(self):
        cont_sabores = {}
        for helado in self.__lista_Helados:
            for sabor in helado.get_Sabores():
                if sabor in cont_sabores:
                    cont_sabores[sabor] += 1
                else:
                    cont_sabores[sabor] = 1
        sabores_mas_pedidos = sorted(cont_sabores.items(), key=lambda item: item[1], reverse=True)[:5]
        return sabores_mas_pedidos

    def estimar_gramos_vendidos(self, id_sabor):
        total = 0
        for helado in self.__lista_Helados:
            i = 0
            band = False
            lista = helado.get_Sabores()
            while i < len(lista) and not band:
                if lista[i].get_id() == id_sabor:
                    band = True
                    nombre = lista[i].get_nom()
                    gramos = helado.get_gramos() / len(helado.get_Sabores())
                    total += gramos
                    i += 1
                else:
                    i += 1
            if band == False:
                print(f'El Id {id_sabor} NO SE ENCUENTRA ')

        print(f'El total de gramos vendidos para el sabor {nombre} con Id: {id_sabor} es de {total}gr')

    def Mostrar_sabor_tipo_H(self, tipo_H):
        i = 0
        lista_sabores = []
        while i < len(self.__lista_Helados):
            helado = self.__lista_Helados[i]
            if int(helado.get_gramos()) == tipo_H:
                lista = helado.get_Sabores()
                for sabores in lista:
                    if sabores.get_nom() not in lista_sabores:
                        lista_sabores.append(sabores.get_nom())
                i += 1
            else:
                i += 1
        if lista_sabores:
            print(f'Los sabores vendidos en el tipo de helado {tipo_H} son: ')
            for sabor in lista_sabores:
                print(f'{sabor}')
        else:
            print(f'No se han vendido Helados del tipo {tipo_H}gr')

    def Total_Recaudado(self):
        Total_Recaudado = {}
        for helado in self.__lista_Helados:
            precio = helado.getPrecio()
            if helado.get_gramos() in Total_Recaudado:
                Total_Recaudado[helado.get_gramos()] += precio
            else:
                Total_Recaudado[helado.get_gramos()] = precio
        return Total_Recaudado

    def mostrar(self):
        for helado in self.__lista_Helados:
            helado.mostrar_Todo()

