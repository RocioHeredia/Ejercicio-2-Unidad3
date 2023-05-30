from ManejaHelados import ManejaHelados
from ManejaSabores import ManejaSabores

def menu():
    print("Menú de opciones:")
    print("1. Registrar un helado vendido")
    print("2. Mostrar los 5 sabores de helado más pedidos")
    print("3. Estimar el total de gramos vendidos para un número de sabor")
    print("4. Mostrar los sabores vendidos para un tipo de helado")
    print("5. Mostrar la recaudación por tipo de helado")
    print("0. Salir")

def item1(maneja_H, lista_sabores):
    maneja_H.Cargar_datos_Helados(lista_sabores)

def item2(maneja_H):
    sabores_mas_pedidos = maneja_H.Helados_mas_vendidos()

    print("Los 5 sabores más pedidos son:")
    for sabor, contador in sabores_mas_pedidos:
        print(sabor, contador)

def item3(maneja_H):
    id_s = int(input('Ingrese numero del Sabor: '))
    maneja_H.estimar_gramos_vendidos(id_s)

def item4(maneja_H):
    tipo_H = int(input('Ingrese tipo de Helado: '))
    maneja_H.Mostrar_sabor_tipo_H(tipo_H)

def item5(maneja_H):
    dic_Total_recaudado = maneja_H.Total_Recaudado()
    for gramos, importe in dic_Total_recaudado.items():
        print(f"El importe total recaudado por el tipo de helado de {gramos}gr es de: ${importe}")

if __name__ == '__main__':
    maneja_S= ManejaSabores()
    lista_sabores = maneja_S.Cargar_Arch()
    maneja_H = ManejaHelados()
    opcion = None

    while opcion != 0:
        menu()
        opcion = int(input('Ingrese una opcion: '))
        if opcion == 1:
            item1(maneja_H, lista_sabores)

        elif opcion == 2:
            item2(maneja_H)

        elif opcion == 3:
            item3(maneja_H)

        elif opcion == 4:
            item4(maneja_H)

        elif opcion == 5:
            item5(maneja_H)

        elif opcion == 0:
            print('Saliendo...')
            break
        elif opcion >= 6:
            opcion = int(input('Ingrese una opcion Valida: '))

    maneja_H.mostrar()